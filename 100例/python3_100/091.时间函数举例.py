# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:27:29 2018

@author: yefang

题目：时间函数举例1。
"""

if __name__ == '__main__':
    import time
    print (time.ctime(time.time()))
    print (time.asctime(time.localtime(time.time())))
    print (time.asctime(time.gmtime(time.time())))