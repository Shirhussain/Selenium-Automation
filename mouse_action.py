from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
import os 
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
url = os.path.dirname(os.path.abspath(__file__))

src = os.path.join(url,"actionIndex.html")
# file:///home/shir/newPro/selenium/actionIndex.html

driver = webdriver.Chrome()
# i use file:/// becuase i'm in linux
driver.get('file:///'+src)

# i wanna select just the third element 

three = driver.find_element_by_name('three')

l = three.location
s = three.size 
print(f'coordinates: {l}')
print(f'size: {s}')

action = ActionChains(driver)
action.move_by_offset(11, 86)

time.sleep(5)
action.click().perform()

