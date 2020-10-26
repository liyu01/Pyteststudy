#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestTestdemo():
    def setup_method(self, method):
        #  电脑启用922端口，调用启动Chrome
        #  C:\Users\86176\AppData\Local\Google\Chrome\Application\chrome --remote-debugging-port=9222
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)
