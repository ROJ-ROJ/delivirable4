import pytest
from fractions import Fraction

@pytest.mark.parametrize("num1, den1, num2, den2",[[1,2,3,4],[2,4,6,8],[2,4,6,8],[2,4,6,8]])
def test_fraction_eq(num1, den1, num2, den2):
    assert Fraction(num1, den1) == Fraction(num1, den1)
    assert not Fraction(num1, den1) == Fraction(num2, den2)

@pytest.mark.parametrize("num1, den1, num2, den2",[[1,2,3,4],[2,4,6,8],[2,4,6,8],[2,4,6,8]])
def test_fraction_ne(num1, den1, num2, den2):
    assert not Fraction(num1, den1) != Fraction(num1, den1)
    assert Fraction(num1, den1) != Fraction(num2, den2)

@pytest.mark.parametrize("num1, den1, num2, den2",[[1,2,3,4],[2,4,6,8],[2,4,6,8],[2,4,6,8]])
def test_fraction_lt(num1, den1, num2, den2):
    assert not Fraction(num1, den1) < Fraction(num1, den1)
    assert Fraction(num1, den1) < Fraction(num2, den2)

@pytest.mark.parametrize("num1, den1, num2, den2",[[1,2,3,4],[2,4,6,8],[2,4,6,8],[2,4,6,8]])
def test_fraction_le(num1, den1, num2, den2):
    assert Fraction(num1, den1) <= Fraction(num2, den2)
    assert not Fraction(num2, den1) <= Fraction(num2, den2)

@pytest.mark.parametrize("num1, den1, num2, den2",[[1,2,3,4],[2,4,6,8],[2,4,6,8],[2,4,6,8]])
def test_fraction_gt(num1, den1, num2, den2):
    assert not Fraction(num1, den1) > Fraction(num1, den1)
    assert Fraction(num2, den2) > Fraction(num1, den1) 

@pytest.mark.parametrize("num1, den1, num2, den2",[[1,2,3,4],[2,4,6,8],[2,4,6,8],[2,4,6,8]])
def test_fraction_ge(num1, den1, num2, den2):
    assert Fraction(num2, den2) >= Fraction(num1, den1)
    assert not Fraction(num1, den1) >= Fraction(num2, den2)

@pytest.mark.parametrize("num1, den1, num2, den2",[[1,2,3,4],[2,4,6,8],[2,4,6,8],[2,4,6,8]])
def test_fraction_mul(num1, den1, num2, den2):
    assert Fraction(num1, den1) * Fraction(num2, den2) == Fraction(num1 * num2, den1 * den2)    

@pytest.mark.parametrize("num1, den1, num2, den2",[[1,2,3,4],[2,4,6,8],[2,4,6,8],[2,4,6,8]])
def test_fraction_truediv(num1, den1, num2, den2):
    assert Fraction(num1, den1) / Fraction(num2, den2) == Fraction(num1 * den2, den1 * num2)    


