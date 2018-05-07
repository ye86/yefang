# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:51:57 2018

@author: yefang

题目：809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，
9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
"""

a = 809
for i in range(10,100):
    b = i * a
    if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
        print( b,' = 800 * ', i, ' + 9 * ', i)
        



# 参考方法1：

l1=[m for m in range(10,100//8+1)]
l2=[m for m in range(12,1000//9+1)]
for i in l1:
    if i in l2:
        k=i
print('809*%d,=%d' % (k,k*809))

# 参考方法2：
def func():
    m = 809    # 9 *??的结果为3位数
    for i in range(1000):
        if i*9<1000:
            n=i #n为最大的范围
    for i in range(1,n):
        if i*8<100: #8*??的结果为两位数
            if i*809<10000:  #809*??为四位数
                if len(str(i*9)) > 2: #9*??结果为3位数 
                   if m*i==800*i+9*i:
                        print (i)
                        print("和为：",m*i)

func()

# 参考方法3：

for i in range(10,101):
    if 809 * i == 800 * i + 9 * i:
        if 8 * i < 100 :
            if 9 * i > 100 and 9 * i < 1000:
                print (i ,809 * i)
                
'''                
假设这个两位数为x, 那它肯定是在range(10,100)中，可用for循环来遍历，
综合题目中给定的其他限定条件用if 语句和 and堆叠在一起便可求得这个数，代码如下：
'''
for i in range(10,100):
    if (809 * i >= 1000) and (8 * i <= 100) and (9 * i >= 100) and (809 * i == 800 * i + 9 * i):
          print("这个两位数是: {0}, 809乘以这个两位数{0}的结果是: {1}".format(i, 809 * i))