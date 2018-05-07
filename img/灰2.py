# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import os
from skimage import io

# 读灰度图片
img=io.imread("e:/yefang/img/2.jpg",as_grey=True)

# io.imshow(img)

def 二维像素(img):
    _img =img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if i  and img.shape[0]-1-i and j and img.shape[1]-1-j:
                _img[i][j] = (img[i-1][j-1]+img[i-1][j]+img[i-1][j+1]+img[i][j-1]+img[i][j]+img[i][j+1]+img[i+1][j-1]+img[i+1][j]+img[i+1][j+1])/9
#            if i == img.shape[0]-1:
#                pass
#            else:
#                if j == img.shape[1]-1:
#                    pass
#                else:
#                    if abs(img[i][j] - img[i+1][j]) < 像素值 or abs(img[i][j] - img[i][j+1]) < 像素值:
#                        _img[i][j] = 1
#                    else:
#                        _img[i][j] = 0
    return _img

img1 = 二维像素(img)
io.imshow(img1)