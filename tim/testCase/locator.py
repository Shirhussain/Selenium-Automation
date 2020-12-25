# the idea here for locator is that any kind of 'CSS' selector should be in a specific location
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON =  (By.ID, "submit")

class SearchResultPageLocators(object):
    pass 
