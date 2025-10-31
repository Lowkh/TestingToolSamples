import pytest
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Fixture to handle browser setup and teardown
@pytest.fixture
def browser():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_np_website_opens(browser):
    """Test 1: Check if NP website opens."""
    print("\nTest: Opening NP website")
    browser.get("https://www.np.edu.sg")
    title = browser.title
    print(f"Page title: {title}")
    assert "Ngee Ann" in title or "NP" in title, "Title should mention NP!"

def test_page_has_content(browser):
    """Test 2: Check if page has content."""
    print("\nTest: Checking page content")
    browser.get("https://www.np.edu.sg")
    page_source = browser.page_source
    print(f"Page length: {len(page_source)} characters")
    assert len(page_source) > 1000, "Page should have content!"

def test_page_has_links(browser):
    """Test 3: Check if page has links."""
    print("\nTest: Counting links")
    browser.get("https://www.np.edu.sg")
    links = browser.find_elements(By.TAG_NAME, "a")
    print(f"Found {len(links)} links")
    assert len(links) > 10, "Page should have many links!"

def test_find_courses_word(browser):
    """Test 4: Look for word 'courses'."""
    print("\nTest: Looking for 'courses'")
    browser
