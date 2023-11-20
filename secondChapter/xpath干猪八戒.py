"""
date:2023-10-21
author:zhou
代码简介：爬取“猪八戒网”上的数据
"""

import requests
from lxml import etree

url='https://www.zbj.com/fw/?k=saas'


headers={
   'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}


resp=requests.get(url=url,headers=headers)
tree =etree.HTML(text=resp.text)
print(tree)
text1=tree.xpath('/html/body/div[2]/div/div/div[3]/div/div[4]/div/div[2]/div[1]/div[1]/div/div[3]/div[2]/a/text()')
text2=tree.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div[2]/div/div[3]/div[2]/a')
print(text1)
print(text2)