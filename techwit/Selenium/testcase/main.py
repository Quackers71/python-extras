import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")

    def test_example(self):
        print("Test")
        assert False

    def test_example_2(self):
        print("Test2")
        assert True

    def not_a_test(self):
        print("This won't print")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
