# -*- coding: utf-8 -*-
"""
Created on Sun May  6 09:53:23 2018

@author: yefang

题目：求一个3*3矩阵主对角线元素之和。

程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
"""

if __name__ == '__main__':
    a = []
    sum1 = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input("input num:\n")))
    for i in range(3):
        sum1 += a[i][i]
    print(sum1)