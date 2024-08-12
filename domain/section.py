from dataclasses import dataclass

import numpy as np


# 断面の情報
@dataclass
class Section:
    idx: int  # フレーム番号
    points: np.ndarray  # 断面上の3D点群
    movement: float  # 1つ前の断面に対して横向きにどのくらい移動したか
