from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open DemoQA form
driver.get("https://demoqa.com/automation-practice-form")

# Locate available gender options
male_label = driver.find_element(
    By.XPATH, "//label[@for='gender-radio-1']"
)

female_label = driver.find_element(
    By.XPATH, "//label[@for='gender-radio-2']"
)

other_label = driver.find_element(
    By.XPATH, "//label[@for='gender-radio-3']"
)

print("Gender options located successfully")

# Locate actual radio buttons
male = driver.find_element(By.ID, "gender-radio-1")
female = driver.find_element(By.ID, "gender-radio-2")
other = driver.find_element(By.ID, "gender-radio-3")

# Select Male
male_label.click()

# Verify Male selection
print("After selecting Male:")
print("Male:", male.is_selected())
print("Female:", female.is_selected())
print("Other:", other.is_selected())

# Select Female
female_label.click()

# Verify Female selection
print("\nAfter selecting Female:")
print("Male:", male.is_selected())
print("Female:", female.is_selected())
print("Other:", other.is_selected())

# Close browser
driver.quit()