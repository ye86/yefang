# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:49:44 2018

@author: yefang
"""



import time
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


@fn_timer
def myfunction(n):
    a = 0
    for i in range(n):
        a += i
    return a

int1 = myfunction(1000000)
print(int1)
print(myfunction.__name__)