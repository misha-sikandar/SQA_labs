from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form?utm_source=chatgpt.com")
time.sleep(2)

first_name = driver.find_element(By.ID, "firstName")
first_name.send_keys("Misha")

last_name=driver.find_element(By.ID,"lastName")
last_name.send_keys("Sikandar")

email=driver.find_element(By.ID,"userEmail")
email.send_keys("misha@gmail.com")

gender_label=driver.find_element(By.XPATH,"//label[@for='gender-radio-2']")
gender_label.click()
gender = driver.find_element(By.ID, "gender-radio-2")
print("Gender Selected:", gender.is_selected())

mobile = driver.find_element(By.ID, "userNumber")
mobile.send_keys("03001234567")

print("First Name:", first_name.get_attribute("value"))
print("Last Name:", last_name.get_attribute("value"))
print("Email:", email.get_attribute("value"))
print("Gender Selected:", gender.is_selected())
print("Mobile Number:", mobile.get_attribute("value"))

driver.quit()