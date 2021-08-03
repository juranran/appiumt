import unittest
from selenium import webdriver
import time
import record


class InitTest(unittest.TestCase):
    def setUp(self):
        version = input('请输入安卓版本')
        devicename = input('请输入设备id')
        self.luyin = record.Luyin('Android',version,devicename)
        #'7.1.2','127.0.0.1:62001'
    def tearDown(self):
        self.luyin.driver.quit()
