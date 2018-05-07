# -*- coding: utf-8 -*-
"""
Created on Tue May  1 16:51:56 2018

@author: yefang
"""

import pygame as pg
# pygame uses (r, g, b) color tuples
白 = (255, 255, 255)
蓝 = (0, 0, 255)
黑 = (0,0,0)
width = 300
height = 300
FPS = 20
# create the display window
img = pg.display.set_mode((width, height))
# optional title bar caption
pg.display.set_caption("Pygame draw circle and save")
# default background is black, so make it white
img.fill(黑)
# draw a blue circle
# center coordinates (x, y)
center = (width//2, height//2)
radius = min(center)
# width of 0 (default) fills the circle
# otherwise it is thickness of outline
width = 0
# 点着色
img.set_at((100, 100), (255,255,255))
# 线着色
pg.draw.line(img, (255,0,255), (100, 100), (200, 200))
# now save the drawing
# can save as .bmp .tga .png or .jpg

# update the display window to show the drawing
pg.display.flip()
# event loop and exit conditions
# (press escape key or click window title bar x to exit)
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
    
    pygame.display.update()  
    pygame.time.Clock().tick(FPS) 