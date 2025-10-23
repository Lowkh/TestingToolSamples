import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# Smoke tests - quick basic tests
@pytest.mark.smoke
def test_basic_addition(calc):
    """Smoke test for addition"""
    assert calc.add(1, 1) == 2


@pytest.mark.smoke
def test_basic_multiplication(calc):
    """Smoke test for multiplication"""
    assert calc.multiply(2, 2) == 4


# Slow tests
@pytest.mark.slow
def test_large_multiplication(calc):
    """Test with large numbers (marked as slow)"""
    result = calc.multiply(1000000, 1000000)
    assert result == 1000000000000


# Skip tests
@pytest.mark.skip(reason="Feature not implemented yet")
def test_modulo(calc):
    """Test modulo operation (not implemented)"""
    assert calc.modulo(10, 3) == 1


# Conditional skip
@pytest.mark.skipif(
    pytest.__version__ < "7.0",
    reason="Requires pytest 7.0 or higher"
)
def test_new_feature(calc):
    """Test that requires specific pytest version"""
    assert calc.add(1, 1) == 2


# Expected failure
@pytest.mark.xfail(reason="Known bug #123")
def test_known_bug(calc):
    """Test for known bug"""
    assert calc.divide(1, 3) == 0.333  # This will fail


# Custom markers
@pytest.mark.critical
@pytest.mark.arithmetic
def test_critical_addition(calc):
    """Critical test for addition"""
    assert calc.add(2, 2) == 4


@pytest.mark.critical
@pytest.mark.arithmetic
def test_critical_division(calc):
    """Critical test for division"""
    assert calc.divide(10, 2) == 5


# Grouping tests in class with markers
@pytest.mark.arithmetic
class TestArithmeticOperations:
    """Group of arithmetic operation tests"""
    
    def test_add(self, calc):
        assert calc.add(2, 3) == 5
    
    def test_subtract(self, calc):
        assert calc.subtract(5, 3) == 2
    
    @pytest.mark.slow
    def test_large_numbers(self, calc):
        assert calc.add(1000000, 2000000) == 3000000
