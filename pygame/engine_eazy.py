from math_tools2 import *
import pygame, sys
import threading


import random

class Camera:
	def __init__(self,place,i,j,k,d=1):	# 上帝表示
		self.place = place # V
		self.i = i	# V	这里先任凭自由度损失吧……
		self.j = j	# V
		self.k = k	# V
		self.d = d	# j=d

		self.d2 = 0.1 # 截断面，由于pygame支持线段端点延伸，只需取一个较小值
		
		self.up = V3(0,0,1)
		
	@property
	def mat(self):
		return Array(self.i,self.j,self.k)
	
	def real_imag(self,v):
		return np.dot(np.linalg.inv(self.mat).T, v - self.place)
	
	
	def trans1(self,v):	# V3 -> V3
		#return V3(*self.real_imag(v))
		return self.real_imag(v)
		
		
	def trans2(self,v): # V3 -> V2
		x,y,z = v
		return V2(x*self.d/y,z*self.d/y)
		
	def rotate(self,v,theta):
		self.i.rotate(v,theta)
		self.j.rotate(v,theta)
		self.k.rotate(v,theta)


class Screen:
	def __init__(self,place,i,j):	# 屏幕表示, ix等为相对
		self.place = place
		self.i = i
		self.j = j
		
	@property
	def mat(self):
		return Array(self.i,self.j)
	
	def imag_real(self,v):
		place, i, j = self.place, self.i, self.j
		return np.dot(self.mat,v) + self.place
	
	def trans(self,v):
		return V2(*self.imag_real(v))
		
		


# 可绘制对象

class P(V3):	# 点
	def imag_real(self,place,i,j,k):
		return np.dot(Array(i,j,k),self)+place
	
	def draw(self,window,camera,screen,color=(255,255,255),t=None):
		if t:
			self = self.imag_real(*t)

		p = screen.trans(camera.trans(self))
		x, y = p
		try:
			pygame.draw.line(window,color,(x,y),(x+1,y+1),1)
		except:
			print("Paint error",x,y)
			
			

class L(VV):	# 线
	def draw(self,window,camera,screen,color=(255,255,255),t=None):
		p1 = self.p1
		p2 = self.p2
		if t:
			p1 = p1.imag_real(*t)
			p2 = p2.imag_real(*t)
		
		
		p1 = camera.trans1(p1)
		p2 = camera.trans1(p2)
		
		d = camera.d2
		x1,y1,z1 = p1
		x2,y2,z2 = p2
		is_back1 = y1 <= d
		is_back2 = y2 <= d
		if is_back1 and is_back2 :
			return
		if is_back1:
			k = (d-p1[1])/(p2[1]-p1[1])
			p1 = p1 + k*(p2-p1)
		elif is_back2:
			k = (d-p2[1])/(p1[1]-p2[1])
			p2 = p2 + k*(p1-p2)
		p1 = screen.trans(camera.trans2(p1))
		p2 = screen.trans(camera.trans2(p2))

		x1, y1 = p1
		x2, y2 = p2
		try:
			pygame.draw.line(window,color,(x1,y1),(x2,y2),1)
		except:
			print("Paint error",x1,y1,x2,y2)
		
class F:	# 面
	def __init__(self,*l):
		self.l = l
		
		self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		
			
	
	def draw(self,window,camera,screen,color=(255,255,255),t=None):
		
		color = self.color
		
		pointlist_before = [p.imag_real(*t) for p in self.l] if t else self.l
		
		#~ d = camera.d2
		d = camera.d
		pointlist = []
		px = camera.trans1(pointlist_before[-1])
		ax = px[1] > d
		for p_ in pointlist_before:
			p = camera.trans1(p_)
			if ax == True and p[1] >= d:
				pointlist.append(screen.trans(camera.trans2(p)))
			elif ax == True and p[1] < d:
				k = (d-p[1])/(px[1]-p[1])
				pointlist.append(screen.trans(camera.trans2(p + k*(px-p))))
			elif ax == False and p[1] >= d:
				k = (d-p[1])/(px[1]-p[1])
				pointlist.append(screen.trans(camera.trans2(p + k*(px-p))))
				pointlist.append(screen.trans(camera.trans2(p)))
				
			elif ax == False and p[1] < d:
				pass
			px = p
			ax = p[1] > d
			
		try:
			if pointlist:	pygame.draw.polygon(window, color, pointlist)
		except:
			print("Paint error",pointlist)
			

class Obj:	# t = place, i, j, k
	def __init__(self):	# 以相对坐标
		self.l = []
	
	def append1(self,obj):
		self.l.append2(obj,None)
		
	def append2(self,obj,t):	# 标准添加对象方法，t是位置和方向
		assert obj != self
		if type(obj) == Obj:	# P L F 是简单对象直接画，obj是简单对象的组合
			for obj_,t_ in obj.l:
				self.append2(obj_,compound(t,t_))
		else:
			self.l.append((obj,t))
	
	def lappend1(self,l):
		for obj in l:
			self.append2(obj,None)
		
	def lappend2(self,l):
		for obj,t in l:
			self.append2(obj,t)
	
	#~ def draw(self,window,camera,screen,t=None):
		#~ for obj,obj_t in self.l:
			#~ obj.draw(window,camera,screen,t=compound(t,obj_t))# ????
	def draw(self,window,camera,screen,t=None):
		for obj,obj_t in self.l:
			obj.draw(window,camera,screen,t=compound(t,obj_t))# ????


