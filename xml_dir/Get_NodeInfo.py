#coding:utf-8
from xml.dom import minidom

#打开文件
dom = minidom.parse('student.xml')

#获取文档元素
root = dom.documentElement

# 获取元素节点
students = root.getElementsByTagName('student')

print(students[0].nodeName)
print(students[0].nodeType)
print(students[0].nodeValue)
