from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import keys
import time 

driver = webdriver.Chrome()

driver.get("file:///home/shir/newPro/selenium/actionIndex.html")

one= driver.find_element_by_name('one')
two= driver.find_element_by_name('two')
three= driver.find_element_by_name('three')
four= driver.find_element_by_name('four')
five= driver.find_element_by_name('five')
six= driver.find_element_by_name('six')

time.sleep(5)
action = ActionChains(driver)
action.key_down(keys.Keys.CONTROL)
action.click(one)
action.click(two)
action.click(three)
action.click(four)
action.click(five)

action.perform()