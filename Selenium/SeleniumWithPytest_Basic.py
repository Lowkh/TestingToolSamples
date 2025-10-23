# Simple tests for beginners using pytest

def test_np_website_opens(browser):
    """Test 1: Check if NP website opens."""
    print("\nTest: Opening NP website")
    
    # Go to NP website
    browser.get("https://www.np.edu.sg")
    
    # Check the title
    title = browser.title
    print(f"Page title: {title}")
    
    # This checks if test passes or fails
    assert "Ngee Ann" in title or "NP" in title, "Title should mention NP!"


def test_page_has_content(browser):
    """Test 2: Check if page has content."""
    print("\nTest: Checking page content")
    
    # Go to NP website
    browser.get("https://www.np.edu.sg")
    
    # Get the page HTML
    page_source = browser.page_source
    
    # Page should be long (have lots of content)
    print(f"Page length: {len(page_source)} characters")
    assert len(page_source) > 1000, "Page should have content!"


def test_page_has_links(browser):
    """Test 3: Check if page has links."""
    print("\nTest: Counting links")
    
    from selenium.webdriver.common.by import By
    
    # Go to NP website
    browser.get("https://www.np.edu.sg")
    
    # Find all links
    links = browser.find_elements(By.TAG_NAME, "a")
    
    print(f"Found {len(links)} links")
    assert len(links) > 10, "Page should have many links!"


def test_find_courses_word(browser):
    """Test 4: Look for word 'courses'."""
    print("\nTest: Looking for 'courses'")
    
    # Go to NP website
    browser.get("https://www.np.edu.sg")
    
    # Get page text
    page_text = browser.page_source.lower()
    
    # Check if 'courses' is there
    if "courses" in page_text or "course" in page_text:
        print("Found 'courses'!")
    else:
        print("Didn't find 'courses'")
    
    assert "courses" in page_text or "course" in page_text


def test_page_has_images(browser):
    """Test 5: Check if page has images."""
    print("\nTest: Counting images")
    
    from selenium.webdriver.common.by import By
    
    # Go to NP website
    browser.get("https://www.np.edu.sg")
    
    # Find all images
    images = browser.find_elements(By.TAG_NAME, "img")
    
    print(f"   Found {len(images)} images")
    assert len(images) > 0, "Page should have at least one image!"
