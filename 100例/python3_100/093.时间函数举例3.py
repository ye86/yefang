# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:29:59 2018

@author: yefang

时间函数举例3
"""


if __name__ == '__main__':
    import time
    start = time.clock()
    for i in range(10000):
        print (i)
    end = time.clock()
    print ('different is %6.3f' % (end - start))