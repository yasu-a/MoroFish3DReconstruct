from dataclasses import dataclass


# サイズ測定・推定結果
@dataclass
class MeasurementResult:
    length: float
    weight: float
