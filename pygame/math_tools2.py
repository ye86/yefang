import numpy as np

def Array(*l):
	return np.array(l)

class Q4:
	def mul(z1,z2):	# 对四元数组操作
		a,b,c,d = z1
		w,x,y,z = z2
		return np.array([
				a*w-b*x-c*y-d*z,
				a*x+b*w+c*z-d*y,
				a*y-b*z+c*w+d*x,
				a*z+b*y-c*x+d*w
				])
				
	def conjugate(z1):	# 对四元数组操作
		a,b,c,d = z1
		return np.array([a,-b,-c,-d])
	

class V3(np.ndarray):
	def __new__(cls,*a):
		return np.ndarray.__new__(cls,3)
	def __init__(self,x,y,z):
		self[0] = x
		self[1] = y
		self[2] = z
		
	def abs(self):
		return np.linalg.norm(self)    
	
	def e(self):
		return self * self.abs()
	
	def rotate(self,v,theta):
		x,y,z = v.e()*np.sin(theta/2)
		h = Array(np.cos(theta/2),x,y,z)
		x,y,z = self
		p = Array(0,x,y,z)
		_,self[0],self[1],self[2] = Q4.mul(Q4.mul(h,p),Q4.conjugate(h))
		
	def __str__(self):
		return "V3({0},{1},{2})".format(*self)
	
	
class V2(np.ndarray):
	def __new__(cls,*a):
		return np.ndarray.__new__(cls,2)
	def __init__(self,x,y):
		self[0] = x
		self[1] = y
	
	def __str__(self):
		return "V2({0},{1})".format(*self)

######################################	

class VV:	# 不一定是三维直线
	def __init__(self,p1,p2):
		self.p1 = p1
		self.p2 = p2
		
	def __str__(self):
		return str(self.p1) + '->' + str(self.p2)
		


# 仿射复合
def compound(t1,t2):
	if t1 == None:
		return t2	# 都为None也满足
	if t2 == None:
		return t1
	
	print("hehe")
	
	place1,i1,j1,k1 = t1
	mat1 = Array(i1,j1,k1)
	
	place2,i2,j2,k2 = t2
	mat2 = Array(i2,j2,k2)
	
	place_ = np.dot(mat2,place1) + place2
	mat_ = np.dot(mat2,mat1)
	i_ = V3(*mat_[0])
	j_ = V3(*mat_[1])
	k_ = V3(*mat_[2])
	
	return (place_,i_,j_,k_)


