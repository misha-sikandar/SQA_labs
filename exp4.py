from selenium import webdriver
import time
driver=webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(2)

driver.get("https://www.facebook.com")
time.sleep(2)

driver.get("https://www.instagram.com")
time.sleep(2)

driver.back()
driver.back()
print("Twice backwards:",driver.title)
time.sleep(2)

driver.forward()
print("Once Forward:", driver.title)
time.sleep(2)

driver.quit()