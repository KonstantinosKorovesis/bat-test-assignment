import pytest
from bat_functions import calculate_bat_power, signal_strength, get_bat_vehicle, fetch_joker_info

# Basic Tests
def test_calculate_bat_power():
    assert calculate_bat_power(-10) == -420
    assert calculate_bat_power(-5) == -210
    assert calculate_bat_power(-2) == -84
    assert calculate_bat_power(-1) == -42
    assert calculate_bat_power(0) == 0
    assert calculate_bat_power(1) == 42
    assert calculate_bat_power(2) == 84
    assert calculate_bat_power(5) == 210
    assert calculate_bat_power(10) == 420
    assert calculate_bat_power(42) == 1764
    assert calculate_bat_power(100) == 4200
    assert calculate_bat_power(1000) == 42000
    assert calculate_bat_power(10000) == 420000

# Parametrization Tests
@pytest.mark.parametrize("distance, expected_signal_strength", [
    (0, 100), (1, 90), (2, 80), (3, 70), (4, 60), (5, 50), (10, 0),
    (11, 0), (12, 0), (15, 0), (50, 0), (100, 0), (1000, 0), (10000, 0)
])
def test_signal_strength(distance, expected_signal_strength):
    assert signal_strength(distance) == expected_signal_strength