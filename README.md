# Bat Functions Testing

This repository contains basic tests for `bat_functions.py` using `pytest` that run on each push.

---

### 1. Basic Tests & Parametrization

- **`calculate_bat_power(level)`**  
  Tested using basic assertions to verify correct output for different levels.

- **`signal_strength(distance)`**  
  Tested using `@pytest.mark.parametrize` to check behavior for multiple distance values.

---

### 2. Tests Using Fixtures

- **`get_bat_vehicle(vehicle_name)`**  
  Tested using a fixture that provides known bat_vehicles. Includes tests to ensure the function raises a `ValueError` for unknown vehicle names.

---

### 3. Monkeypatch and Mock Tests

- **`fetch_joker_info()`**  

  Tested using `monkeypatch` and `pytest-mock` to simulate a fast response and customize the return value of the function.

---

### GitHub Actions Workflow

- **`.github/workflows/pytest.yml`**

    - Runs on **every push**
    - Uses **Ubuntu** and tests with **Python 3.10**
    - Installs dependencies (`pytest` and `pytest-mock`)
    - Runs all `pytest` test functions from `test_bat_functions.py`

---