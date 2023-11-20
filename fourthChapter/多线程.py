# 线程，进程
#进程是资源单位，每一个进程至少要有一个线程
#线程是执行单位

#单线程
def func():
    for  i in range(100):
        print('func',i)



if __name__ == '__main__':
    func()
    for i in range(100):
        print("main",i)


# #多线程函数式
# from threading import Thread
# def func():
#     for  i in range(100):
#         print('func',i)



# if __name__ == '__main__':
#     t=Thread(target=func)
#     t.start()#多线程状态为可以开始工作状态，具体的执行时间由cpu决定

#     for i in range(100):
#         print("main",i)

#多线程class

from threading import Thread

class myThread(Thread):
    def run(self):#固定的
        for  i in range(100):
            print('子线程',i)




if __name__ == '__main__':
    t=myThread()
    # t.run()#方法的调用了，不能这么写
    t.start()

    for i in range(100):
        print("main",i)