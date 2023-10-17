import requests
url='https://fanyi.baidu.com/sug'

s=input("请输入您要翻译的英文")
formData={
    "kw":s
}

#发生post请求

resp=requests.post(url=url,data=formData)
print(resp)
print(resp.json())#将服务器返回的内容直接处理成json()=>dict
