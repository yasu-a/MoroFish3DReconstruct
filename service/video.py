# 動画I/O

import cv2
import numpy as np

from domain.frame import FrameType

_video_path: str | None = None
_cap: cv2.VideoCapture | None = None


def open_video(video_path: str) -> None:
    """
    Set the path of the video.

    :param video_path:
        - Path object to the video file
    """
    global _video_path, _cap
    _video_path = video_path
    _cap = cv2.VideoCapture(video_path)
    assert _cap.isOpened()


def close_video() -> None:
    """
    Close the video.
    """
    _cap.release()


def get_frame_width() -> int:
    """
    Get the width of the video.

    :return:
        - int: width of the video
    """
    # Implement your code here
    raise NotImplementedError()


def get_frame_height() -> int:
    """
    Get the height of the video.

    :return:
        - int: height of the video
    """
    # Implement your code here
    raise NotImplementedError()


def get_frame_count() -> int:
    """
    Get the total number of frames in the video.

    :return:
        - int: number of frames
    """
    # Implement your code here
    raise NotImplementedError()


def get_frame_bgr(idx: int) -> np.ndarray:
    """
    Load a frame in BGR format from the video.

    :param idx:
        - frame index
    :return:
        - np.ndarray: frame in BGR format
    """
    # Implement your code here
    raise NotImplementedError()


def get_frame_type(idx: int) -> FrameType:
    """
    Get the type of frame.

    :param idx:
        - frame index
    :return:
        - FrameType: frame type
    """
    # Implement your code here
    raise NotImplementedError()


def get_previous_frame_index_with_type(idx: int, frame_type: FrameType) -> int | None:
    """
    Get the index of the previous frame with a specific type.

    :param idx:
        - frame index
    :param frame_type:
        - FrameType: frame type
    :return:
        - int | None: previous frame index or None if no previous frame with the given type exists
    """
    for i in reversed(range(idx)):
        if get_frame_type(i) == frame_type:
            return i
    return None
