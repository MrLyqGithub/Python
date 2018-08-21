# coding: utf-8
from selenium import webdriver
from time import sleep

def zn(str):
    return str.decode('utf-8')

def find_Element_by(by, tag, content, driver):
    if by == 'id':
        driver.find_element_by_id(tag).send_keys(content)
    elif by == 'class_name':
        driver.find_element_by_class_name(tag).send_keys(content)
    elif by == 'tag_name':
        driver.find_element_by_tag_name(tag).send_keys(content)
    elif by == 'xpath':
        driver.find_element_by_xpath(tag).send_keys(content)
    elif by == 'link_text':
        driver.find_element_by_link_text(tag).click()
    elif by == 'partial_link_text':
        driver.find_element_by_partial_link_text(tag).click()
    
def webdriver_open(driver, url, str):
    driver.get(url)
    find_Element_by('id','kw',str,driver)
    sleep(2)
    find_Element_by('link_text','百度首页','',driver)
    sleep(1)
    find_Element_by('link_text', '新闻', '', driver)
    sleep(1)
    find_Element_by('partial_link_text', '文化工作述评', '', driver)
    
if __name__ == '__main__':
    str = zn("我要自学网")
    webdriver_open(webdriver.Firefox(),'https://www.baidu.com', str)
