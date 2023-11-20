
# 常见阻塞状态
# 1、requests.get(url),在网络请求返回数据之前，程序也是处于阻塞状态的
# 2、一般情况下，当出现处于IO操作的时候，线程都会处于阻塞状态
# 3、input()


# 协程：当程序遇到IO操作的时候，可以选择性的切换到其他任务
# 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
# 在宏观上，我们能看到的其实是多个任务的一起在执行
# 多任务异步操作

""""
import asyncio
import time


async def func1():
    print('你好，我叫赛利亚1')
    # time.sleep(2)#当程序出现同步操作的时候，异步就中断了
    await asyncio.sleep(3)  # 异步操作的代码
    print('你好，我叫赛利亚2')


async def func2():
    print('你好，我叫潘金莲1')

    print('你好，我叫潘金莲2')


async def func3():
    print('你好，我叫武松1')

    print('你好，我叫武松2')


async def main():
    # 第一种写法
    # f1 =func1()
    # await f1 #一般await挂起操作放在协程对象前面

    # 第二种写法（推荐）

    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())


"""

#爬虫当中的使用模板
import asyncio
async def download(url):
    print('准备开始下载')
    await asyncio.sleep(2)#网络请求 requsets.get()
    print('下载完成')

async def main():
    urls=[
        'http://www.baidu.com',
        'http://www.jd.com',
        'http://www.taobao.com',
    ]

    tasks=[]#任务

    for url in urls:
        down= asyncio.create_task(download(url))
        tasks.append(down)

    await asyncio.wait(tasks)#启动运行


if __name__ == '__main__':
    asyncio.run(main())
