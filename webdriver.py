import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://google.com")
print (driver.find_element(By.TAG_NAME, "img").get_attribute("src"))
print (driver.find_element(By.NAME, "btnK").get_attribute("value"))
print (driver.find_element(By.NAME, "btnI").get_attribute("value"))
driver.find_element(By.NAME,'q').send_keys("abc\n")

driver.find_element(By.PARTIAL_LINK_TEXT, "Australian Broadcasting").click()
