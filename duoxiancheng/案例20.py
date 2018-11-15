import multiprocessing
from time import ctime,sleep

class ClockProcess(multiprocessing.Process):
    '''
    两个函数比较重要
    1.init函数
    2.run
    '''
    def __init__(self,interval):
        super().__init__()
        #super():调用父类的一个方法
        self.interval = interval

    def run(self):
        while True:
            print('Thr time is %s'% ctime())
            sleep(self.interval)

if __name__=='__main__':
    p = ClockProcess(3)
    p.start()