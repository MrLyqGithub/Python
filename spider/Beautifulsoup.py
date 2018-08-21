# -*- coding: utf-8 -*-

from flask import Flask, request
from bs4 import BeautifulSoup
import urllib

app = Flask(__name__)

# 网页下载
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html.decode('utf-8')

# 网页解析
def analysis(html):
    soup = BeautifulSoup(html)
    print soup.select('.toplist__songname')
    print soup.find('a')
    
html=getHtml("https://y.qq.com/")
analysis(html)

