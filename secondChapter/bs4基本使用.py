import requests
from bs4 import BeautifulSoup
url = 'http://www.xinfadi.com.cn/priceDetail.html'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
}

data = {
    'limit': '',
    'current': '',
    'pubDateStartTime': '',
    'pubDateEndTime': '',
    'prodPcatid': '',
    'prodCatid': '',
    'prodName': '',
}

resp = requests.post(url=url, headers=headers, data=data)
print(resp.text)
