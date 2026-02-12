"""
Tests for the SimpleCalculator class.

Author: Maxime BORNARD
"""
import pytest
from calculator import SimpleCalculator

calc = SimpleCalculator()

# -------------------
# Tests fsum
# -------------------

def test_fsum_positive() -> None:
    """Test addition with positive integers"""
    assert calc.fsum(2, 3) == 5


def test_fsum_negative() -> None:
    """Test addition with negative integers"""
    assert calc.fsum(-2, -3) == -5


def test_fsum_type_error() -> None:
    """Test that fsum raises TypeError with invalid input"""
    with pytest.raises(TypeError):
        calc.fsum("2", 3)
        
# -------------------
# Tests substract
# -------------------

def test_substract_positive() -> None:
    """Test subtraction with positive integers"""
    assert calc.substract(5, 3) == 2


def test_substract_negative() -> None:
    """Test subtraction with negative integers"""
    assert calc.substract(-5, -3) == -2


def test_substract_type_error() -> None:
    """Test that substract raises TypeError with invalid input"""
    with pytest.raises(TypeError):
        calc.substract(5, None)




# -------------------
# Tests multiply
# -------------------

def test_multiply_basic() -> None:
    """Test multiplication of two integers"""
    assert calc.multiply(4, 3) == 12


def test_multiply_with_zero() -> None:
    """Test multiplication by zero"""
    assert calc.multiply(4, 0) == 0


def test_multiply_type_error() -> None:
    """Test that multiply raises TypeError with invalid input."""
    with pytest.raises(TypeError):
        calc.multiply(4, "3")



# -------------------
# Tests devide
# -------------------

def test_divide_basic() -> None:
    """Test division of two integers."""
    assert calc.divide(6, 3) == 2.0


def test_divide_zero_numerator() -> None:
    """Test division when numerator is zero."""
    assert calc.divide(0, 5) == 0.0


def test_divide_by_zero() -> None:
    """Test that division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)


def test_divide_type_error() -> None:
    """Test that divide raises TypeError with invalid input."""
    with pytest.raises(TypeError):
        calc.divide(5, "2")
        
