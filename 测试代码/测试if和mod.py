
class 周期:
	def __init__(self,循环体,循环数):
		self.循环体=int(循环体)
		self.循环数=int(循环数)
	def 加(self):
		self.循环数 += 1
		if self.循环数 >= self.循环体:
			self.循环数 -= self.循环体
		return self.循环数
	def 减(self):
		self.循环数 -= 1
		if self.循环数 < 0:
			self.循环数 += self.循环体
		return self.循环数
b2 = 周期(2,1)
b3 = 周期(3,1)
b5 = 周期(5,1)
b7 = 周期(7,1)
for each in range(10000000):
	c2 = b2.加()
	c3 = b3.加()
	c5 = b5.加()
	c7 = b7.加()

print(c2,c3,c5,c7)