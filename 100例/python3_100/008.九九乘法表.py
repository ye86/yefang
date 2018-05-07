# -*- coding: utf-8 -*-
"""
Created on Sat May  5 15:45:06 2018

@author: yefang
题目：输出 9*9 乘法口诀表。

程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
"""
a = ""
for i in range(1, 10):
    a += '\n'
    for j in range(1, i+1):
        a += "%01d*%01d=%02d " % (i, j, i*j)
print(a)