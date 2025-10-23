import pytest
from calculator import Calculator


# Function-scoped fixture (default)
@pytest.fixture
def calculator():
    """Fixture that provides a Calculator instance"""
    print("\nSetting up calculator")
    calc = Calculator()
    yield calc
    print("\nTearing down calculator")


# Class-scoped fixture
@pytest.fixture(scope="class")
def calculator_class():
    """Fixture with class scope"""
    return Calculator()


# Module-scoped fixture
@pytest.fixture(scope="module")
def calculator_module():
    """Fixture with module scope"""
    print("\nModule setup")
    calc = Calculator()
    yield calc
    print("\nModule teardown")


# Fixture with setup and teardown
@pytest.fixture
def calculator_with_cleanup():
    """Fixture with explicit cleanup"""
    calc = Calculator()
    calc.history = []  # Add some state
    
    yield calc
    
    # Cleanup
    calc.history = None


# Using fixtures in tests
def test_add_with_fixture(calculator):
    """Test using calculator fixture"""
    assert calculator.add(2, 3) == 5


def test_subtract_with_fixture(calculator):
    """Test using calculator fixture"""
    assert calculator.subtract(5, 3) == 2


# Multiple fixtures
@pytest.fixture
def sample_numbers():
    """Fixture providing sample numbers"""
    return {'a': 10, 'b': 5, 'expected_sum': 15}


def test_with_multiple_fixtures(calculator, sample_numbers):
    """Test using multiple fixtures"""
    result = calculator.add(
        sample_numbers['a'], 
        sample_numbers['b']
    )
    assert result == sample_numbers['expected_sum']


# Fixture that uses another fixture
@pytest.fixture
def calculator_with_result(calculator):
    """Fixture that depends on another fixture"""
    result = calculator.add(2, 3)
    return calculator, result


def test_chained_fixtures(calculator_with_result):
    """Test using chained fixtures"""
    calc, previous_result = calculator_with_result
    assert previous_result == 5
    assert calc.multiply(previous_result, 2) == 10


# Using class with fixture
class TestCalculatorWithFixtures:
    """Test class using fixtures"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Fixture that runs automatically for each test"""
        self.calc = Calculator()
        print("\nClass setup")
        yield
        print("\nClass teardown")
    
    def test_add(self):
        assert self.calc.add(2, 3) == 5
    
    def test_multiply(self):
        assert self.calc.multiply(4, 5) == 20
