from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import quote

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Create a sample HTML page
html = """
<html>
<body>
    <h2>Student Registration Form</h2>

    <input type="checkbox" id="terms">
    <label for="terms">Accept Terms</label>

    <br><br>

    <input type="radio" id="male" name="gender">
    <label for="male">Male</label>

    <input type="radio" id="female" name="gender">
    <label for="female">Female</label>

</body>
</html>
"""

# Open the sample page
driver.get("data:text/html;charset=utf-8," + quote(html))

# Locate checkbox by ID
checkbox = driver.find_element(By.ID, "terms")

# Check state before clicking
print("Checkbox before click:", checkbox.is_selected())

# Click checkbox if it is not selected
if not checkbox.is_selected():
    checkbox.click()

# Verify checkbox state
print("Checkbox after click:", checkbox.is_selected())


# Locate radio option using its label
radio_label = driver.find_element(
    By.XPATH, "//label[normalize-space()='Male']"
)

# Click the label
radio_label.click()

# Locate radio input and verify its state
radio = driver.find_element(By.ID, "male")

print("Radio button selected:", radio.is_selected())

# Close browser
driver.quit()