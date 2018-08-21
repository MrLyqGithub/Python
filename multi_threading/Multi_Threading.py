# coding: utf-8
from time import ctime, sleep
import threading

# 定义读函数
def talk(content, loop):
    for i in range(loop):
        print("Start talk: %s %s" %(content, ctime()))
        sleep(2)
    
# 定义写函数
def write(content, loop):
    for i in range(loop):
        print("Start write: %s %s" %(content, ctime()))
        sleep(3)
    
# 定义一个线程集合
threads = []

t1 = threading.Thread(target=talk, args=('talking Im LYQ!', 2))
t2 = threading.Thread(target=write, args=('writing Im LYQ!', 2))

threads.append(t1)
threads.append(t2)

# 执行多线程
if __name__ == '__main__':
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()
        
    print("All end! %s" %ctime())