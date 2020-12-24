from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://demoqa.com/selectable")


one = driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[1]')
two = driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[2]')
three = driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[3]')
four = driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[4]')


action = ActionChains(driver)
action.click(one)
action.click(two)
action.click(three)
action.click(four)

action.perform()