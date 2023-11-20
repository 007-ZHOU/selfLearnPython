"""
date:2023-10-19
author:zhou
代码简介：初学xpath语法
"""

from lxml import etree

xml=r'xPath解析入门2.html'

tree=etree.parse(source=xml)

html=tree.xpath('/html')
# print(html)

aText=tree.xpath('/html/body/ul/li[1]/a/text()')
# print(aText)# 百度  xpath默认是从1开始数



ahref=tree.xpath('/html/body/ol/li/a[@href="dapao"]/text()')# [@xxx=xxx]是对属性的筛选
# print(ahref)

olLiList=tree.xpath('/html/body/ol/li')
print(olLiList)
for li in olLiList:
    text=li.xpath('./a/text()')#在li中继续曲寻找，相对查找 也可以： text=li.xpath('a/text()')
    print(text)
    href=li.xpath('./a/@href')#获取a标签的属性值
    print(href)