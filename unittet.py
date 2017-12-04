import unittest
from selenium import webdriver
from time import sleep

class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Ie()
    def test_baidu(self):
        self.driver.get("http://www..baidu.com/")
        sleep(5)
        self.send_keys("id","kw","test")
        sleep(5)
    def send_keys(self,local,ele,value):
        self.driver.find_element(local,ele).send_keys(value)
    def tearDown(self):
        print("1111")

if __name__ == '__main__':
    unittest.main()
