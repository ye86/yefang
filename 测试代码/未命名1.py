# -*- coding: utf-8 -*-
"""
Created on Tue May  1 17:10:54 2018

@author: yefang
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:51:42 2018

@author: yefang
"""

import pygame as pg
import numpy as np 
# 定义类：二维点 
class D2_point(object):
    def __init__(self,x,y):
        #print ('***init')
        self.x = x
        self.y = y  
  
    def __add__(self,oth):
        
        if type(oth) == type(self) :
            return D2_point(self.x + oth.x,self.y + oth.y)
        else:
            return D2_point(self.x + oth,self.y + oth)
    def __sub__(self,oth):
        if type(oth) == type(self) :
            return D2_point(self.x - oth.x,self.y - oth.y)
        else:
            return D2_point(self.x - oth,self.y - oth)
    def __mul__(self,oth):
        if type(oth) == type(self) :
            return D2_segment(self, oth)
        else:
            return D2_point(self.x * oth,self.y * oth)
    def __truediv__(self,oth):
        if type(oth) == type(self) :
            return D2_line(self,oth)
        else:
            return D2_point(self.x / oth,self.y / oth)
  
    def info(self):
        #print ('***info')
        return self.x,self.y
    def __getitem__(self,key): 
        if key == 0 or key == 'x':
            return self.x
        if key == 1 or key == 'y':
            return self.y
    def __setitem__(self, key, value):
        if key == 0 or key == 'x':
            self.x = value
        if key == 1 or key == 'y':
            self.y = value

# 定义类 二维线段
class D2_segment(object):

    def __init__(self,a,b):
        if a.x == b.x:
            if a.y ==b.y:
                exit('两坐标相同')
            elif a.y > b.y:
                self.star = a
                self.end = b
            else:
                self.star = b
                self.end =a
        elif a.x < b.x:
            self.star = a
            self.end = b
        else:
            self.star = b
            self.end = a
        self.long = pow((pow(a.x - b.x ,2) + pow(a.y-b.y,2)),0.5)
    def info(self):
        return [[self.star.x, self.star.y],[self.end.x, self.end.y]]
    def toplt(self,分辨率=100):
        lx = []
        ly = []
        self.x = (self.end.x -self.star.x)/分辨率
        self.y = (self.end.y -self.star.y)/分辨率
        for i in range(分辨率):
            lx.append(self.star.x + self.x * i)
            ly.append(self.star.y + self.y * i)
        return [lx,ly]
    pass

# 定义类 二维直线
class D2_line(object):
    def __init__(self,a,b):
        # 求出直线表达式y=kx+b
        if a.x == b.x:
            if a.y ==b.y:
                exit('两坐标相同')
            self.k = 0
        else:
            self.k = (a.y - b.y)/(a.x - b.x)
        self.b = a.y - self.k * a.x
        
        # 求出直线与原点最近的点（x，y）
        self.c = (a.x*b.y - b.x*a.y)/(b.y-a.y)
        self.d = (a.x*b.y - b.x*a.y)/(-b.x + a.x)
        self.x = self.c*(self.d**2)/(self.c**2+self.d**2)
        self.y = self.d*(self.c**2)/(self.c**2+self.d**2)
    def 相交(self,oth):
        return D2_point((oth.b-self.b)/(self.k-oth.k),(oth.b*self.k-self.b*oth.k)/(self.k-oth.k))
    def info(self):
        if self.k == 0:
            return('y = %.2f',self.b)
        else:
            if self.b > 0:
                return( 'y = %.2fx+%.2f' % (self.k,self.b))
            elif self.b == 0:
                return( 'y = %.2fx' % self.k)
            else:
                return( 'y = %.2fx%.2f' % (self.k,self.b))
    def __getitem__(self,key): 
        if key == 0 or key == 'x':
            return self.x
        if key == 1 or key == 'y':
            return self.y
    def __setitem__(self, key, value):
        if key == 0 or key == 'x':
            self.x = value
        if key == 1 or key == 'y':
            self.y = value

白 = (255, 255, 255)
蓝 = (0, 0, 255)
黑 = (0,0,0)
width = 800
height = 800
FPS = 60
# create the display window
img = pg.display.set_mode((width, height))
# optional title bar caption
pg.display.set_caption("Pygame draw circle and save")
# default background is black, so make it white
img.fill(黑)
点 = D2_point
star = 点(width//2, height//2)
end = 点(width//2, height//2)
center = 点(width//2, height//2)
d1 = 点(0,0)
d2 = 点(0,0)
# width of 0 (default) fills the circle
# otherwise it is thickness of outline

# 点着色

# 线着色

# now save the drawing
# can save as .bmp .tga .png or .jpg

# update the display window to show the drawing
pg.display.flip()
# event loop and exit conditions
# (press escape key or click window title bar x to exit)
s = 0
q = 0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # most reliable exit on x click
            pg.quit()
            raise SystemExit
        elif event.type == pg.KEYDOWN:
            # optional exit with escape key
            if event.key == pg.K_ESCAPE:
                pg.quit()
                raise SystemExit
    if s == 360:
        s = 0
    if q == 200:
        q = 0
        
    pygame.draw.line(img, (0,0,0), (star.x, star.y), (end.x, end.y))
    s += 1
    q += 1
    d1.x = np.cos(s * np.pi * 2 / 360) *100
    d1.y = np.sin(s * np.pi * 2 / 360) *100
    d2.x = np.cos(q * np.pi * 2 / 200) *200
    d2.y = np.sin(q * np.pi * 2 / 200) *200
    star = center + d1 - d2
    end = star + d1 + d2
    pygame.draw.line(img, (255,0,255), (star.x, star.y), (end.x, end.y))
    
    pygame.display.update()  
    pygame.time.Clock().tick(FPS) 
        
