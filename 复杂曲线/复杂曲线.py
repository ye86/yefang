import random,math

x = 50
a = 0
b = 0
c = 0
d = 0
e = 0
z = "*"
for i in range(0,150):

    if d==0:
        a += 1
        if a == 10:
            d = 1
    else:
        a -= 1
        if a == -10:            
            d = 0


    if e==0:
        b += 0.1
        if b == 1.6:
            e = 1
    else:
        b -= 0.1
        if b == -3.8:
            e = 0


#    x += 1

    
    y = 40 + a * math.sqrt(b)
    # print("现在是第%-3d秒，x的值为%-3d，y的值为%-5d" % (i+1,x,y))
    
    print("%03d:%s"%(i+1,z * (abs(int(y)) % 150)))





