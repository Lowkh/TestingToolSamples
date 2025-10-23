import pytest
from selenium.webdriver.common.by import By


import chromedriver_autoinstaller

# Auto-install ChromeDriver (no manual download needed!)
chromedriver_autoinstaller.install()


# Test multiple words at once!
@pytest.mark.parametrize("word", [
    "courses",
    "student", 
    "admission",
    "ngee ann"
])
def test_find_important_words(browser, word):
    """Look for important words on NP website."""
    print(f"\nLooking for: {word}")
    
    # Go to NP
    browser.get("https://www.np.edu.sg")
    
    # Get page text
    page_text = browser.page_source.lower()
    
    # Check if word is there
    assert word.lower() in page_text, f"Should find '{word}' on the page!"
    print(f"Found '{word}'!")


def test_page_title_is_correct(browser):
    """Check page title is correct."""
    browser.get("https://www.np.edu.sg")
    
    title = browser.title
    print(f"\nPage title: {title}")
    
    # Title should have NP or Ngee Ann
    assert "NP" in title or "Ngee Ann" in title


def test_at_least_10_links(browser):
    """Check page has at least 10 links."""
    browser.get("https://www.np.edu.sg")
    
    links = browser.find_elements(By.TAG_NAME, "a")
    
    print(f"\nNumber of links: {len(links)}")
    assert len(links) >= 10


def test_at_least_1_image(browser):
    """Check page has at least 1 image."""
    browser.get("https://www.np.edu.sg")
    
    images = browser.find_elements(By.TAG_NAME, "img")
    
    print(f"\nNumber of images: {len(images)}")
    assert len(images) >= 1
