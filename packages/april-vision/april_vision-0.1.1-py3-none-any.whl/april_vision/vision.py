import logging
from pathlib import Path
from sys import platform
from typing import Callable, Dict, List, NamedTuple, Optional, Tuple, Union

import cv2
import numpy as np
from numpy.typing import NDArray
from pyapriltags import Detector

from .marker import Marker

LOGGER = logging.getLogger(__name__)


class Frame(NamedTuple):
    grey_frame: NDArray
    colour_frame: NDArray

    @classmethod
    def from_colour_frame(cls, colour_frame: NDArray) -> 'Frame':
        grey_frame = cv2.cvtColor(colour_frame, cv2.COLOR_BGR2GRAY)

        return cls(
            grey_frame=grey_frame,
            colour_frame=colour_frame,
        )

    @classmethod
    def from_file(cls, filepath: Union[str, Path]) -> 'Frame':
        colour_frame = cv2.imread(str(filepath))

        return cls.from_colour_frame(colour_frame)


class Camera:
    def __init__(
        self,
        index: int,
        resolution: Tuple[int, int],
        calibration: Optional[Tuple[float, float, float, float]] = None,
        tag_sizes: Optional[Dict[int, float]] = None,
        *,
        camera_parameters: Optional[List[Tuple[int, int]]] = None,
        tag_family: str = 'tag36h11',
        threads: int = 4,
        quad_decimate: float = 1,
        aruco_orientation: bool = True,
        name: str = "Camera",
        vidpid: str = "",
        **kwargs,
    ) -> None:
        self._camera = cv2.VideoCapture(index)
        self.calibration = calibration
        self._aruco_orientation = aruco_orientation
        self.name = name
        self.vidpid = vidpid
        if tag_sizes is None:
            self.tag_sizes = {}
        else:
            self.tag_sizes = tag_sizes
        if resolution != (0, 0):
            try:
                self._set_resolution(resolution)
            except AssertionError as e:
                LOGGER.warning(f"Failed to set resolution: {e}")

        if camera_parameters is None:
            camera_parameters = []

        # Set buffer length to 1
        camera_parameters.append((cv2.CAP_PROP_BUFFERSIZE, 1))

        for parameter, value in camera_parameters:
            try:
                self._set_camera_property(parameter, value)
            except AssertionError as e:
                LOGGER.warning(f"Failed to set property: {e}")

        # Maximise the framerate on Linux
        self._optimise_camera(vidpid)

        # Take and discard a camera capture
        _ = self._capture_single_frame()

        self.detector = Detector(
            families=tag_family,
            nthreads=threads,
            quad_decimate=quad_decimate,
        )

        self.capture_filter: Callable[[NDArray], NDArray]
        self.marker_filter: Callable[[List[Marker]], List[Marker]]
        self.detection_hook: Callable[[Frame, List[Marker]], None]

        self.capture_filter = lambda frame: frame
        self.marker_filter = lambda markers: markers
        self.detection_hook = lambda frame, markers: None

    @classmethod
    def from_calibration_file(
            cls,
            index: int,
            calibration_file: Union[str, Path, None],
            name: str = "Camera",
            vidpid: str = "",
            **kwargs,
    ) -> 'Camera':
        if calibration_file is not None:
            calibration_file = Path(calibration_file)
        else:
            return cls(index, resolution=(0, 0), **kwargs)

        if not calibration_file.exists():
            LOGGER.warning(f"Calibrations not found: {calibration_file}")
            return cls(index, resolution=(0, 0), **kwargs)

        storage = cv2.FileStorage(str(calibration_file), cv2.FILE_STORAGE_READ)
        resolution_node = storage.getNode("cameraResolution")
        camera_matrix = storage.getNode("cameraMatrix").mat()
        fx, fy = camera_matrix[0, 0], camera_matrix[1, 1]
        cx, cy = camera_matrix[0, 2], camera_matrix[1, 2]
        return cls(
            index,
            resolution=(
                int(resolution_node.at(0).real()),
                int(resolution_node.at(1).real()),
            ),
            calibration=(fx, fy, cx, cy),
            name=name,
            vidpid=vidpid,
            **kwargs,
        )

    def _set_camera_property(self, property: int, value: int) -> None:
        self._camera.set(property, value)
        actual = self._camera.get(property)

        assert actual == value, (f"Failed to set property '{property}', "
                                 f"expected {value} got {actual}")

    def _set_resolution(self, resolution: Tuple[int, int]) -> None:
        width, height = resolution
        self._set_camera_property(cv2.CAP_PROP_FRAME_WIDTH, width)
        self._set_camera_property(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def _get_resolution(self) -> Tuple[int, int]:
        return (
            int(self._camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(self._camera.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        )

    def _optimise_camera(self, vidpid: str):
        """
        Tweak the camera's image type and framerate to achieve the minimum
        frame time.
        """
        verified_vidpid = {'046d:0825', '046d:0807'}
        if not platform.startswith("linux"):
            # All current optimisations are for linux
            return

        # These may not improve frame time on all cameras
        if vidpid not in verified_vidpid:
            return

        camera_parameters = [
            (cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')),
            (cv2.CAP_PROP_FPS, 30)
        ]

        for parameter, value in camera_parameters:
            try:
                self._set_camera_property(parameter, value)
            except AssertionError as e:
                LOGGER.warning(f"Failed to set property: {e}")

    def _capture_single_frame(self) -> NDArray:
        ret, colour_frame = self._camera.read()
        if not ret:
            raise IOError("Failed to get frame from camera")
        return colour_frame

    def _capture(self, fresh: bool = True) -> Frame:
        if fresh is True:
            # Discard a frame to remove the old frame in the buffer
            _ = self._capture_single_frame()

        colour_frame = self._capture_single_frame()

        # hook to allow modification of the captured frame
        colour_frame = self.capture_filter(colour_frame)

        return Frame.from_colour_frame(colour_frame)

    def _detect(self, frame: Frame) -> List[Marker]:
        if self.calibration is None:
            detections = self.detector.detect(frame.grey_frame)
        else:
            detections = self.detector.detect(
                frame.grey_frame,
                estimate_tag_pose=True,
                camera_params=self.calibration,
                tag_size=self.tag_sizes,
            )

        markers: List[Marker] = []
        for detection in detections:
            markers.append(Marker(
                detection,
                aruco_orientation=self._aruco_orientation
            ))

        # hook to filter and modify markers
        markers = self.marker_filter(markers)

        # hook to extract a frame and its markers
        self.detection_hook(frame, markers)

        return markers

    def _annotate(
        self,
        frame: Frame,
        markers: List[Marker],
        line_thickness: int = 2,
        text_scale: float = 0.5,
    ) -> Frame:
        for marker in markers:
            integer_corners = np.array(marker.pixel_corners, dtype=np.int32)
            marker_id = f"id={marker.id}"

            for frame_type in frame:
                cv2.polylines(
                    frame_type,
                    [integer_corners],
                    isClosed=True,
                    color=(0, 255, 0),  # Green (BGR)
                    thickness=line_thickness,
                )

                # Add square at marker origin corner
                origin_square = np.array([
                    # index -1 is the top-left corner in apriltag
                    # index 1 is correct for aruco's orientation
                    integer_corners[1] + np.array([3, 3]),
                    integer_corners[1] + np.array([3, -3]),
                    integer_corners[1] + np.array([-3, -3]),
                    integer_corners[1] + np.array([-3, 3])
                ], dtype=np.int32)
                cv2.polylines(
                    frame_type,
                    [origin_square],
                    isClosed=True,
                    color=(0, 0, 255),  # red
                    thickness=line_thickness,
                )

                cv2.putText(
                    frame_type,
                    marker_id,
                    np.array(marker.pixel_centre, dtype=np.int32),
                    cv2.FONT_HERSHEY_DUPLEX,
                    text_scale,
                    color=(255, 0, 0),  # blue
                    thickness=2,
                )

        return frame

    def _save(self, frame: Frame, name: Union[str, Path], colour: bool = True) -> None:
        if colour:
            output_frame = frame.colour_frame
        else:
            output_frame = frame.grey_frame

        path = Path(name)
        if not path.suffix:
            LOGGER.warning("No file extension given, defaulting to jpg")
            path = path.with_suffix(".jpg")

        cv2.imwrite(str(path), output_frame)

    def capture(self) -> NDArray:
        return self._capture().colour_frame

    def see(self, *, frame: Optional[NDArray] = None) -> List[Marker]:
        if frame is None:
            frames = self._capture()
        else:
            frames = Frame.from_colour_frame(frame)
        return self._detect(frames)

    def see_ids(self, *, frame: Optional[NDArray] = None) -> List[int]:
        if frame is None:
            frames = self._capture()
        else:
            frames = Frame.from_colour_frame(frame)
        markers = self._detect(frames)
        return [marker.id for marker in markers]

    def save(self, name: Union[str, Path], *, frame: Optional[NDArray] = None) -> None:
        if frame is None:
            frames = self._capture()
        else:
            frames = Frame.from_colour_frame(frame)
        markers = self._detect(frames)
        frames = self._annotate(
            frames,
            markers
        )
        self._save(frames, name)

    def close(self) -> None:
        self._camera.release()
