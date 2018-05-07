import random
总和 = 0

for i in range(0,999):
    temp = random.randint(0,999)
    总和 = 总和 + int(temp)
    平均数 = 总和 / (i+1)
    print("i=%03d temp=%03d 平均数=%03d"%(i , temp , 平均数))
print('运行结束')
