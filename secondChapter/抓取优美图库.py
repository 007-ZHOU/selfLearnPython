"""
date:2023-10-18
author:zhou
代码简介：在url地址中，有优美壁纸列表，需要进入每个文章中获取它的高清大图（原图）
分析：1、服务器渲染数据，网页源代码中直接有数据，进入文章的链接在标签中都有。2、get请求
"""


import requests,re,bs4
from bs4 import BeautifulSoup

url='https://www.umei.cc/gaoxiaotupian/baoxiaotupian'
urlWeb='https://www.umei.cc'
headers={
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}

#1、获取页面内容
resp=requests.get(url=url,headers=headers)
resp.encoding='UTF-8'#转码
soup=BeautifulSoup(markup=resp.text,features='html.parser')
resp.close()
#2、获取全部文章链接与名字
itemMasnry=soup.find_all("div",attrs={'class':'item masonry_brick'})#获取全部‘文章链接与名字’所处的div
#aList=soup.find('div',class_='item_list infinite_scroll').find_all("a")
# 接上：另外一种方法，在所有item masonry_brick的上一级找它下一级有所有的a，1找m不用for，n找m用for
hrefList=[]
for i in  itemMasnry:
    tag=i.find("div",attrs={'class':'item_b clearfix'})
    text=tag.a.get_text()
    href=tag.a.attrs['href']
    hrefList.append(urlWeb+href)

# print(hrefList)

#3、进入文章链接
imgSrcList=[]
for href in hrefList:
#4、获取图片链接并下载
    resp=requests.get(url=href,headers=headers)
    resp.encoding='UTF-8'
    # print(resp.text)
    soup=BeautifulSoup(markup=resp.text,features='html.parser')
    resp.close()
    tag=soup.find("div",attrs={'class':'big-pic'})
    # print(tag)
    src=tag.img.attrs['src']
    # print(src)
    imgSrcList.append(src)

#5下载图片
for imgSrc in imgSrcList:
    imgResp=requests.get(url=imgSrc,headers=headers)
    imgName=imgSrc.split('/')[-1]
    print(imgSrc)
    with open (file='./优美图库/'+imgName,mode='wb') as f:
        f.write(imgResp.content )#字节的形式写入
    
    f.close()
    imgResp.close()
