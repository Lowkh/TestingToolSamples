import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# Basic parameterization
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 5, 5),
    (-2, 3, 1),
    (-4, -6, -10),
])
def test_add_parametrized(calc, a, b, expected):
    """Test addition with multiple parameters"""
    assert calc.add(a, b) == expected


# Parameterization with test names
@pytest.mark.parametrize("a,b,expected", [
    pytest.param(2, 3, 6, id="positive"),
    pytest.param(0, 10, 0, id="with_zero"),
    pytest.param(-2, 4, -8, id="negative"),
], ids=None)  # ids=None uses the id= values above
def test_multiply_parametrized(calc, a, b, expected):
    """Test multiplication with named test cases"""
    assert calc.multiply(a, b) == expected


# Multiple parameter sets
@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (20, 4, 5),
    (100, 10, 10),
])
def test_divide_parametrized(calc, a, b, expected):
    """Test division with parameters"""
    assert calc.divide(a, b) == expected


# Parameterizing with dictionaries
@pytest.mark.parametrize("test_input,expected", [
    ({"a": 2, "b": 3}, 5),
    ({"a": -1, "b": 1}, 0),
    ({"a": 0, "b": 0}, 0),
])
def test_add_with_dict(calc, test_input, expected):
    """Test with dictionary parameters"""
    assert calc.add(**test_input) == expected


# Multiple parametrize decorators (creates cartesian product)
@pytest.mark.parametrize("base", [2, 3, 5])
@pytest.mark.parametrize("exponent", [2, 3])
def test_power_combinations(calc, base, exponent):
    """Test power with all combinations"""
    result = calc.power(base, exponent)
    assert result == base ** exponent


# Parameterized exception testing
@pytest.mark.parametrize("a,b", [
    (10, 0),
    (5, 0),
    (-3, 0),
])
def test_divide_by_zero_parametrized(calc, a, b):
    """Test division by zero with parameters"""
    with pytest.raises(ValueError):
        calc.divide(a, b)


# Complex parameterization
@pytest.mark.parametrize("operation,a,b,expected", [
    ("add", 2, 3, 5),
    ("subtract", 5, 3, 2),
    ("multiply", 4, 3, 12),
    ("divide", 10, 2, 5),
])
def test_all_operations(calc, operation, a, b, expected):
    """Test all operations with one parametrized test"""
    method = getattr(calc, operation)
    assert method(a, b) == expected
