# -*- coding: utf-8 -*-
"""
Created on Sun May  6 10:41:34 2018

@author: yefang

题目：学习使用按位与 & 。

程序分析：0&0=0; 0&1=0; 1&0=0; 1&1=1。
"""

if __name__ == '__main__':
    a = 172
    b = a & 3
    print ('a & b = %d' % b)
    b &= 7
    print ('a & b = %d' % b)