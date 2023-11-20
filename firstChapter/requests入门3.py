#针对在ajax中获取的数据
import requests

url=r'https://movie.douban.com/j/chart/top_list'

#重新封装参数

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}
param={
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20,
}

resp=requests.get(url=url,params=param,headers=headers)#被反扒，首选user-agent,get用params,post用data

print(resp.request.url)
print(resp.json())
resp.close()#关闭resp