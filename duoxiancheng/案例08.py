import time
import threading

def loop1():
    print('start loop1 at',time.ctime())
    time.sleep(8)
    print('end loop1 at',time.ctime())

def loop2():
    print('start loop2 at', time.ctime())
    time.sleep(2)
    print('end loop2 at', time.ctime())

def loop3():
    print('start loop3 at', time.ctime())
    time.sleep(9)
    print('end loop3 at', time.ctime())

def main():
    print('starting at',time.ctime())
    loop1()
    loop2()
    print('all done at',time.ctime())

def main():
    print('Starting at:',time.ctime())
    #生成threading.Thread实例
    t1 = threading.Thread(target=loop1,args=( ))
    # setName是给每一个子线程一个名字
    t1.setName('THR_1')
    t1.start()

    t2 = threading.Thread(target=loop2, args=( ))
    # setName是给每一个子线程一个名字
    t2.setName('THR_2')
    t2.start()

    t3 = threading.Thread(target=loop3, args=( ))
    # setName是给每一个子线程一个名字
    t3.setName('THR_3')
    t3.start()

    #预期3秒后，Thread2已经结束
    time.sleep(5)
    #enumerate 得到正在运行子程序，即子线程1和子线程3
    for thr in threading.enumerate():
        print('正在运行的线程名字是: {0}'.format(thr.getName()))

    print('正在运行的子线程的数量:{0}'.format(threading.activeCount()))
    print('All done at',time.ctime())
if __name__ == '__main__':
    main()