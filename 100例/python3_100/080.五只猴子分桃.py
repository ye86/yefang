# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:46:33 2018

@author: yefang

题目：海滩上有一堆桃子，五只猴子来分。
第一只猴子把这堆桃子平均分为五份，多了一个，
这只猴子把多的一个扔入海中，拿走了一份。
第二只猴子把剩下的桃子又平均分成五份，又多了一个，
它同样把多的一个扔入海中，拿走了一份，
第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
"""


i = 0
j = 1
x = 0
while (i < 5) :
    x = 4 * j
    for i in range(0,5) :
        if(x%4 != 0) :
            break
        else :
            i += 1
        x = (x/4) * 5 +1
    j += 1
print( x)
    
    
    
# 猴子分桃，最少问题分析：问最少有多少只桃子，则岸上最后剩的桃子数目越小，则原岸上的桃子越少
# 假设最后岸上还剩4x只桃子,可以利用递归方法求解

print('\n递归方法:')
num=int(input("输入猴子的数目:"))
def fn(n):
    if n==num:
        return(4*x)       #最后剩的桃子的数目
    else:
        return(fn(n+1)*5/4+1)
    
x=1
while 1:
    count=0
    for i in range(1,num):
        if fn(i)%4==0 :
            count=count+1
    if count==num-1:
        print("海滩上原来最少有%d个桃子" % int(fn(0)))
        break
    else:
        x=x+1
        





# 比较笨的方法
print('\n比较笨的方法:')
start,end,m1=0,100,0
while m1==0:
    end=end*2
    for i in range(start,end):
        m5=5*i+1
        if m5%4==0:
            m4=(m5/4)*5+1
            if m4%4==0:
                m3=(m4/4)*5+1
                if m3%4==0:
                    m2=(m3/4)*5+1
                    if m2%4==0:
                        m1=(m2/4)*5+1
                        break
    start=i
print("最少为：%d个桃子" % m1)