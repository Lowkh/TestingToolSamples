import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

# Auto-install ChromeDriver (no manual download needed!)
chromedriver_autoinstaller.install()

@pytest.fixture
def browser():
    # Create Chrome WebDriver instance; chromedriver_autoinstaller ensures driver is present
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("word", [
    "courses",
    "student",
    "admission",
    "ngee ann"
])
def test_find_important_words(browser, word):
    """Look for important words on NP website."""
    browser.get("https://www.np.edu.sg")
    page_text = browser.page_source.lower()
    assert word.lower() in page_text, f"Should find '{word}' on the page!"

def test_page_title_is_correct(browser):
    """Check page title is correct."""
    browser.get("https://www.np.edu.sg")
    title = browser.title
    assert "NP" in title or "Ngee Ann" in title

def test_at_least_10_links(browser):
    """Check page has at least 10 links."""
    browser.get("https://www.np.edu.sg")
    links = browser.find_elements(By.TAG_NAME, "a")
    assert len(links) >= 10

def test_at_least_1_image(browser):
    """Check page has at least 1 image."""
    browser.get("https://www.np.edu.sg")
    images = browser.find_elements(By.TAG_NAME, "img")
    assert len(images) >= 1
