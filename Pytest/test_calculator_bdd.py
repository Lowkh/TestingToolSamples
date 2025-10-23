import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from calculator import Calculator

# Load all scenarios from feature file
scenarios('features/calculator.feature')


# Fixtures
@pytest.fixture
def calculator_context():
    """Context to hold calculator and results"""
    return {
        'calculator': None,
        'result': None,
        'error': None
    }


# Given steps
@given('I have a calculator')
def given_calculator(calculator_context):
    """Create calculator instance"""
    calculator_context['calculator'] = Calculator()


# When steps
@when(parsers.parse('I add {a:d} and {b:d}'))
def when_add(calculator_context, a, b):
    """Add two numbers"""
    calc = calculator_context['calculator']
    calculator_context['result'] = calc.add(a, b)


@when(parsers.parse('I subtract {b:d} from {a:d}'))
def when_subtract(calculator_context, a, b):
    """Subtract b from a"""
    calc = calculator_context['calculator']
    calculator_context['result'] = calc.subtract(a, b)


@when(parsers.parse('I multiply {a:d} and {b:d}'))
def when_multiply(calculator_context, a, b):
    """Multiply two numbers"""
    calc = calculator_context['calculator']
    calculator_context['result'] = calc.multiply(a, b)


@when(parsers.parse('I divide {a:d} by {b:d}'))
def when_divide(calculator_context, a, b):
    """Divide a by b"""
    calc = calculator_context['calculator']
    try:
        calculator_context['result'] = calc.divide(a, b)
    except ValueError as e:
        calculator_context['error'] = e


# Then steps
@then(parsers.parse('the result should be {expected:d}'))
def then_result_integer(calculator_context, expected):
    """Check integer result"""
    assert calculator_context['result'] == expected


@then(parsers.parse('the result should be {expected:f}'))
def then_result_float(calculator_context, expected):
    """Check float result"""
    assert calculator_context['result'] == expected


@then('I should get an error')
def then_error(calculator_context):
    """Check that error occurred"""
    assert calculator_context['error'] is not None
