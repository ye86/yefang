# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:08:52 2018

@author: yefang

题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。
"""

import time
 
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1) # 暂停 1 秒