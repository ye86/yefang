# -*- coding: utf-8 -*-
"""
Created on Sat May  5 17:06:22 2018

@author: yefang

题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。
"""

Tn = 0
Sn = 0
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn += a
    a *= 10
    Sn += Tn
    print(Tn)
 
print ("计算和为：",Sn)
