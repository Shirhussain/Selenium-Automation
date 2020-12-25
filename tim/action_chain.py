from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

# if you refresh this webpage you cans see that it has a littel bet lack so it's better to define 
# before it's completing it's loading you have to define 'implicit wait'
# this means that we won't pass this line until five second 
driver.implicitly_wait(6)

cookie = driver.find_element_by_id('bigCookie')
cookie_counter = driver.find_element_by_id('cookies')
# because in her we have to kind of product price which the first one is for 'Cursor' and second is 
# for grandma which is like 'productPrice0' and 'productPrice1' so we can get with in a list like follows
# how my for loop is working here ---> it's start with '1' and gos to '0' then gos to the end 
# range(10, -1, -1)
# Gives us
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# the reason i reversed because i want to upgrade the more expensive first which is grandma is here 
# upgrade cursor until it's the same price of grand ma and then upgrade grandma, rather upgrade bigger one first
items = [driver.find_element_by_id('productPrice'+str(i)) for i in range(1,-1,-1)]

action = ActionChains(driver)
action.click(cookie)

for i in range(1000):
    action.perform()
    # count = cookie_counter.text
    count = int(cookie_counter.text.split(" ")[0]) 
    print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            # why i redefine the action again? because in our for loop we have different items and we don't know which 
            # item gonna be so we need to redefine action chain
            upgrade_actoins = ActionChains(driver)
            # move our cursor to that element and then click
            upgrade_actoins.move_to_element(item)
            upgrade_actoins.click()
            upgrade_actoins.perform()
