class Temperature:
    def __init__(self, value, unit="C"):
     if not isinstance(unit, str) or unit.upper()not in ("C","F","K"):
       raise ValueError("Unit must be 'C', 'F', or 'K'")    
     unit = unit.upper()
     value = float(value)
     absolute_zero = {"C": -273.15, "F": -459.67, "K": 0}
     if value < absolute_zero[unit]:
       raise ValueError("temperaturen cannot be below absolute zero.")
     self._value = value
     self._unit = unit
    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit
    def to_celsius(self)-> float:
        if self.unit == "C":
            return self.value
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9
        elif self.unit == "K":
            return self.value - 273.15
    def to_fahrenheit(self) -> float:
        if self.unit == "F":
            return self.value
        return self.to_celsius() * 9 / 5 + 32
    def to_kelvin(self) -> float:
        if self.unit == "C":
            return self.value + 273.15
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9 + 273.15
        elif self.unit == "K":
            return self.value
    def convert_to(self, target_unit: str) -> "Temperature":
        if not isinstance(target_unit,str) or target_unit.upper() not in ("C","F","K"):
            raise ValueError("Target unit must be 'C', 'F', or 'K'")
        target_unit = target_unit.upper()
        if target_unit == self.unit:
            return Temperature(self.value, self.unit)
        elif target_unit == "C":
            return Temperature(self.to_celsius(), "C")
        elif target_unit == "F":
            return Temperature((self.to_celsius() * 9 / 5) + 32, "F")
        elif target_unit == "K":
            return Temperature(self.to_kelvin(), "K")
    def __str__(self) -> str:
        symbol = "K" if self.unit == "K" else f"°{self.unit}"
        return f"{self.value:.2f} {symbol}"

    def __repr__(self) -> str:
        return f"Temperature({self.value!r}, {self.unit!r})"
    def _compare(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        difference = self.to_kelvin() - other.to_kelvin()
        if abs(difference) < 1e-9:
            return 0
        if difference < 0:
            return -1
        return 1
    def __eq__(self, other):
        result = self._compare(other)
        if result is NotImplemented:
            return NotImplemented
        return result == 0
    def __ne__(self, other):
        result = self._compare(other)
        if result is NotImplemented:
            return NotImplemented
        return result != 0
    def __lt__(self, other):
        result = self._compare(other)
        if result is NotImplemented:
            return NotImplemented
        return result < 0
    def __le__(self, other):
        result = self._compare(other)
        if result is NotImplemented:
            return NotImplemented
        return result <= 0  
    def __gt__(self, other):
        result = self._compare(other)
        if result is NotImplemented:
            return NotImplemented
        return result > 0 
    def __ge__(self, other):
        result = self._compare(other)
        if result is NotImplemented:
            return NotImplemented
        return result >= 0  