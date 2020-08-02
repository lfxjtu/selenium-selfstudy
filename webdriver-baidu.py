import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.find_element(By.XPATH, "//input[@name ='q']").send_keys("极客时间"+"\n")
print (driver.title)
time.sleep(5)
try:
    assert(driver.title == "极客时间 - Google Search"), "automated test failed."
    print("test automation example passed")
except AssertionError as msg:
    print(msg)
time.sleep(3)
driver.quit()