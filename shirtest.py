from selenium import webdriver
import time

# sudo apt-get install chromium-chromedriver
browser = webdriver.Chrome()
# browser.get('http://www.google.com')

# print(browser.title)
# print(browser.current_url)
# print(browser.page_source)
# browser.fullscreen_window()
# browser.maximize_window()
# browser.set_window_size(5
# 00,500)
# browser.set_window_rect(x=800,y=50, width=400, height=500)
# browser.close()

"""
search_box = browser.find_element_by_name('q')
search_box.send_keys('Shirhussain Danishyar')
time.sleep(3)
search_box.submit()
"""

# search_box = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
# search_box.send_keys('Shir Hussain Danishyar')
# search_box.submit()

browser.get("https://demoqa.com/text-box")


input_field1 = browser.find_element_by_id('userName')
input_field2 = browser.find_element_by_id('userEmail')
input_field3 = browser.find_element_by_id('currentAddress')
input_field4 = browser.find_element_by_id('permanentAddress')

time.sleep(3)
input_field1.send_keys('Hu3in danishyar')
time.sleep(2)
input_field2.send_keys('sh.danishyarkhan@gmail.com')
time.sleep(2)
input_field3.send_keys('Kabul Afghanistan')
time.sleep(2)
input_field4.send_keys('Kabul Afghanistan Shar now')
time.sleep(4)

btn_submit = browser.find_element_by_id('submit')
btn_submit.click()

