import pytest
from bat_functions import calculate_bat_power, signal_strength, get_bat_vehicle

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


# Monkeypatch Test
def test_fetch_joker_info_monkeypatch(monkeypatch):
    def mock_fetch():
        return {'mischief_level': 0, 'location': 'captured'}

    monkeypatch.setattr("bat_functions.fetch_joker_info", mock_fetch)
    
    from bat_functions import fetch_joker_info
    fetched_info = fetch_joker_info()

    assert fetched_info == {'mischief_level': 0, 'location': 'captured'}
    assert fetched_info['mischief_level'] == 0
    assert fetched_info['location'] == 'captured'


# pytest-mock mocker Test
def test_fetch_joker_info_mocker(mocker):
    mock = mocker.patch("bat_functions.fetch_joker_info", return_value={'mischief_level': 0, 'location': 'captured'})

    from bat_functions import fetch_joker_info
    fetched_info = fetch_joker_info()

    assert fetched_info == {'mischief_level': 0, 'location': 'captured'}
    mock.assert_called_once()