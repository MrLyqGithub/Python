# coding: utf-8
import urllib
import re

# 获取html
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

# 获取图片
def getImage(html):
    reg = r'http://[\S]*jpg'
    pattern = re.compile(reg)
    image_list = re.findall(pattern, repr(html))
    print image_list
    
    num = 1
    for img in image_list:
        image = getHtml(img)
        with open('D:\\test\\%s.jpg' %num, 'wb') as fb:
            fb.write(image)
            print("正在下载第%s张图片" %num)
            num = num + 1
    print("下载完成")
    
url = 'http://p.weather.com.cn'
html = getHtml(url)
getImage(html)