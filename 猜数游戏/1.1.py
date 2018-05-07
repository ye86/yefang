import random

secret = random.randint(0,9)
gress = secret - 1
max_try = 3
now_try = 0
while gress != secret and now_try < max_try:
    print("你有%d次机会！"%(max_try - now_try))
    temp = input("请输入你要猜的数值（0-9）：")
    gress = int(temp)

    if gress > secret:
        print("大了，大了\n应该猜小一点的！")
    if gress < secret:
        print("小了，小了\n应该猜大一点的！")
    now_try = now_try +1
if gress == secret:
    print("你是我肚子里的虫虫吗？\n这都被你猜中了！")
else:
    print("你没机会了！")
print("答案是：" + str(secret))
print("不玩了，不玩了，拜拜~！")
