import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.find_element(By.XPATH, "//input[@name ='q']")

print (driver.find_element(By.XPATH, "//div/img").get_attribute("src"))
print (driver.find_element(By.NAME, "btnK").get_attribute("value"))
print (driver.find_element(By.XPATH, "//a[@data-pid ='23']").text)

driver.find_element(By.NAME,'q').send_keys("abc\n")
driver.find_element(By.XPATH, "//h3[contains(text(),'ABC (Australian Broadcasting Corporation)')]").click()
