class Temperature:
    #initaliserer verdiene til klassen
    def __init__(self, value, unit="C"):
     #sjekker om input verdiene er gyldige
     if not isinstance(unit, str) or unit.upper()not in ("C","F","K"):
       raise ValueError("Unit must be 'C', 'F', or 'K'")    
    #gjør unit til uppercase for å unngå problemer med små og store bokstaver
     unit = unit.upper()
     #gjør value til float
     value = float(value)
     #sjekker om temperaturen er under absolutt null
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
    #converterer temperaturen til celsius
    def to_celsius(self)-> float:
        if self.unit == "C":
            return self.value
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9
        elif self.unit == "K":
            return self.value - 273.15
    #circulerer temperaturen til fahrenheit
    def to_fahrenheit(self) -> float:
        if self.unit == "F":
            return self.value
        elif self.unit == "C": 
            return self.value * 9 / 5 + 32
        elif self.unit == "K": 

            return (self.value - 273.15) * 9 / 5 + 32
    #converterer temperaturen til kelvin
    def to_kelvin(self) -> float:
        if self.unit == "C":
            return self.value + 273.15
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9 + 273.15
        elif self.unit == "K":
            return self.value
    #converterer temperaturen til en annen enhet
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
    #lager metoder for å gi informasjon om temperaturen
    def __str__(self) -> str:
        return f"Tempraturen er {self.value:.2f} {self.unit}"

    def __repr__(self) -> str:
        return f"Temperature({self.value!r}, {self.unit!r})"

    #lager metoder for å sammenligne temperaturer
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