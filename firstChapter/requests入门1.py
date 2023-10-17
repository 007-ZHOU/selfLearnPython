import requests

url=r'https://www.sogou.com/web?query=周杰伦'
reHeaders={

    'User-Agent':r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46"
}

resp=requests.get(url=url,headers=reHeaders)
print(resp.text)#拿到页面源代码