from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")
search = driver.find_element(By.NAME, "q")
search.send_keys("Selenium WebDriver tutorial")
time.sleep(1)
search.clear()
search.send_keys("Software Quality Engineering")
search.send_keys(Keys.RETURN)
time.sleep(2)
print("Results page title:", driver.title)
driver.quit()