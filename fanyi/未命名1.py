# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 08:08:06 2018

@author: yefang
"""
import requests
import json
import urllib

def fanyi(q = 'hello',fromLang = 'en',toLang = 'zh'):


    

    myurl = 'http://api.fanyi.baidu.com/#'    

    
    myurl = myurl+fromLang+'//'+toLang+'//'+urllib.parse.quote(q)
    
    

    r_ctn = requests.post(myurl)
    # a = r_ctn.json()['trans_result'][0]['dst']

    return r_ctn

b = True
while b:
    s = input("请输入要翻译的内容，按“0”退出：")
    if s == '0':
        b = False        
    else:
        c =fanyi(s)
        print(c)