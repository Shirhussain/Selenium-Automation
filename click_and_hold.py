from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os 
import time

url = os.path.dirname(os.path.abspath(__file__))

src = os.path.join(url,"sortable.html")

driver = webdriver.Chrome()
driver.get('file:///'+src)

time.sleep(3)

one = driver.find_element_by_name('one')
teen = driver.find_element_by_name('teen')

action = ActionChains(driver)
action.click_and_hold(one)
action.release(teen)

action.perform()
