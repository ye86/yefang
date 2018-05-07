# -*- coding: utf-8 -*-
"""
Created on Sun May  6 08:58:33 2018

@author: yefang

题目：利用递归方法求5!。

程序分析：递归公式：fn=fn_1*4!


"""

def fact(j):
    sum1 = 0
    if j == 0:
        sum1 = 1
    else:
        sum1 = j * fact(j - 1)
    return sum1
 
print(fact(5))