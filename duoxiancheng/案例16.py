import threading
import time

semaphore = threading.semaphore(3)

def func():
    if semaphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName()+ 'get semaphore')
        time.sleep(15)
        semaphore.reless()
        print(threading.currentThread().getName()+' release semaphore')

for i in range(8):
    t1 = threading.Thread(target=func())
    t1.start()
    t1.join()

if __name__=="__main__":
    func()
