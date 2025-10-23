#Dependencies needed
pip install pytest
pip install pytest-cov        # For coverage
pip install pytest-bdd        # For BDD tests
pip install pytest-benchmark  # For benchmarking

# Basic Commands
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific file
pytest test_calculator_basic.py

# Run specific test
pytest test_calculator_basic.py::test_add

# Run tests matching pattern
pytest -k "add"

# Run tests with markers
pytest -m smoke
pytest -m "not slow"
pytest -m "critical and arithmetic"

# Only performance benchmarks
pytest --benchmark-only     

 # Stop after 2 failures
pytest --maxfail=2         

