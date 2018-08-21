# coding: utf-8

from xml.dom import minidom

# 打开xml文件
dom = minidom.parse('student.xml')

# 获取文档元素
root = dom.documentElement

# 获取文本节点
names = root.getElementsByTagName('name')
ages = root.getElementsByTagName('age')
citys = root.getElementsByTagName('city')

# 打印
for i in range(4):
    # names类似列表，firstChild.data是标签对的数据
    print(names[i].firstChild.data)
    print(ages[i].firstChild.data)
    print(citys[i].firstChild.data)
