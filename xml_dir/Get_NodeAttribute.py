# coding: utf-8

from xml.dom import minidom

# 打开文件
dom = minidom.parse('student.xml')

# 获取文档元素
root = dom.documentElement

# 获取属性节点
logins = root.getElementsByTagName('login')

# 循环打印
for i in range(2):
    print(logins[i].getAttribute('username'))
    print(logins[i].getAttribute('password'))