# -*- coding: utf-8 -*-
"""
Created on Sat May  5 13:26:41 2018

@author: yefang
"""

import pygame as pg

import time

# from random import randint  
import sys
from skimage import io as skio

# 获取适合屏幕显示的比例
def new_wh(aw,ah,bw,bh):
    if ah >= bh:
        if aw >= bw:
            return bw,bh
        else:
            return aw,int(aw/bw *bh)
    else:
        if aw >= ah/bh * bw :
            return int(ah/bh * bw),ah
        else:
            return aw,int(aw/bw *bh)



def display(img):
    global window   
    # 将新图片显示在屏幕上
    for w in range(nw):
        for h in range(nh): 
            rand_col = img[int(h*(imgh/nh))][int(w*(imgw/nw))] 
            rand_pos = (w + _w, h + _h)              
            window.set_at(rand_pos, rand_col) 


img=skio.imread("d:/yefang/img/1.jpg")
pgw = 400 # 显示宽度
pgh = 300 # 显示高度 


# 显示图片



pg.init() 
window = pg.display.set_mode((pgw,pgh), 0, 32)  

imgh = img.shape[0]
imgw = img.shape[1]
nw,nh = new_wh(pgw,pgh,imgw,imgh) # 获得适合显示的尺寸
# img1 = img[:nh,:nw,:] # 生成一张大小适合显示的图片
_h = (pgh - nh) // 2  # 显示高度位移量
_w = (pgw - nw) // 2  # 显示宽度位移量

while True:
    
    for event in pg.event.get():  
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    window.fill((0, 0, 0)) 
    
    window.lock()  
    display(img)
    window.unlock()  
    pg.display.update()
    # time.sleep(1)