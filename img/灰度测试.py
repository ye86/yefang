# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 17:56:48 2018

@author: yefang
"""

import os
from skimage import io

# 读JPG文件
img=io.imread("e:/yefang/img/1.jpg")

# 读三原色之一
img1=img[:,:,1]


# 提取单色图中的指定像素，返回0和1组成的数组
# 复制一份新的单色图，等于指定像素值的为1，不等于的为0，return 新图
def 二维像素(img,像素值):
    _img =img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j] == 像素值:
                _img[i][j] = 1
            else:
                _img[i][j] = 0
    return _img


# 提取值等于1的坐标                
#def 提取坐标(img):
#    for i in range(img.shape[0]):
#        for j in range(img.shape[1]):
#            if img[i][j] == 1:
#                print("%d,%d坐标值为1"%(i,j))
#
# 遍历256个色度，写入到256个文本文件，值为真时写入“米”，为0时写入“  ”，
for i in range(255):
    xy01 = 二维像素(img1,i)  # xy01 是由01组成的二维图
    with open('a%s.txt'% i,"w") as f:
        for j in range(xy01.shape[0]):
            for k in range(xy01.shape[1]):
                if xy01[j][k] == 1:
                    f.write('米')
                else:
                    f.write('  ')
            f.write('\n')
        f.close()


    




