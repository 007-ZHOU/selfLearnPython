"""
date:2023-11-08
author:zhou
代码简介：古诗文网（https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx）模拟登录
分析：1、下载验证码图片到本地
    2、验证码识别
    3、把账号和密码发送
    4、总结，这方法不行，因为向url发送了两次请求，一次是获取验证码图片和code，第二次是把账号、密码和验证码code发送；两次的验证码不同。
    可以用selenium对页面进行截屏，然后对图片中的验证码进行解析，再次填入验证码，发送了一次请求。
"""

import requests
from lxml import etree

import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../")))
from lib.yunMa import YdmVerify

def getTextCode(image,verify_type):
    y = YdmVerify()
    result=y.common_verify(image=image,verify_type=verify_type)
    return result


def identify(url,headers):
    resp=requests.get(url=url,headers=headers)
    tree =etree.HTML(text=resp.text)
    img=tree.xpath('/html//img[@id="imgCode"]')
    src=img[0].get('src')
    imgUrl=url.split('/user')[0]+src

    resp=requests.get(url=imgUrl,headers=headers)
    with open(file='./fifthChapter/验证码.jpg',mode='wb') as f:
        f.write(resp.content)

    #调用云码平台识别
    code=getTextCode(image='./fifthChapter/验证码.jpg',verify_type='10110')
    print('识别结果：',code)
    return code 

def login():
    url='https://so.gushiwen.cn/user/login.aspx'
    urlLogin=r'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    headers={
    'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }
    code=identify(url=url,headers=headers)
    data={
        '__VIEWSTATE': 'n06AUfuVCBdUf5aLvGkSfSn8rgUA29dmHQpnWlFMmiqBE8y/sDnI1JbXNKHbTegCoASEzmE4NRPuVro+KSzhr2egOo8gewc/kIyuiA9Br9i+rqi2DEm3aPuvdtavESk7PN0yF81natPp6CLoElxN70/KAKY=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': '',
        'email': '2672929618@qq.com',
        'pwd': 'qwe145...',
        'code': code,
        'denglu': '登录',
    }

    session=requests.session()
    resp=session.post(url=urlLogin,data=data,headers=headers)
    print('=========================================')
    print(resp.status_code)
    print(resp.cookies)
    print(resp.text)

if __name__=='__main__':
    login()