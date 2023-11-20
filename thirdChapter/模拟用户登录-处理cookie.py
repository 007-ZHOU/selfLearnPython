"""
date:2023-10-23
author:zhou
代码简介：模拟用户登录“17k小说网”,并获取我的书架内容。
"""
#1、登录2、获取信息
#我们必须得把上面的两个操作连起来
#可以使用session进行请求-> session 你可以认为是一连串得请求，在这个过程中的cookie不会丢失

import requests

#1、会话，获取cookies拿取个人通行证
session=requests.session()
url='https://passport.17k.com/ck/user/login'
data={
    'loginName': '19857181251',
    'password': 'aqz145',
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
}

#thirdChapter\重要部分截图\模拟用户登录-处理cookie_1.JPG
#thirdChapter\重要部分截图\模拟用户登录-处理cookie_2.JPG
#thirdChapter\重要部分截图\模拟用户登录-处理cookie_3.JPG
#thirdChapter\重要部分截图\模拟用户登录-处理cookie_4.JPG
resp=session.post(url=url,data=data,headers=headers)
# print(resp.cookies)

#2、拿取数据
#secondChapter\重要部分截图\模拟用户登录-处理cookie_5.JPG
urlData=r'https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919' 

respData=session.get(url=urlData)
print(respData.json())
respData.close()