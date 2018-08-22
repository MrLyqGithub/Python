# coding: utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 汉字转码
def zn(str):
    return str.decode('utf-8')


# 自动测试过程
def open(url):

    driver.get(url)
    
    driver.find_element_by_id('kw').send_keys(zn("我要自学网"))
    
    driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
    driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'c')
    
    driver.find_element_by_id('su').click()
    
    driver.get('http://www.51zxw.com')

    driver.find_element_by_id('frm_login_url').click()
    
    driver.find_element_by_id('loginStr').send_keys(zn("abc1234test"))
    
    driver.find_element_by_id('pwd').send_keys(zn("liuyuquan.."))
    
    driver.find_element_by_xpath('//*[@id="loginFrom"]/div/div[5]/button').click()
    
    sleep(2)
    
    element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.NAME,'sgo')))
    element.send_keys(Keys.CONTROL,'v')
    #driver.find_element_by_name('sgo').send_keys(Keys.CONTROL,'v')
    
    print ("登陆成功")

# 主入口
if __name__ == '__main__':
    open('https://www.baidu.com')
    