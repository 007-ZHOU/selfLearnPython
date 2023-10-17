import requests,re

url='https://dy2018.com'

headers={
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}

resp=requests.get(url=url,headers=headers,verify=False) #verify=False 去掉安全验证
resp.encoding='gb2312'

pattern1=r'2023必看热片.*?<ul>(?P<ul>.*?)</ul>'
obj1=re.compile(pattern=pattern1,flags=re.S)
result1=obj1.finditer(string=resp.text)#大概过滤结果
resp.close()

pattern2=r"<a href='(?P<href>.*?)'"+r'.*?title="(?P<title>.*?)"'+r".*?</li>"

childPattern=r'◎片　　名　(?P<name>.*?)<br />◎年　　代　(?P<year>.*?)<br />◎产　　地　(?P<location>.*?)<br />'\
   +r'◎类　　别　(?P<type>.*?)<br />◎语　　言　(?P<language>.*?)<br />◎字　　幕　(?P<captions>.*?)<br />'\
   +r'◎上映日期　(?P<date>.*?)<br />◎豆瓣评分　(?P<doubanScore>.*?) users<br />◎IMDb评分　(?P<ibdbScore>.*?)<br />'\
   +r'◎文件格式　(?P<format>.*?)<br />◎视频尺寸　(?P<size>.*?)<br />◎文件大小　(?P<big>.*?)<br />◎片　　长　(?P<time>.*?)<br />'\
   +r'◎导　　演　(?P<director>.*?)<br />'\
   +r'.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">'

obj2=re.compile(pattern=pattern2,flags=re.S)#再次过滤条件

childHrefList=[]

for i in result1:
   """
   进行仔细筛选
   """
   ul=i.group('ul')
   #提取子页面内容
   result2=obj2.finditer(string=ul)#
   for j in result2:
      """
      存放地址
      """
      dic=j.groupdict()#字典化
      dic['href']=url+dic['href']#转化为绝对地址
      childHrefList.append(dic['href'])
      

print(childHrefList)

childListDetailInfo=[]
for href in childHrefList:
   """
   进入电影链接，获取信息与下载地址
   """
   childResp=requests.get(url=href,headers=headers,verify=False)
   childResp.encoding='gb2312'
   

   # print(childResp.text)

   clildObj=re.compile(pattern=childPattern,flags=re.S)
   childResult=clildObj.finditer(string=childResp.text)
   childResp.close()#关闭，一定要注意，特别是在循环中
   for i in childResult:
      """遍历迭代器"""
      dic=i.groupdict()
      # print(dic)
      childListDetailInfo.append(dic)

print(childListDetailInfo)

import csv
with open(file='屠戮盗版天堂电影信息.csv',mode='w',newline='') as f:#newline去除空一行的现象
    csvWriter=csv.writer(f)
    csvWriter.writerow(['片名','年代','产地','类别','语言','字幕','上映时间',
                     '豆瓣评分','IMDb评分','文件格式','视频尺寸','文件大小','时长',
                     '导演','下载链接'])#添加列名
    for i in childListDetailInfo:#i是字典形式
       csvWriter.writerow(i.values()) 
