#request.get() 同步的代码——》异步操作aiohttp


import asyncio
import aiohttp


async def download(url):
    name=url.rsplit('/')[-1]
    #aiohttp.ClientSession()==requests().session() 完全相等
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with  open(file=f'./fourthChapter/aiohttp模块应用/{name}',mode='wb') as f:
                f.write(await resp.content.read())
    pass

async def main():
    urls=[
        'https://www.umei.cc/d/file/20230901/85dce71c53e061c61df127651e6462b0.jpg',
        'https://www.umei.cc/d/file/20230901/3922c4fb1536b09bd7f6f251b6f94259.jpg',
        'https://www.umei.cc/d/file/20230901/402538d4b0e8512e8636c88b1e66035a.jpg',
    ]

    tasks=[]#任务

    for url in urls:
        down= asyncio.create_task(download(url))
        tasks.append(down)

    await asyncio.wait(tasks)#启动运行


if __name__ == '__main__':
    asyncio.run(main())
