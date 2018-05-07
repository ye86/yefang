# -*- coding: utf-8 -*-
"""
Created on Sun May  6 10:09:22 2018

@author: yefang

题目：学习使用auto定义变量的用法。

程序分析：没有auto关键字，使用变量作用域来举例吧。
"""

num = 2
def autofunc():
    num = 1
    print('internal block num = %d' % num)
    num += 1
for i in range(3):
    print('The num = %d' % num)
    num += 1
    autofunc()