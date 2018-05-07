# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 13:41:10 2018

@author: yefang
"""

import math,time,os

#N = int(input("请输入要分解的数"))
N = 16851629
timestar=time.time()

宽=int(math.sqrt(N))
长,余 = divmod(N,宽)
if 余 == 0:
    timeover=time.time()
    print("两个最大因子为：%d,%d" % (宽,长))
    time1=timeover-timestar
    print("用时：%d" % time1 )
    os._exit()

class 两倍:
    def __init__(self,a=0):
        self.a=a
    def read(self):
        while true:
            self.a -= 1
            yield self.a
            self.a += 1
            yield self.a
class 三倍:
    def __init__(self,b=0):
        self.b=b
    def read(self):
        while true:
            self.b -= 1
            yield self.b
            self.b -= 1
            yield self.b
            self.b += 2
            yield self.b
class 五倍:
    def __init__(self,c=0):
        self.c=c
    def read(self):
        while true:
            self.c -= 1
            yield self.c
            self.c -= 1
            yield self.c
            self.c -= 1
            yield self.c
            self.c -= 1
            yield self.c
            self.c += 4
            yield self.c
class 七倍:
    def __init__(self,d=0):
        self.d=d
    def read(self):
        while true:
            self.d -= 1
            yield self.d
            self.d -= 1
            yield self.d
            self.d -= 1
            yield self.d
            self.d -= 1
            yield self.d
            self.d -= 1
            yield self.d
            self.d -= 1
            yield self.d
            self.d += 6
            yield self.d

a2 = 宽 % 2
a3 = 宽 % 3
a5 = 宽 % 5
a7 = 宽 % 7

b2 = 两倍(a2)
b3 = 三倍(a3)
b5 = 五倍(a5)
b7 = 七倍(a7)


for each in range(宽):
    宽 -= 1
    if b2.read or b3.read or b5.read or b7.read:
        if N % 宽 == 0:
            长 = N / 宽
            timeover=time.time()
            print("两个最大因子为：%d,%d" % (宽,长))
            time1=timeover-timestar
            print("用时：%d" % time1 )
            break
else:
    timeover=time.time()
    time1=timeover-timestar
    print("没有找到因子，您输入的%d是个质数！" % N )
    print("用时：%d" % time1 )

            
            
        
        
    
    



    
    