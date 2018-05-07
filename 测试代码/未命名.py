s="a"

locals()[s+'1']=12
locals()[s+'2']=13


print(s2)
print(a1,a2)
class b():
	def say(self):
		return '我是b' 
class c():
	def say(self):
		return '我是c'
locals()[s+'3']=b()
locals()[s+'4']=c()
s1=a3.say
s2=a4.say

print(s1)
