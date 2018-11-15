from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:',__name__)
    #ppid ：父类进程的id
    print('parent process',os.getppid())
    #pid ： 子类进程的id
    print('process id',os.getpid())

def f(name):
    info('function f')

    print('hello',name)

if __name__=='__main__':
    info('main line')
    p = Process(target=f, args=('bbb',))
    p.start()
    p.join()