# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:28:39 2018

@author: yefang

时间函数举例2
"""

if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(3000):
        print (i)
    end = time.time()
 
    print (end - start)