from selenium import webdriver
import time
driver = webdriver.Chrome()
# Open Google

driver.get("https://www.google.com")
print("Title:", driver.title)
time.sleep(2)
# Navigate to Wikipedia
driver.get("https://www.wikipedia.org")
print("Title:", driver.title)
time.sleep(2)
# Go Back
driver.back()
print("After Back:", driver.title)
time.sleep(2)
# Go Forward
driver.forward()
print("After Forward:", driver.title)
time.sleep(2)
# Refresh
driver.refresh()
print("After Refresh:", driver.title)
time.sleep(2)
# Close the browser
driver.quit()