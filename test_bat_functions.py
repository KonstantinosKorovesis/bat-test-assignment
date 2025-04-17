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


# Fixture Tests
@pytest.fixture(scope="function")
def bat_vehicles():
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50},
    }

def test_get_bat_vehicle(bat_vehicles):
    for vehicle_name in bat_vehicles.keys():
        vehicle_info = get_bat_vehicle(vehicle_name)
        assert vehicle_info == bat_vehicles[vehicle_name]
        assert vehicle_info["speed"] == bat_vehicles[vehicle_name]["speed"]
        assert vehicle_info["armor"] == bat_vehicles[vehicle_name]["armor"]

    for unknown_vehicle_name in ["Batboat", "Batcopter", "Batplane"]:
        with pytest.raises(ValueError, match=f"Unknown vehicle: {unknown_vehicle_name}"):
            get_bat_vehicle(unknown_vehicle_name)