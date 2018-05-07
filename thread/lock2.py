# -*- coding: utf-8 -*-
"""
Created on Thu May  3 17:00:37 2018

@author: yefang
"""

import threading, time

from functools import wraps


def fn_timer(function):
    #@wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("运行时间 %s: %s 秒" %
               (function.__name__, str(t1-t0))
               )
        return result
    return function_timer
class StandardOut(object):   
   """  
   线程锁装饰器 
   """   
   def __init__(self): 
       threading.Thread.__init__(self)
       self.thread_lock = threading.Lock()  
      
   def __call__(self,func):  
       def _call(*args,**kw):   
           self.thread_lock.acquire()  
           func(*args,**kw)  
           self.thread_lock.release()  
       return _call  

@StandardOut
class MyThread(threading.Thread):
    # def __init__(self):
        # threading.Thread.__init__(self)
    def run(self):
        global n, lock
        time.sleep(1)
        if lock.acquire():
            print (n , self.name)
            n += 1
            lock.release()
if "__main__" == __name__:
    n = 1
    ThreadList = []
    lock = threading.Lock()
    for i in range(1, 20):
        t = MyThread()
        ThreadList.append(t)
    for t in ThreadList:
        t.start()
    for t in ThreadList:
        t.join()