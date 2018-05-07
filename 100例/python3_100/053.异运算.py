# -*- coding: utf-8 -*-
"""
Created on Sun May  6 10:59:27 2018

@author: yefang

题目：学习使用按位异或 ^ 。

程序分析：0^0=0; 0^1=1; 1^0=1; 1^1=0
"""

if __name__ == '__main__':
    a = 77
    b = a ^ 3
    print('The a ^ 3 = %d' % b)
    b ^= 7
    print('The a ^ b = %d' % b)