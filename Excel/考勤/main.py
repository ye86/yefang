# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:45:12 2018

@author: yefang
"""

import os
import glob
import convert

# 获取指定文件夹下的指定文件类型的列表，默认当前目录，.xls文件
def findfiles(dirname=0,pattern='*.xls'):
    cwd = os.getcwd() #保存当前工作目录
    if dirname == 0:
        dirname = cwd
    if dirname:
        os.chdir(dirname)

    result = []
    for filename in glob.iglob(pattern): #此处可以用glob.glob(pattern) 返回所有结果
        result.append(filename)
    #恢复工作目录
    os.chdir(cwd)
    return result

def test():
    xlslist = findfiles()
    for i in xlslist:
        if i[:4] != 'new_':
            convert.考勤表转换(i)
    

if __name__ == '__main__': 
    test()