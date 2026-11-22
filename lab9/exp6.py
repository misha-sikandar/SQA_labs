from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from urllib.parse import quote

# Launch Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Create sample HTML page
html = """
<html>
<body>
    <h2>Country Selection</h2>

    <select id="country">
        <option value="pk">Pakistan</option>
        <option value="us">United States</option>
        <option value="uk">United Kingdom</option>
        <option value="ca">Canada</option>
    </select>

</body>
</html>
"""

# Open page in browser
driver.get("data:text/html;charset=utf-8," + quote(html))

# Locate dropdown
dropdown_element = driver.find_element(By.ID, "country")

# Create Select object
dropdown = Select(dropdown_element)

# 1. Select by visible text
dropdown.select_by_visible_text("Pakistan")
print("Selected by Visible Text:", dropdown.first_selected_option.text)

# 2. Select by index
dropdown.select_by_index(1)
print("Selected by Index:", dropdown.first_selected_option.text)

# 3. Select by value
dropdown.select_by_value("uk")
print("Selected by Value:", dropdown.first_selected_option.text)

# Close browser
driver.quit()