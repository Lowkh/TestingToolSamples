import pytest
from calculator import Calculator


def test_add():
    """Test addition"""
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_subtract():
    """Test subtraction"""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2


def test_multiply():
    """Test multiplication"""
    calc = Calculator()
    assert calc.multiply(4, 3) == 12


def test_divide():
    """Test division"""
    calc = Calculator()
    assert calc.divide(10, 2) == 5.0


def test_divide_by_zero():
    """Test division by zero raises exception"""
    calc = Calculator()
    with pytest.raises(ValueError) as excinfo:
        calc.divide(10, 0)
    assert "Cannot divide by zero" in str(excinfo.value)


def test_add_negative():
    """Test addition with negative numbers"""
    calc = Calculator()
    assert calc.add(-2, -3) == -5


def test_multiply_by_zero():
    """Test multiplication by zero"""
    calc = Calculator()
    assert calc.multiply(5, 0) == 0


def test_power():
    """Test power function"""
    calc = Calculator()
    assert calc.power(2, 3) == 8
    assert calc.power(5, 2) == 25


# Multiple assertions in one test
def test_multiple_operations():
    """Test multiple calculator operations"""
    calc = Calculator()
    assert calc.add(1, 1) == 2
    assert calc.subtract(5, 3) == 2
    assert calc.multiply(2, 3) == 6
    assert calc.divide(10, 2) == 5.0
