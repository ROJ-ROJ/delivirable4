class Fraction:
    def __init__(self, numerator: int, denominator: int):


        #sjekker om input tallene er gyldige
        if denominator <= 0 or numerator <= 0:
            raise ValueError("Et av input tallene er ikke gyldige.")
        #setter numerator og denominator som attributter
        self.numerator = numerator
        self.denominator = denominator



#lager metoder for å sammenligne brøker
   def __eq__(self, other: "Fraction") -> bool:
        if self.numerator / self.denominator == other.numerator / other.denominator:
            return True
        else:
            return False
    def __ne__(self, other: "Fraction") -> bool:
        if self.numerator / self.denominator == other.numerator / other.denominator:
            return False    
        else:
            return True    

    def __lt__(self, other: "Fraction") -> bool:
        if self.numerator / self.denominator < other.numerator / other.denominator:
            return True
        else:
            return False
    def __le__(self, other: "Fraction") -> bool:
        if self.numerator / self.denominator <= other.numerator / other.denominator:
            return True
        else:
            return False
    def __gt__(self, other: "Fraction") -> bool:
        if self.numerator / self.denominator > other.numerator / other.denominator:
            return True
        else:
            return False
    def __ge__(self, other: "Fraction") -> bool:
        if self.numerator / self.denominator >= other.numerator / other.denominator:
            return True
        else:
            return False
        
    #lager metoder for å enklere gi informasjon om fractonen
    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"


# lager metoder for å multiplisere og dividere brøker
    def __mul__(self, other: "Fraction") -> "Fraction":
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)