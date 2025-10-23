import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add_performance(benchmark, calc):
    """Benchmark addition operation"""
    result = benchmark(calc.add, 100, 200)
    assert result == 300


def test_multiply_performance(benchmark, calc):
    """Benchmark multiplication operation"""
    benchmark(calc.multiply, 500, 7)


def test_divide_performance(benchmark, calc):
    """Benchmark division operation"""
    benchmark(calc.divide, 1000, 10)


# Benchmark with setup
def test_complex_calculation_performance(benchmark):
    """Benchmark complex calculation with setup"""
    calc = Calculator()
    
    def setup():
        # Expensive setup
        pass
    
    def run():
        result = calc.add(100, 200)
        result = calc.multiply(result, 2)
        return result
    
    benchmark.pedantic(run, setup=setup, rounds=100)
