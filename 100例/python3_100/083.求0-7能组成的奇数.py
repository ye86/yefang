# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:08:38 2018

@author: yefang

题目：求0—7所能组成的奇数个数。

程序分析：

组成1位数是4个。

组成2位数是7*4个。

组成3位数是7*8*4个。

组成4位数是7*8*8*4个。
"""

def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 7
    else:
        return f(n-1)*8
l = []
#算出每位数有多少奇数
for i in range(1,9):
    l.append(f(i-1)*4)
print(l)
#输出一共有多少个奇数
print(sum(l))


#方法2
if __name__ == '__main__':
    sum1 = 4
    s = 4
    for j in range(2,9):
        print (sum1)
        if j <= 2:
            s *= 7
        else:
            s *= 8
        sum1 += s
    print('sum = %d' % sum1)