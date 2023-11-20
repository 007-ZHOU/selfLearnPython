from multiprocessing import Process

def func(name):
    for i in range(100):
        print(name,i)


if __name__=='__main__':
    p=Process(target=func,args=('周杰伦',))#传参
    p.start()
    for i in range(100):
        print('主进程',i)