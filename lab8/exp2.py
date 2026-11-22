
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open a sample website
driver.get("https://the-internet.herokuapp.com/login")

time.sleep(2)

# 1. Absolute XPath (fragile — avoid)
elem1 = driver.find_element(
    By.XPATH, "/html/body/div[2]/div/div/form/div[1]/div/input"
)
print("Absolute XPath:", elem1.get_attribute("name"))

# 2. Relative XPath (preferred)
elem2 = driver.find_element(
    By.XPATH, '//input[@name="username"]'
)
print("Relative XPath:", elem2.get_attribute("name"))

# 3. XPath with text()
link = driver.find_element(
    By.XPATH, '//a[text()="Elemental Selenium"]'
)
print("Text XPath:", link.text)

# 4. XPath with contains()
link2 = driver.find_element(
    By.XPATH, '//a[contains(text(),"Elemental")]'
)
print("Contains XPath:", link2.text)

# 5. XPath — parent-child
child = driver.find_element(
    By.XPATH, '//div[@id="content"]/div'
)
print("Parent-Child XPath:", child.tag_name)

# Close browser
driver.quit()
