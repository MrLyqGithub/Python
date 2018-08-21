# coding: utf-8
from time import ctime, sleep
import multiprocessing

# 定义讲方法
def talk(content, loop):
    for i in range(loop):
        print("Talk: %s -----%s" %(content, ctime()))
        sleep(2)
        
# 定义写方法
def write(content, loop):
    for i in range(loop):
        print("Write: %s -----%s" %(content, ctime()))
        sleep(3)
        
# 定义线程集合
threads = []

# 定义线程
t1 = multiprocessing.Process(target=talk, args=('Start talk!', 2))
t2 = multiprocessing.Process(target=write, args=('Start write!', 2))

threads.append(t1)
threads.append(t2)

# 执行方法
if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    print("All end! -----%s" %ctime())