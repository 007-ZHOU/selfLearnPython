"""
date:2023-11-07
author:zhou
代码简介：古诗文网（https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx）验证码识别
分析：1、下载验证码图片到本地
    2、验证码识别
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


def main():
    url='https://so.gushiwen.cn/user/login.aspx'
    print(123)
    headers={
    'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    resp=requests.get(url=url,headers=headers)
    tree =etree.HTML(text=resp.text)
    img=tree.xpath('/html//img[@id="imgCode"]')
    src=img[0].get('src')
    imgUrl=url.split('/user')[0]+src
    print(imgUrl)

    resp=requests.get(url=imgUrl,headers=headers)
    with open(file='./fifthChapter/验证码.jpg',mode='wb') as f:
        f.write(resp.content)

    #调用云码平台识别
    code=getTextCode(image='./fifthChapter/验证码.jpg',verify_type='10110')
    print('识别结果：',code)


if __name__=='__main__':
    main()