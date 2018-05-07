# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:44:13 2018

@author: yefang

题目：字符串排序。
"""

if __name__ == '__main__':
    str1 = input('input string:\n')
    str2 = input('input string:\n')
    str3 = input('input string:\n')
    print (str1,str2,str3)
    
    if str1 > str2 : str1,str2 = str2,str1
    if str1 > str3 : str1,str3 = str3,str1
    if str2 > str3 : str2,str3 = str3,str2
 
    print ('after being sorted.')
    print (str1,str2,str3)