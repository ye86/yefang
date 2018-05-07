# -*- coding: utf-8 -*-
"""
Created on Sat May  5 15:18:22 2018

@author: yefang
"""

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print(i,j,k)