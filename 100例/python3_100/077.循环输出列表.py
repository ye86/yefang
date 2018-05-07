# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:31:04 2018

@author: yefang

题目：循环输出列表
"""

if __name__ == '__main__':
    s = ["man","woman","girl","boy","sister"]
    # 方法1
    for i in range(len(s)):
        print(s[i])
        
        
    print("\n")
    # 方法2
    for i in s:
        print(i)