import unittest 
from selenium import webdriver
import page 


class PythonOrgSearch(unittest.TestCase):
    # this setUp is call verytime that test function is called
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    # for very function that you are gonna test you have to start with word 'test' at the begining of every function
    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon" 
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()
    # this function gonna run after the testcase is finished.
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
