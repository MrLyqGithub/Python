# coding: utf-8

from selenium import webdriver
from time import sleep

# 打开浏览器
driver = webdriver.Chrome()

# 打开自学网
driver.get('http://www.51zxw.net')
print(driver.title)
sleep(2)

driver.get('https://www.baidu.com')
print(driver.title)
sleep(2)
driver.quit()