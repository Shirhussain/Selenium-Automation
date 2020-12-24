from selenium import webdriver
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://demoqa.com/login")

username = browser.find_element_by_id('userName')
password = browser.find_element_by_id('password')
login = browser.find_element_by_id('login')

username.send_keys('parwiz')
password.send_keys('Parwiz@123')
login.click()

# here we wait until the searbox is become present so after that we gonna continue
try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'searchBox'))
    )
    element.send_keys('grow with danishyar')
    time.sleep(5)
finally:
    browser.close()