p1 = P(0,0,0)
p2 = P(1,0,0)
p3 = P(1,1,0)
p4 = P(0,1,0)
p5 = P(0,0,1)
p6 = P(1,0,1)
p7 = P(1,1,1)
p8 = P(0,1,1)

#~ l = [
#~ F(p1,p2,p3,p4),F(p5,p6,p7,p8),
#~ F(p1,p2,p6,p5),F(p2,p3,p7,p6),
#~ F(p3,p4,p8,p7),F(p4,p1,p5,p8),
#~ ]
l = [
L(p1,p2),L(p2,p3),L(p3,p4),L(p4,p1),
L(p5,p6),L(p6,p7),L(p7,p8),L(p8,p5),
L(p5,p1),L(p6,p2),L(p7,p3),L(p8,p4),
]
square = Obj()
square.lappend1(l)

# 游戏类（用于运行）
if "for: check_events":
	def keydown_K_ESCAPE(self):
		print()
		print("帧频：",self.clock.get_fps())
		sys.exit()		
	def keydown_K_a(self):
		self.left = True
		self.right = False
	def keydown_K_d(self):
		self.right = True
		self.left = False
	def keydown_K_w(self):
		self.go = True
		self.back = False
	def keydown_K_s(self):
		self.back = True
		self.go = False
	def keydown_K_SPACE(self):
		self.up = True
		self.down = False
	def keydown_K_LSHIFT(self):
		self.down = True
		self.up = False
	def keydown_K_LCTRL(self):
		self.check()
	keydown_d = {
	pygame.K_ESCAPE:keydown_K_ESCAPE,
	pygame.K_a:keydown_K_a,
	pygame.K_d:keydown_K_d,
	pygame.K_w:keydown_K_w,
	pygame.K_s:keydown_K_s,
	pygame.K_SPACE:keydown_K_SPACE,
	pygame.K_LSHIFT:keydown_K_LSHIFT,
	pygame.K_LCTRL:keydown_K_LCTRL,
	}
	
				
	def keyup_K_a(self):
		self.left = False
	def keyup_K_d(self):
		self.right = False
	def keyup_K_w(self):
		self.go = False
	def keyup_K_s(self):
		self.back = False
	def keyup_K_SPACE(self):
		self.up = False
	def keyup_K_LSHIFT(self):
		self.down = False
	
	keyup_d = {
	pygame.K_a:keyup_K_a,
	pygame.K_d:keyup_K_d,
	pygame.K_w:keyup_K_w,
	pygame.K_s:keyup_K_s,
	pygame.K_SPACE:keyup_K_SPACE,
	pygame.K_LSHIFT:keyup_K_LSHIFT,
	}
	event_type_d = {
	pygame.KEYDOWN:keydown_d,
	pygame.KEYUP:keyup_d,
	
	}

class App_:		# 基础类
	def main(self):
		self.init()
		self.clock = pygame.time.Clock()
		#~ threading.Thread(target=self.thread_window_update,args=()).start()
		while True:
			self.window_update()
			self.check_events()
			self.var_update()	# 自动更新
			self.clock.tick(20)
			
	def init(self):
		pygame.init()
		self.window = pygame.display.set_mode((1200,800))
		pygame.display.set_caption("Example")
		
		pygame.event.set_grab(True)
		pygame.mouse.set_visible(False)	# 隐藏鼠标
	
		self.camera = Camera(V3(0,-10,1),V3(1,0,0),V3(0,1,0),V3(0,0,1),5)
		self.screen = Screen(V2(600,400),V2(200,0),V2(0,-200))
		self.go = False
		self.back = False
		self.left = False
		self.right = False
		self.up = False
		self.down = False
		
		self.obj = Obj()	# 环境是一个复合对象
		self.make_obj()
	
	def make_obj(self):
		pass
	
	def window_update(self):
		self.window.fill((0,0,0))
		
		self.obj.draw(self.window,self.camera,self.screen)
		
		pygame.draw.line(self.window,(48,48,48),(600-5,400),(600+5,400),1)
		pygame.draw.line(self.window,(48,48,48),(600,400-5),(600,400+5),1)
		pygame.display.flip()

	def check_events(self):
		for event in pygame.event.get():
			key_d = event_type_d.get(event.type,None)
			if not key_d: return
			f = key_d.get(event.key,None)
			if not f: return
			f(self)
			
	def var_update(self):
		if self.go:
			self.camera.place += self.camera.j/10
		elif self.back:              
			self.camera.place -= self.camera.j/10
		if self.left:                
			self.camera.place -= self.camera.i/10
		elif self.right:            
			self.camera.place += self.camera.i/10
		if self.up:                
			self.camera.place += self.camera.k/10
		elif self.down:            
			self.camera.place -= self.camera.k/10

		dx, dy = pygame.mouse.get_rel()
		self.camera.rotate(self.camera.k,-dx/2000)
		self.camera.rotate(self.camera.i,-dy/2000)
		
	def check(self):
		pass
	

