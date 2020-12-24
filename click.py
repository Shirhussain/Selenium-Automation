from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os 
import time

url = os.path.dirname(os.path.abspath(__file__))

src = os.path.join(url,"actionIndex.html")

driver = webdriver.Chrome()
driver.get('file:///'+src)

time.sleep(3)

one = driver.find_element_by_name('one')
two = driver.find_element_by_name('two')
three = driver.find_element_by_name('three')
four = driver.find_element_by_name('four')
five = driver.find_element_by_name('five')

action = ActionChains(driver)

action.click(one)
action.click(two)
action.click(three)
action.click(four)
action.click(five)

action.perform()