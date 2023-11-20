"""
date:2023-10-23
author:zhou
代码简介：抓取网易云音乐（‘https://music.163.com/#/song?id=1325905146’）热评。
分析：
1、刷新，在异步请求中的‘get?csrf_token=’找到了评论响应。
2、分析headers和payload：token加密，post请求，Referer。
    token加密：
            1.找到未加密的参数、
            2.想办法把参数进行加密（必须参考网易云的逻辑）,params=>window.asrsea(,,,).params  //  encSecKey =>window.asrsea(,,,).encSecKey
            3.请求到网易，拿到评论
3、

#分析处理加密过程

 function a(a) {  #返回随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,#随机数
            e = Math.floor(e),#取整
            c += b.charAt(e);#取字符串中的第e位置
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        
        #逗号表达式，取最后一个表达式的值
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),#返回的就是params
        h.encSecKey = c(i, e, f),#得到的就是encSecKey,e和f是定死的，如果此时我把i固定
        h
    }


window.asrsea(JSON.stringify(i2x), bvh3x(["流泪", "强"]), bvh3x(Re6Y.md), bvh3x(["爱心", "女孩", "惊恐", "大笑"]));

#运行控制台获取数据
d=JSON.stringify(i2x)=={
    "rid": "R_SO_4_1325905146",
    "threadId": "R_SO_4_1325905146",
    "pageNo": "1",
    "pageSize": "20",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "csrf_token": ""
}
e=bvh3x(["流泪", "强"])=='010001'
f=bvh3x(Re6Y.md)=='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g=bvh3x(["爱心", "女孩", "惊恐", "大笑"])=='0CoJUm6Qyw8W8jud'


"""

import requests
from  Crypto.Cipher import AES

url='https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

#post请求
data={
    "rid": "R_SO_4_1325905146",
    "threadId": "R_SO_4_1325905146",
    "pageNo": "1",
    "pageSize": "20",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "csrf_token": ""
}


requests.post(url=url,data=data)



