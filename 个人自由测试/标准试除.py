import math
N = 50097840248975052365

x = int(math.sqrt(N))

for i in range(1,x):
	
	if N%(x+i)== 0:
		print("P为%d，Q为%d" % (x+i,N/(x+i)))
		break
