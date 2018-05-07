# -*- coding: utf-8 -*-
"""
Created on Sun May  6 10:22:33 2018

@author: yefang

题目：两个变量值互换。
"""

def exchange(a,b):
    a,b = b,a
    return (a,b)
 
if __name__ == '__main__':
    x = 10
    y = 20
    print('x = %d,y = %d' % (x,y))
    x,y = exchange(x,y)
    print('x = %d,y = %d' % (x,y))