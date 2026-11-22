from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org")

print("Current URL:", driver.current_url)
print("Page Title:", driver.title)
driver.quit()