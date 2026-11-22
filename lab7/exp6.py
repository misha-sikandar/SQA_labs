from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.google.com")
print("First Website:")
print("Title:", driver.title)
print("URL:", driver.current_url)


driver.get("https://www.wikipedia.org")
print("\nSecond Website:")
print("Title:", driver.title)
print("URL:", driver.current_url)

driver.back()
print("\nAfter Back:")
print("Title:", driver.title)


driver.forward()
print("\nAfter Forward:")
print("Title:", driver.title)

driver.refresh()
print("\nAfter Refresh:")
print("Title:", driver.title)

driver.quit()
