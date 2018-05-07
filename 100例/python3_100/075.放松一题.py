# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:22:17 2018

@author: yefang

题目：放松一下，算一道简单的题目。
"""

if __name__ == '__main__':
    for i in range(5):
        n = 0
        if i != 1: n += 1
        if i == 3: n += 1
        if i == 4: n += 1
        if i != 4: n += 1
        if n == 3: print (64 + i)
        





# 判断情人节：
    import time
    date=time.strftime('%m-%d',time.localtime())
    if date=='02-14':
        print('情人节是时候给你女朋友买支玫瑰花了！！')
    else:
        print('这时候你不要忘记发个红包！！')
    print('哈哈，这是一个测试题！！')