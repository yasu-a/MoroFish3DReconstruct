# 断面の点群から全身の点群を再構成する

import numpy as np

from domain.section import Section


def construct_3d_points_from_sections(sections: list[Section]) -> np.ndarray:
    raise NotImplementedError()

    # 例： return np.ndarray([[x1, y1, z1], [x2, y2, z2], ...])
