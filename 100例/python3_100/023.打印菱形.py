# -*- coding: utf-8 -*-
"""
Created on Sun May  6 08:03:26 2018

@author: yefang

打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
"""

for i in range(4):
    a=""
    for j in range(2 - i + 1):
        a += ' '
    for k in range(2 * i + 1):
        a += '*'
    print(a)
 
for i in range(3):
    a = ""
    for j in range(i + 1):
        a += ' '
    for k in range(4 - 2 * i + 1):
        a += '*'
    print(a)