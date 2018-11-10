import threading
sum = 0
loopSum = 1000000

def maAdd():
    global sum,loopSum
    for i in range(1,loopSum):
        sum += 1

def myMinu():
    global sum, loopSum
    for i in range(1,loopSum):
        sum -= 1
if __name__ == '__main__':
    print('Starting...{0}'.format(sum))
    #开始多线程的实例，看执行结果是否一样
    t1 = threading.Thread(target = maAdd,args=())
    t2 = threading.Thread(target = myMinu,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('Done...{0}'.format(sum))

    #因为多线程执行的原因， 所以最后的结果不为0