import multiprocessing
from time import ctime

def consumer(input_q):
    print('Into consumer:',ctime())
    while True:
        #处理项
        item = input_q.get()
        print('pull',item,'out of q')#此处替换为有用的工作
        input_q.task_done()# 发送信号通知任务完成
    print('Out of consumer',ctime())

def producter(sequence,output_q):
    print('Into producter',ctime())
    for item in sequence:
        output_q.put(item)
        print('put',item,'into q')
    print('Out of producter:',ctime())

#建立进程
if __name__=='__main__':
    q = multiprocessing.JoinableQueue()
    #运行消费者进程
    cons_p = multiprocessing.Process(target=consumer,args=(q,))
    cons_p.start()
    #生产多个项，sequence代表要发送给消费者的项序列
    #在实践中，这可能是生成器的输出或者通过一些其他方式生产出来
    sequence = [1,2,3,4]
    producter(sequence,q)
    q.join()