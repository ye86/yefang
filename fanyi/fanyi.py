# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:41:38 2018

@author: yefang
"""

import requests
import urllib
import random
import hashlib
from tkinter import *   





def fanyi(q = 'hello',fromLang = 'auto',toLang = 'zh'):
    if '\u4e00' <= q <= '\u9fff':
        toLang = 'en'
        

    appid = '20180323000139297'
    secretKey = 'GF_SG7lkFdIjfL1TFGYz'
    

    myurl = '/api/trans/vip/translate'
    
    
    salt = random.randint(32768, 65536)
    
    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode("utf8"))
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    
    
    myurl = "http://api.fanyi.baidu.com" + myurl
    r_ctn = requests.post(myurl)
    a = r_ctn.json()['trans_result'][0]['dst']

    return a


while True:
    s = input("请输入要翻译的内容（按“q”键退出）：")
    if s != 'q':
        print(fanyi(s))       
    else:
        break

