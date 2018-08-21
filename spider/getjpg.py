import urllib
import re
import os


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 68
    path = 'D:\\test' 
    
    if not os.path.isdir(path):
        os.makedirs(path)
        
    paths = path + "\\"
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '{}{}.jpg'.format(paths, x))
        x = x + 1
        
    return imglist

html = getHtml("https://tieba.baidu.com/p/2460150866?pn=2") 
print (getImg(html)) 
