#拿到页面源代码

import requests

url=r'https://movie.douban.com/top250'

headers={
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}

resp=requests.get(url=url,headers=headers)
pageContent=resp.text
# print(pageContent)
#通过re来提取想要的信息

import re

pattern=r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'\
+r'.*?<div class="bd">.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;/&nbsp;'\
+r'.*?<div class="star">.*?<span class="rating_num" property="v:average">(?P<rate>.*?)</span>'\
+r'.*?<span property="v:best" content="10.0"></span>.*?<span>(?P<number>.*?)人评价</span>'#(?P<name>.*?)赋值给name

obj=re.compile(pattern=pattern,flags=re.S)
#开始匹配
result= obj.finditer(string=pageContent)

# for i in result:
#     print(i.group("name"))
#     print(i.group("year").strip())#默认删除字符串开头和结尾的空格
    
#     print(i.group("rate"))
#     print(i.group("number"))

#     print('------')

#存入scv文件
import csv
with open(file='手刃豆瓣TOP250.csv',mode='w') as f:
    csvWriter=csv.writer(f)

    for i in result:
        dic=i.groupdict()
        dic['year']=dic['year'].strip()
        print(dic)
        csvWriter.writerow(dic.values())

print('over')