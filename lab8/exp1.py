from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/html/html_forms.asp')
# By ID
elem_id = driver.find_element(By.ID, 'fname')
print('Found by ID:', elem_id.get_attribute('placeholder'))
# By Tag Name — find all links
links = driver.find_elements(By.TAG_NAME, 'a')
print('Total links on page:', len(links))
# By CSS Selector
btn = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
print('Button found:', btn.get_attribute('value'))
driver.quit()