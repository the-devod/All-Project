import json
from dataclasses import dataclass
from typing import Any


@dataclass
class TelemetryPacket:
    distance_cm: float
    accel_g: float
    alert_triggered: bool


def parse_serial_payload(raw_json: str, obstacle_threshold_cm: float = 20.0) -> TelemetryPacket:
    """
    Parses incoming microcontroller JSON telemetry and evaluates safety thresholds.
    """
    try:
        data: dict[str, Any] = json.loads(raw_json)
    except json.JSONDecodeError as exc:
        raise ValueError("Malformed JSON telemetry payload") from exc

    if "distance_cm" not in data or "accel_g" not in data:
        raise KeyError("Missing required sensor keys: 'distance_cm' or 'accel_g'")

    distance = float(data["distance_cm"])
    accel = float(data["accel_g"])

    if distance < 0:
        raise ValueError("Sensor distance cannot be negative")

    # Trigger alert if an obstacle is too close or seismic vibration exceeds 2.5G
    alert = (distance <= obstacle_threshold_cm) or (abs(accel) >= 2.5)

    return TelemetryPacket(
        distance_cm=distance,
        accel_g=accel,
        alert_triggered=alert,
    )
