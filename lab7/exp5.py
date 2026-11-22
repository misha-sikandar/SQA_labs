from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://youtube.com")

page_title1=driver.title
driver.refresh()
page_title2=driver.title

if page_title1==page_title2:
    print("The title remained same before and after refresh.")
else:
    print("The title did not remain same.")

driver.quit()