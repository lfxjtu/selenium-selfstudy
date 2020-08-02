
import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('http://www.baidu.com/')
driver.fullscreen_window()
# driver.find_element_by_id("nav-packard-glow-loc-icon").click()
# driver.find_element_by_name("q").send_keys('lfxjtu selenium demo\n')
# driver.find_element_by_link_text('Gmail').click()
# driver.find_element_by_partial_link_text('il').click()
# # driver.find_element_by_name('Sign in').click()
# time.sleep(5)
# driver.back()
# driver.find_element_by_xpath("")

elements = driver.find_elements_by_tag_name('a')
# print (elements)

for element in elements:
    print (element)
    if '视频' in element.text:
        element.click()

