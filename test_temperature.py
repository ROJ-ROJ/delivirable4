import pytest
from temperature import Temperature

def test_temperature_initialization():
    temp = Temperature(25, "C")
    assert temp.value == 25
    assert temp.unit == "C"
    for unit in ["C", "F", "K"]:
        assert Temperature(25, unit).unit == unit.upper()
def test_read_only():
    t=Temperature(25, "C")
    with pytest.raises(AttributeError):
        t.value = 30
    with pytest.raises(AttributeError):
        t.unit = "F"
def test_invalid_unit():
    with pytest.raises(ValueError):
        Temperature(25, "X")
    with pytest.raises(ValueError):
        Temperature(25).convert_to("X")
@pytest.mark.parametrize("value, unit", [
    (-273.16, "C"),  # Absolute zero in Celsius
    (-459.68, "F"),  # Absolute zero in Fahrenheit
    (-0.01, "K")          # Absolute zero in Kelvin
])
def test_below_absolute_zero(value, unit):
    with pytest.raises(ValueError):
        Temperature(value,unit)
@pytest.mark.parametrize("celsius, fahrenheit, kelvin", [
    (-273.15, -459.67, 0),  # Absolute zero
    (-40, -40, 233.15),  # Same value in C and F
    (0, 32, 273.15),
    (37, 98.6, 310.15),  # Freezing point of water
    (100, 212, 373.15),  # Boiling point of water
])
def test_conversion(celsius, fahrenheit, kelvin):
    for value, unit in [(celsius, "C"), (fahrenheit, "F"), (kelvin, "K")]:
        t=Temperature(value, unit)
        assert t.to_celsius() == pytest.approx(celsius, rel=1e-9)
        assert t.to_fahrenheit() == pytest.approx(fahrenheit, rel=1e-9)
        assert t.to_kelvin() == pytest.approx(kelvin, rel=1e-9)
def test_round_trip():
    original = Temperature(25, "C")
    converted = original.convert_to("F")
    assert converted.unit == "F"
    assert converted.value == pytest.approx(77, abs=1e-9)
    assert original.unit == "C"
    result = converted.convert_to("K").convert_to("C")
    assert result.unit == "C"
    assert result == original
def test_comparison():
    cold = Temperature(0, "C")
    same_cold = Temperature(32, "F")
    warm=Temperature(300, "K")

    assert cold == same_cold
    assert cold != warm
    assert cold < warm
    assert cold <= same_cold
    assert warm > cold
    assert cold >= same_cold
def test_tolerance():
    t=Temperature(1, "k")
    assert t == Temperature(1 + 0.5e-9, "K")
    assert t<Temperature(1 + 2e-9, "K")
def test_string_representation():
    t=Temperature(25, "C")
    assert t.__eq__(25) is NotImplemented
    with pytest.raises(TypeError):
        _=t<25
def test_formatting():
    t=Temperature(25, "C")
    assert str(t) == "25.00 °C"
    assert repr(t) == "Temperature(25.0, 'C')"
    assert str(Temperature(300, "K")) == "300.00 K"