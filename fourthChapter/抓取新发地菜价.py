"""
date:2023-10-25
author:zhou
代码简介：抓取北京新发地前num页的菜价。
分析：1、url='http://www.xinfadi.com.cn/priceDetail.html'
2、都是ajax请求，每一个页面的请求url和方法post都一样。唯一不一样的就是payload
"""

import requests,csv
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def downloadPage(url,headers,data,csvWriter):
    resp=requests.post(url=url,data=data,headers=headers)
    # print(resp.json()['list'])
    vegeList=resp.json()['list']
    resp.close()

    for vege in vegeList:#i是字典形式
        #数据清洗
        vege=dict(filter(lambda item :item[1] ,vege.items()))
        del vege['id'],vege['prodCatid'],vege['pubDate'],vege['userIdCreate'],vege['userCreate']
        print(vege)
        csvWriter.writerow(vege.values()) 


if __name__ == '__main__':

    url='http://www.xinfadi.com.cn/getPriceData.html'

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
        'Referer':'http://www.xinfadi.com.cn/priceDetail.html',
    }
    data={
    'limit': 20,
    'current': 1,
    }   
    num=int(input('请输入您要获取前几页数据:'))
    f=open(file='./fourthChapter/抓取新发地菜价.csv',mode='w',newline='')#先把文件打开，不要在线程中一直开关
    csvWriter=csv.writer(f)
    with ThreadPoolExecutor(50) as t:#线程池有50个线程
        for i in range(num | 50):#预设采集50页
            data['current']=data['current']+1
            t.submit(downloadPage,url=url,headers=headers,data=data,csvWriter=csvWriter)
    f.close()
    print('页全部下载完毕！')

