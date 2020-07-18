import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://www.jianshu.com/search?q=python&page=1&type=note")


    def test_search_by_category(self):
        self.search_field = self.driver.find_element_by_class_name("search-input")
        self.search_field.clear()
        self.search_field.send_keys("monkey")
        self.search_field.submit()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)