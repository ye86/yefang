# -*- coding: utf-8 -*-
import os
from skimage import io

# 读灰度图片
img=io.imread("e:/yefang/img/1.jpg",as_grey=True)

# io.imshow(img)

def 二维像素(img,像素值):
    _img =img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if abs(img[i][j] - 像素值) > 0.05:
                _img[i][j] = 1
    return _img

img1 = 二维像素(img,0.8)
io.imshow(img1)