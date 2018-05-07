# -*- coding: utf-8 -*-
"""
Created on Sun May  6 09:44:10 2018

@author: yefang

题目：求区间之内的素数。
"""

# 输出指定范围内的素数
 
# 用户输入数据
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
 
for num in range(lower,upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)