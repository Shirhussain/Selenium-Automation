from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()

browser.get("https://demoqa.com/droppable")


dargable = browser.find_element_by_id('draggable')
droppable = browser.find_element_by_id('droppable')

action = ActionChains(browser)

action.click_and_hold(dargable)
action.release(droppable)

action.perform()