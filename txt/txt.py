import re
with open('1.txt','r') as f:
    a = f.read()
    
b = re.split(r'\d+',a)

for i,j in enumerate(b):
    while j[:1] == ' ':
        b[i] = j[1:]
    
d = []
e = []
for i in b:
    d.append(i[:3])
    e.append(i[3:])
print(d)

print(e)