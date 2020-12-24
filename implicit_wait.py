from selenium import webdriver


browser = webdriver.Chrome()

# implicit wait is good for every kind of element but some times it take a lot of time so 
# implicit wait is not enough for use so we have to use 'explicit wait' 
# because in explicit wait we can set some pre define custom condation to wait for processing
browser.implicitly_wait(9)

browser.get("https://demoqa.com/login")

username = browser.find_element_by_id('userName')
password = browser.find_element_by_id('password')
login = browser.find_element_by_id('login')

username.send_keys('parwiz')
password.send_keys('Parwiz@123')
login.click()
