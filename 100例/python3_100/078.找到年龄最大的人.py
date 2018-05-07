# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:34:30 2018

@author: yefang

题目：找到年龄最大的人，并输出。请找出程序中有什么问题。
"""


person = {"li":18,"wang":50,"zhang":20,"sun":22}
m = 'li'
for key in person.keys():
    if person[m] < person[key]:
        m = key
 
print ('%s,%d' % (m,person[m]))
    
    
    


# 参考解法：
import operator

__author__ = 'Lei Zhong'

person = {"li":18,"wang":50,"zhang":20,"sun":22}
print(max(person.iteritems(), key=operator.itemgetter(1))[0])   # 获取最大值的 key
print(max(person.values()))                                      # 获取最大值



# 参考方法：
person = {"li":18,"wang":50,"zhang":20,"sun":22}
def find_max(dict):
    max_age = 0
    for key, value in dict.items():
        if value > max_age:
            max_age = value
            name = key
    print(name)
    print(max_age)
find_max(person)

