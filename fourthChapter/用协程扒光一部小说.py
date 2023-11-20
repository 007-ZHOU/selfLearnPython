"""
date:2023-10-230
author:zhou
代码简介：百度小说中的西游记小说“https://dushu.baidu.com/pc/detail?gid=4306063500”
分析：1、找到小说数据是异步加载的，定位到request的url为“
https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}”,得到章节名


url'https://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500|1569782244%22,%22need_bookinfo%22:1}'点击章节，获取到的小说内容

2、同步操作：访问getCatalog 拿到所有章节的cid和名称
    异步操作：访问getChapterContent  下载所有的文章内容

3、get？ params？ cookie？ refer？ user-agent？
"""


import requests ,asyncio,aiohttp,aiofiles,json

async def download(b_id,title,cid):
    data= {
        "book_id":b_id,
        "cid":f"{b_id}|{cid}",
        "need_bookinfo":1
        }
    
    data=json.dumps(data)#转化为json对象
    url=f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic=await resp.json()#请求用await
            # print(dic)
            content=dic['data']['novel']['content']
            # print(content)

            async with aiofiles.open(file=f'./fourthChapter/用协程扒光一部小说/{title}.txt',mode='w',encoding='utf-8') as f:
               await f.write(content)#把小说内容写入,io用await

 
async def getCatalog(b_id,url):

    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76",
    }
    resp=requests.get(url=url,headers=headers)
    dic=resp.json()
    tasks=[]
    for item in dic['data']['novel']['items']:
        title=item['title']
        cid=item['cid']
        print(title,cid)
        #准备异步任务
        down= asyncio.create_task(download(b_id=b_id,title=title,cid=cid))
        tasks.append(down)

    await asyncio.wait(tasks)


if __name__=='__main__':
    b_id='4306063500'
    url=r'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+b_id+'"}'#%22就是双引号
    asyncio.run(getCatalog(b_id=b_id,url=url))