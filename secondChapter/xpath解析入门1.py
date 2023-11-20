"""
date:2023-10-19
author:zhou
代码简介：初学xpath语法
"""

from lxml import etree


xml = """
<html>
    <head>
        <meta charset="utf-8"/>
        <title>菜鸟教程(runoob.com)</title>
    </head>
    <body>
        <h1>我的第一个标题<a/></h1>
        <p>我的第一个段落。</p>
        <p class='second'>我的第二个段落。</p>
        <div>
            <p>我的第三个段落</p>
        </div>
        <div>
            <p>我的第四个段落</p>
        </div>
    </body>
</html>
"""

tree = etree.XML(xml)
# result=tree.xpath("/html")#表示层级关系，第一个“/”是根节点
result1=tree.xpath('/html/head')
result2=tree.xpath('/html//title')
result3=tree.xpath('/html//title/text()')#text()拿文本
result4=tree.xpath('/html//a')
result5=tree.xpath('/html//p/text()')
result6=tree.xpath('/html/body/*/p/text()')#*任意的节点
print(result1)#注意<meta>标签后加“/”#[<Element head at 0x23adb6e1440>]
print(result2)#[<Element title at 0x23adb6e1600>]
print(result3)#['菜鸟教程(runoob.com)']
print(result4)#[<Element a at 0x23adb6e17c0>]
print(result5)#['我的第一个段落。', '我的第二个段落。', '我的第三个段落', '我的第四个段落']
print(result6)#['我的第三个段落', '我的第四个段落']
