# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:05:35 2018

@author: yefang

题目：八进制转换为十进制
"""

n = 0
p = input('input a octal number:\n')
for i in range(len(p)):
    n = n * 8 + ord(p[i]) - ord('0')
print(n)



# 参考方法：
def f8to10(num):
    print("8进制数：", num)
    l = str(num)
    length = len(l)
    sum = 0
    for i in range(length):
        sum += 8 ** i * int(l[length-1-i])
    print("转成10进制数为：",sum)

f8to10(122)



n=input('请输入一个八进制数：')
#使用列表推导式来写
lost=sum([int(n[-i])*8**(i-1) for i in range(1,len(n)+1)])
print('转换十进制数为：%s'%lost)