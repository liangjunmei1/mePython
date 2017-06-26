from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Search1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        url = "http://127.0.0.1:8013/iwebshop"
        self.driver.get(url)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_search(self):
        driver = self.driver
        driver.find_element_by_id("word").click()
        driver.find_element_by_id("word").clear()
        driver.find_element_by_id("word").send_keys("ipad")
        driver.find_element_by_css_selector("input.btn").click()
        driver.find_element_by_css_selector("h3.title > a.p_name").click()
        driver.find_element_by_css_selector("img").click()
        driver.find_element_by_id("5dbc98dcc983a70728bd082d1a47546e").click()
        print "search1 pass"

    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
