import time
import threading
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
    print('Starting at:',time.ctime())

    t1 = threading.Thread(target=loop1 ,args=('老大',))
    t1.start()

    t2 = threading.Thread(target=loop2, args=('老二','老三'))
    t2.start()

    print('All done at:',time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)