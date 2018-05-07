# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:49:35 2018

@author: yefang

题目：列表转换为字典。
"""

i = ['a', 'b']
l = [1, 2]
print(dict([i,l]))

# 从列表创建字典
i = ['a','b','c']
l = [1,2,3]
b=dict(zip(i,l))
print(b)



l1 = ['a','b','c']
l2 = [1,2,3]
d = {}
for i in range(len(l1)):
    d.setdefault(l1[i],l2[i])
print (d)