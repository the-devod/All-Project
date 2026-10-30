import pytest
from src.telemetry_parser import parse_serial_payload


def test_valid_normal_telemetry() -> None:
    payload = '{"distance_cm": 120.5, "accel_g": 1.0}'
    packet = parse_serial_payload(payload)
    assert packet.distance_cm == 120.5
    assert packet.accel_g == 1.0
    assert packet.alert_triggered is False


def test_obstacle_alert_triggered() -> None:
    payload = '{"distance_cm": 12.0, "accel_g": 0.98}'
    packet = parse_serial_payload(payload, obstacle_threshold_cm=20.0)
    assert packet.alert_triggered is True


def test_negative_distance_raises_error() -> None:
    payload = '{"distance_cm": -5.0, "accel_g": 1.0}'
    with pytest.raises(ValueError, match="cannot be negative"):
        parse_serial_payload(payload)
