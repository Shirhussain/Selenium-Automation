from selenium import webdriver

driver = webdriver.Chrome()

# driver.get("https://www.google.com")
driver.get("https://the-internet.herokuapp.com/checkboxes")

# search_box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

# print(search_box.is_displayed())
# print(search_box.is_enabled())
# print(search_box.is_selected())

check_box = driver.find_element_by_xpath('//*[@id="checkboxes"]/input[1]')
check_box2 = driver.find_element_by_xpath('//*[@id="checkboxes"]/input[2]')

print(check_box.is_selected())
print(check_box2.is_selected())