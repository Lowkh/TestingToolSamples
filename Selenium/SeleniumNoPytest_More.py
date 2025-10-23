import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Auto-install ChromeDriver
chromedriver_autoinstaller.install()

# Start browser
print("\n" + "="*50)
print("Testing NP Website - Simple Checks")
print("="*50 + "\n")

driver = webdriver.Chrome()
driver.maximize_window()

# Go to NP website
driver.get("https://www.np.edu.sg")
time.sleep(3)

# Test 1: Check page title
print("Test 1: Checking page title...")
title = driver.title
print(f"  Page title: {title}")

if "Ngee Ann" in title or "NP" in title:
    print("PASS - Title looks good!")
else:
    print("FAIL - Title doesn't look right")

# Test 2: Check page loaded (not blank)
print("\nTest 2: Checking if page loaded...")
page_text = driver.page_source

if len(page_text) > 1000:  # Page should have lots of content
    print("PASS - Page has content!")
else:
    print("FAIL - Page seems empty")

# Test 3: Look for the word "courses"
print("\nTest 3: Looking for 'Courses' on the page...")
if "courses" in page_text.lower() or "course" in page_text.lower():
    print("PASS - Found 'Courses'!")
else:
    print("FAIL - Didn't find 'Courses'")

# Test 4: Count how many links are on the page
print("\nTest 4: Counting links on the page...")
links = driver.find_elements(By.TAG_NAME, "a")
print(f"  Found {len(links)} links")

if len(links) > 10:
    print("PASS - Page has plenty of links!")
else:
    print("FAIL - Page doesn't have many links")

# Test 5: Count how many images are on the page
print("\nTest 5: Counting images on the page...")
images = driver.find_elements(By.TAG_NAME, "img")
print(f"  Found {len(images)} images")

if len(images) > 0:
    print("PASS - Page has images!")
else:
    print("FAIL - Page has no images")

# Summary
print("\n" + "="*50)
print("All tests completed!")
print("="*50)

# Take screenshot
driver.save_screenshot("np_test_results.png")
print("\nScreenshot saved!")

# Close browser
time.sleep(2)
driver.quit()
print("Browser closed. Goodbye!")
