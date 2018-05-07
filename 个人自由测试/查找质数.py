# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 09:30:32 2018

@author: yefang
"""

s = int(input("请输入要计算多少位的素数："))
b = [2]   # 素数表
for num_s in range(2,s+1):
    a = 0
    for num_b in b:
        if num_s % num_b == 0:
            a = 1
            break
    if a == 0:
        b.append(num_s)
        
print("%d以内的素数共有：\n" % s)
print(b)
        

    
         