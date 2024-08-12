from enum import IntEnum


# フレームタイプ
class FrameType(IntEnum):
    UNKNOWN = 0  # レーザーが写っているかどうか微妙なフレーム
    TEMPLATE = 1  # レーザーが完全に写っていないフレーム
    LASER_EXPOSED = 2  # レーザーが完全に写っているフレーム
