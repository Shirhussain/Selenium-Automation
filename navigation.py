from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("https://www.google.com")
search_box = driver.find_element_by_name('q')
search_box.send_keys('Shir hsussain danishyar')

time.sleep(3)
search_box.submit()
time.sleep(5)

driver.back()
print(driver.title)

time.sleep(3)
driver.forward()
driver.refresh()