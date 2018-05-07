l = [2]
for i in range(3,5000+1):
	if all(map(lambda a: i%a,l)):
		l.append(i)
print(l)