# レーザー切断法で断面上の3D点を

import numpy as np

from domain.frame import FrameType
from video import get_frame_type


def extract_3d_points_on_section(idx: int) -> np.ndarray:
    assert get_frame_type(idx) == FrameType.LASER_EXPOSED

    # ここに処理を書く

    # 返す点群の例
    # points = np.ndarray([
    #     [x1, y1, z1],
    #     [x2, y2, z2],
    #     ...
    # ])
    # return points

    raise NotImplementedError()
