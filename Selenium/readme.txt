# Run all tests
pytest

# Show more details
pytest -v

# Run specific file
pytest test_simple_np.py

# Run specific test
pytest test_simple_np.py::test_np_website_opens

# See print statements
pytest -v -s
