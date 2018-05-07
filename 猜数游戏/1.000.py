import random

secret = random.randint(1,10)

temp = input("请输入您猜的数值：")
gress = int(temp)
while gress != secret:

    temp = input("请输入您猜的数值：")
    gress = int(temp)

    if gress == secret:
        print("你是我肚子里的虫虫吗？这都被你猜中了")
        print('猜对了也没奖励！')
    else:
        print("猜错了~哈哈")
