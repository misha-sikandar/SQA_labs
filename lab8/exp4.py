from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://the-internet.herokuapp.com/login")

username1 = driver.find_element(By.ID, "username")
print("Username field found using ID")

username2 = driver.find_element(By.NAME, "username")
print("Username field found using NAME")

username3 = driver.find_element(By.XPATH, '//input[@name="username"]')
print("Username field found using XPATH")

driver.quit()
