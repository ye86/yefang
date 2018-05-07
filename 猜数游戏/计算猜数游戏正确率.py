import 猜数游戏.py

正确=0
for i in range(1,1000):
    正确 += 猜数游戏.server()
print("猜对次数为：" + str(正确))
