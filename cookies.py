from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.google.com')

# getting all cookies
mycookies = browser.get_cookies()
print(len(mycookies))
print(mycookies)

# adding cookies
cookie = {'name': 'shircookiename', 'value': 'dnaihsyarCookieValue'}
browser.add_cookie(cookie)
mycookies = browser.get_cookies()
print(len(mycookies))
print(mycookies)

# deleting cookie
browser.delete_cookie('shircookiename')
mycookies = browser.get_cookies()
print(len(mycookies))
print(mycookies)
