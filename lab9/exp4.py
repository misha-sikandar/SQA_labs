from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open DemoQA form
driver.get("https://demoqa.com/automation-practice-form")

# Locate checkbox
checkbox = driver.find_element(By.ID, "hobbies-checkbox-1")

# Record initial state
initial_state = checkbox.is_selected()
print("Initial Checkbox State:", initial_state)

# Click checkbox
driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']").click()

# Verify new state
new_state = checkbox.is_selected()
print("State After First Click:", new_state)

# Click checkbox again
driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']").click()

# Verify original state
final_state = checkbox.is_selected()
print("State After Second Click:", final_state)

# Compare initial and final states
print("Returned to Original State:", final_state == initial_state)

# Close browser
driver.quit()