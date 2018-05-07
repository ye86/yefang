# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:51:42 2018

@author: yefang
"""
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


# 三维点，待续……
class D3_point(D2_point):
    def __init__(self,x,y,z):
        #print ('3Dinit')
        super(D3_point,self).__init__(x,y)      #python2 中，super()需指定子类的继承
        self.z = z
    def __add__(self,oth):
        #print ('3Dadd')
        return D3_point(self.x + oth.x,self.y + oth.y,self.z + oth.z)
    def info(self):
        #print ('3Dinfo')
        print(self.x,self.y,self.z)

def myadd(a,b):         #注意此处是def，而不是class
    print ('***myadd')
    return a + b

        

if __name__ == '__main__':
    #myadd(D2_point(1,2),D2_point(3,4)).info()
    #myadd(D3_point(1,2,3),D3_point(4,5,6)).info()  
    
    二维点 = D2_point

    二维线段 = D2_segment

    二维直线 = D2_line

    点a = 二维点(6,5)

    点b = 二维点(13,-6)
    
    点c = 二维点(15,7)
    
    点d = 二维点(-5,-16)

    直线1 = 二维直线(点a,点b)
    
    直线2 = 二维直线(点c,点d)
    
    相交点1 = 直线1.相交(直线2)
    

    
    print(直线1.info())
    print(直线2.info())
    print('两直线相交于点[%f,%f]'% (相交点1.x,相交点1.y))
    
    ab = 点a * 点b
    cd = 点c * 点d
    print('线段ab为%s\n线段cd为%s' % (ab.info(), cd.info()) )
    print('ab的长为%f，cd的长为%f' % (ab.long, cd.long) )    