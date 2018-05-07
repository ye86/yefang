# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:09:40 2018

@author: yefang

题目：暂停一秒输出，并格式化当前时间。

程序分析：无。
"""

import time
 
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
 
# 暂停一秒
time.sleep(1)
 
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))