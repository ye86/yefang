# -*- coding: utf-8 -*-
"""
Created on Sat May  5 08:58:32 2018

@author: yefang
"""

'''
微信投票
http://www.2b.cn/vote/hundred/digg.php?id=452&from=groupmessage&isappinstalled=0
https://www.vzan.cc/vote/vdetail-63882?vuid=46645&auth_time=636611224191030807

'''
# 导入http请求库request
import requests
#导入随机数库
import random
import time
import sys
import re

# 谢邀云动态IP代理地址和端口号，如有需要可以联系微信：vista8购买


# 投票函数
def run():
    vote_url = 'https://www.vzan.cc/vote/vdetail-63882'
    headers = {}
    # 构造随机UA
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400" + str(random.randint(0,99))
    # Referer 地址
    headers['Referer'] = "https://www.vzan.cc/vote/vdetail-63882?vuid=46645&auth_time=636611224191030807"
    headers['Cookie'] = "828c03698c45964580b5f5cbce2ad577=452"

    # 超时设为3秒，如果网页3秒内无响应抛出异常
    timeout = 3
    # 构造Post请求发送的内容，id对应的文章id，from为微信群，isappinstalled也是微信群聊点击传的参数
    data = {
    'id': 452,
    'from': 'groupmessage',
    'isappinstalled': 0
    }

    try:
        res = requests.post(vote_url, data = data, headers = headers, proxies=proxies, timeout = 3)
        print(res.status_code)
    except:
        run()


run()
