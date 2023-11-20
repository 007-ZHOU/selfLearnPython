#线程任务的调度交给线程池来完成

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

#任务
def fn(name):
    for i in range(1000):
        print(name,i)


if __name__ == '__main__':
    #创建线程池 
    with  ThreadPoolExecutor(10) as t:#创建了一个有10个线程组成的线程池
        for i in range(300):#300个任务
            t.submit(fn,name=f'线程{i}')

