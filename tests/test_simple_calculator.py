"""

"""
import pytest
from calculator import SimpleCalculator

calc = SimpleCalculator()

# -------------------
# Tests fsum
# -------------------

def test_fsum_positive() -> None:
    assert calc.fsum(2, 3) == 5


def test_fsum_negative() -> None:
    assert calc.fsum(-2, -3) == -5


def test_fsum_type_error() -> None:
    with pytest.raises(TypeError):
        calc.fsum("2", 3)
        
# -------------------
# Tests substract
# -------------------

def test_substract_positive() -> None:
    assert calc.substract(5, 3) == 2


def test_substract_negative() -> None:
    assert calc.substract(-5, -3) == -2


def test_substract_type_error() -> None:
    with pytest.raises(TypeError):
        calc.substract(5, None)




# -------------------
# Tests multiply
# -------------------

def test_multiply_basic() -> None:
    assert calc.multiply(4, 3) == 12


def test_multiply_with_zero() -> None:
    assert calc.multiply(4, 0) == 0


def test_multiply_type_error() -> None:
    with pytest.raises(TypeError):
        calc.multiply(4, "3")



# -------------------
# Tests devide
# -------------------

def test_divide_basic() -> None:
    assert calc.divide(6, 3) == 2.0


def test_divide_zero_numerator() -> None:
    assert calc.divide(0, 5) == 0.0


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)


def test_divide_type_error() -> None:
    with pytest.raises(TypeError):
        calc.divide(5, "2")
        
