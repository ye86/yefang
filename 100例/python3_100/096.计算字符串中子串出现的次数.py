# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:33:39 2018

@author: yefang

题目：计算字符串中子串出现的次数。
"""

if __name__ == '__main__':
    str1 = input('请输入一个字符串:\n')
    str2 = input('请输入一个子字符串:\n')
    ncount = str1.count(str2)
    print (ncount)