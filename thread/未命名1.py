# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:44:04 2018

@author: yefang
"""

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：%s \n" % self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
print('创建新线程')
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
print('开启新线程1')
thread1.start()

print('开启新线程2')
thread2.start()

print('等待线程1结束')
thread1.join()

print('等待线程2结束')
thread2.join()

print ("退出主线程")
