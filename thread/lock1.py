# -*- coding: utf-8 -*-
"""
Created on Thu May  3 13:57:00 2018

@author: yefang

  示例
线程不安全:

最普通的一个多线程小例子。我一笔带过地讲一讲，我创建了一个继承Thread类的子类MyThread，
作为我们的线程启动类。按照规定，重写Thread的run方法，我们的线程启动起来后会自动调用该方法。
于是我首先创建了10个线程，并将其加入列表中。再使用一个for循环，开启每个线程。在使用一个for循环，
调用join方法等待所有线程结束才退出主线程。

这段代码看似简单，但实际上隐藏着一个很大的问题，只是在这里没有体现出来。
你真的以为我创建了10个线程，并按顺序调用了这10个线程，每个线程为n增加了1.
实际上，有可能是A线程执行了n++，再C线程执行了n++，再B线程执行n++。

这里涉及到一个“锁”的问题，如果有多个线程同时操作一个对象，如果没有很好地保护该对象，
会造成程序结果的不可预期（比如我们在每个线程的run方法中加入一个time.sleep(1)，
并同时输出线程名称，则我们会发现，输出会乱七八糟。因为可能我们的一个print语句只打印出一半的字符，
这个线程就被暂停，执行另一个去了，所以我们看到的结果很乱），这种现象叫做“线程不安全”

"""

import  threading   
import  time   
      
counter = 0 
counter_lock = threading.Lock() #只是定义一个锁,并不是给资源加锁,你可以定义多个锁,像下两行代码,当你需要占用这个资源时，任何一个锁都可以锁这个资源 
counter_lock2 = threading.Lock()  
counter_lock3 = threading.Lock() 
   
#可以使用上边三个锁的任何一个来锁定资源 
    
class  MyThread(threading.Thread):#使用类定义thread，继承threading.Thread 
     def  __init__(self,name):   
        threading.Thread.__init__(self)   
        self.name = "Thread-" + str(name) 
     def run(self):   #run函数必须实现 
         global counter,counter_lock #多线程是共享资源的，使用全局变量 
         time.sleep(1);   
         if counter_lock.acquire(): #当需要独占counter资源时，必须先锁定，这个锁可以是任意的一个锁，可以使用上边定义的3个锁中的任意一个 
            counter += 1    
            print ("I am %s, set counter:%s"  % (self.name,counter)   )
            counter_lock.release() #使用完counter资源必须要将这个锁打开，让其他线程使用 
               
if  __name__ ==  "__main__":   
    for i in range(1,101):   
        my_thread = MyThread(i) 
        my_thread.start()