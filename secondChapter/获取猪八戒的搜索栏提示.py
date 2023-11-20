import requests

url='https://alg.api.zbj.com/search/suggest'


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
}


param={
    '_t': 1697871278439,
'jsonpcallback': 'jQuery370038945989652933166_1697871154887',
'type': 1,
'size': 7,
'kw': 'vue',
'_': 1697871154907,
}
resp=requests.get(url=url,params=param,headers=headers)
print(resp.text)