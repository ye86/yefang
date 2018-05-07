# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:41:38 2018

@author: yefang
"""

import requests
import urllib
import random
import hashlib
import tkinter as tk





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
def b1click():
    global var
    s1 = text1.get(1.0,tk.END)
    s2 = s1.split('\n')
    s3 = ''
    for i in s2:
        if i != "":
            s3 += str(fanyi(i))
            s3 += '\n'
       
    
    text2.delete(1.0,tk.END)
    text2.insert(1.0,s3)
    

window = tk.Tk()
window.title('翻译脚本-叶方')
window.geometry('500x200')
l1 = tk.Label(window,text='百度翻译API',bg='Gainsboro',font=('Arial',8),width=15,height=1)
l1.pack()



text1 = tk.Text(window,width=60,height=5,)
text1.pack()
text2 = tk.Text(window,width=60,height=5)
text2.pack()

b1 = tk.Button(window,text='翻译',width=15,height=1,command=b1click)
b1.pack()



window.mainloop()


