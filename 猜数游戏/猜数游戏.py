# 客户端：
def client(次数,状态,猜数):
    if 次数 == 0 and 状态 == 0:
        return random.randint(n1,n2) 
    else:
        if 状态 > 0:
            return random.randint(n1,猜数-1) 
        else:
            return random.randint(猜数+1,n2) 

# 服务器端
def server():
    gress = -1
    now_try = 0
    大小=0
    while gress != secret and now_try < max_try:
        # print("你有%d次机会！"%(max_try - now_try))
        # print("请输入%d-%d之间的数字:" %(n1,n2))
        temp = client(次数=now_try,状态=大小,猜数=gress)
        gress = int(temp)
        # print("你输入的数字是：" + str(gress))

        if gress > secret:
            # print("大了，大了\n应该猜小一点的！")
            大小 = 1
        if gress < secret:
            # print("小了，小了\n应该猜大一点的！")
            大小 = -1
            now_try = now_try +1
    if gress == secret:
        # print("你是我肚子里的虫虫吗？\n这都被你猜中了！")
        return 1
    else:
        # print("你没机会了！")
        return 0
    # print("答案是：" + str(secret))
    # print("不玩了，不玩了，拜拜~！")
import random
n1 = 0
n2 = 9
secret = random.randint(n1,n2)
max_try = 3


