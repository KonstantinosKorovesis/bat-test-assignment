import pytest
from bat_functions import calculate_bat_power

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