# Import what we need
import chromedriver_autoinstaller
from selenium import webdriver
import time

# Auto-install ChromeDriver (no manual download needed!)
chromedriver_autoinstaller.install()

# Create a browser
print("Opening Chrome browser...")
driver = webdriver.Chrome()

# Make browser full screen
driver.maximize_window()

# Go to NP website
print("Going to NP website...")
driver.get("https://www.np.edu.sg")

# Wait 3 seconds to see the page
time.sleep(3)

# Check the page title
title = driver.title
print(f"Page title is: {title}")

# Check if "NP" or "Ngee Ann" is in the title
if "NP" in title or "Ngee Ann" in title:
    print("SUCCESS! NP website opened correctly!")
else:
    print("OOPS! Something might be wrong.")

# Take a screenshot
driver.save_screenshot("np_website.png")
print("Screenshot saved as 'np_website.png'")

# Close the browser
print("Closing browser...")
driver.quit()
print("Done!")
