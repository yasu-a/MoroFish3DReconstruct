# モデルフィッティングの結果から測定をするモジュール

from typing import Any

from domain.measure import MeasurementResult


def _measure_length(args: Any) -> float:  # 何を受け取るかは不明
    raise NotImplementedError()


def _estimate_weight(args: Any) -> float:  # 何を受け取るかは不明
    raise NotImplementedError()


def measure(args: Any) -> MeasurementResult:  # 何を受け取るかは不明
    return MeasurementResult(
        length=_measure_length(args),
        weight=_estimate_weight(args),
    )
