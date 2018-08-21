# coding: utf-8
from time import ctime, sleep

# 定义讲
def talk():
    print("Talk! %r" %ctime())
    sleep(2)
def write():
    print("Write! %r" %ctime())
    sleep(3)
    
if __name__ == '__main__':
    talk()
    write()
    print("All end! %r" %ctime())