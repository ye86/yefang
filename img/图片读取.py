# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 15:41:14 2018

@author: yefang
"""

import os
from skimage import io
img=io.imread("e:/yefang/img/1.jpg")
new_0=img.copy()
new_1=img.copy()
new_2=img.copy()
new_0[:,:,1]=0
new_0[:,:,2]=0
new_1[:,:,0]=0
new_1[:,:,2]=0
new_2[:,:,0]=0
new_2[:,:,1]=0

# 保存图片
io.imsave("e:/yefang/img/new_0.jpg",new_0)
io.imsave("e:/yefang/img/new_1.jpg",new_1)
io.imsave("e:/yefang/img/new_2.jpg",new_2)


