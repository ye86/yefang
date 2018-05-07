#/usr/bin/env python
#coding=utf8
 
import http.client
import hashlib
import urllib
import random

appid = '20180323000139297'
secretKey = 'GF_SG7lkFdIjfL1TFGYz'

 
httpClient = None
myurl = '/api/trans/vip/translate'
q = 'apple'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
m1 = hashlib.md5()
m1.update(sign.encode("utf8"))
sign = m1.hexdigest()
myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign






try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
 
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print('response.status = %s' % response.status)
    print('response.reason = %s' % response.reason)
    print('response.getheaders() = %s' % response.getheaders())
    print('response.read() = %s' % response.read())
    print('response.status = %s' % response.status)
    a=str(response.read(), "utf-8")
    print(a)
except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()
