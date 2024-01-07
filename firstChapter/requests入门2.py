import requests,jieba
url='https://fanyi.baidu.com/sug'#Request URL:   https://fanyi.baidu.com/sug

s=input("请输入您要翻译的英文")
segList=jieba.cut(s)
arr=[]
for i in segList:

    formData={
        "kw":i
    }
    #发生post请求
    resp=requests.post(url=url,data=formData)
    print(resp)
    # print(resp.json())#将服务器返回的内容直接处理成json()=>dict
    a=resp.json()['data'][0]['v']
    print(a)
    print(list(jieba.cut(a)))
    first=list(jieba.cut(a))[0]
    arr.append(first)
arr1=' '.join(arr)
print(arr1)