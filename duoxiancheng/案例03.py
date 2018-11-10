import time
import _thread as thread
def loop1(in1):
    print('start loop1 at',time.ctime())
    print('我是参数',in1)
    time.sleep(4)
    print('end loop1 at',time.ctime())

def loop2(in1,in2):
    print('start loop2 at',time.ctime())
    print('我是参数',in1,'和参数',in2)
    time.sleep(2)
    print('end loop2 at',time.ctime())
def main():
    print('starting at', time.ctime())
    #启动多线程的意思是用多线程去执行某个函数
    #启动多线程函数为start_new_thread
    #参数两个，一个是需要运行的函数名，第二个是函数的参数作为元组使用，为空则为空元组
    #注意：如果函数只有一个参数，需要参数后有一个逗号
    thread.start_new_thread(loop1,('lalal',))
    thread.start_new_thread(loop2,('asdas','asdasasd'))
    print('all done at', time.ctime())
if __name__ == '__main__':
    main()