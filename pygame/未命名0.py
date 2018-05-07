# -*- coding: utf-8 -*-
"""
Created on Sat May  5 13:26:41 2018

@author: yefang
"""

import pygame as pg
import sys
from skimage import io as skio

# 计算适合屏幕显示的比例（a为屏幕，b为图像）
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


# 在window窗口上显示传入的图像
def display(img):
    global window
    pgw = window.get_width()    #获取显示宽度
    pgh = window.get_height()   #获取显示高度 
    imgh = img.shape[0]         #获取图片高度
    imgw = img.shape[1]         #获取图片高度
    nw,nh = new_wh(pgw,pgh,imgw,imgh) # 计算适合显示的尺寸
    # img1 = img[:nh,:nw,:] # 生成适合显示的图片尺寸格式

    _h = (pgh - nh) // 2  # 显示高度位移量
    _w = (pgw - nw) // 2  # 显示宽度位移量
    
    # 将新图片显示在屏幕上
    for w in range(nw):
        for h in range(nh): 
            rand_col = img[int(h*(imgh/nh))][int(w*(imgw/nw))] 
            rand_pos = (w + _w, h + _h)              
            window.set_at(rand_pos, rand_col) 


img=skio.imread("1.jpg")
pgw = 800
pgh = 600

pg.init() 
window = pg.display.set_mode((pgw,pgh), 0, 32)  


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
    
    
    
    
    