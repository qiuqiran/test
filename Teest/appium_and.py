#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from appium import webdriver
import time
import os

#---nexus 6p----
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '8.1'
# desired_caps['deviceName'] = 'CVH7N15B14004484'
# desired_caps['appPackage'] = 'com.petter.swisstime_android'
# desired_caps['appActivity'] = 'com.petter.swisstime_android.ui.WelcomeGuideActivity'
#
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#




from appium import webdriver
import time
import unittest


class And_test(unittest.TestCase):
    '''android Teest'''

    def setUp(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '8.0'
        self.desired_caps['deviceName'] = '5EF0218108007755'
        self.desired_caps['app'] = 'E:\kew\kkk\kew-webapp\com.UCMobile_12.0.2.982_982.apk'  # 测试apk包的路径
        self.desired_caps['noReset'] = True  # 不需要每次都安装apk
        self.desired_caps['appPackage'] = 'com.UCMobile'
        self.desired_caps['appActivity'] = 'com.UCMobile.main.UCMobile'
        self.desired_caps['unicodeKeyboard'] = True
        self.desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        time.sleep(1)
        self.driver.get_window_size()

    def tearDown(self):
        time.sleep(1)
        self.driver.close_app()
        print('关闭app')

    def test_01(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        time.sleep(1)
        time.sleep(1)
        self.driver.swipe(6 / 7 * x, 6 / 7 * y, 6 / 7 * x, 1 / 7 * y, 300)  # 向上滑动
        time.sleep(1)
        self.driver.swipe(6 / 7 * x, 1 / 7 * y, 6 / 7 * x, 6 / 7 * y, 300)  # 向下滑动
        time.sleep(1)
        print('滑动首页')






if __name__=='__main__':
    unittest.main()



