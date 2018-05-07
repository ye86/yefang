# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:04:32 2018

@author: yefang
"""

s = list(range(2,100000))

b = [2]
while len(s)!=0:
    n = s.pop(0)
    for i in b:
        if n % i ==0:
            break
    else:
        b.append(n)
print(b)
