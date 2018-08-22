# coding: utf-8

from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'MI'
desired_caps['appPackage'] = 'com.android.calculator'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723', desired_caps)