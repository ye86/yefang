import requests

s = "你好"


def go(s=""):
    url = "http://www.weilaitec.com/Web/pythonServlet.py"
    my_key = "81be50639e618ae0903cb6439a6ac0b3"
    my_ip = "91.73.129.58"

    data = {
        "key":my_key,
        "msg":s,
        "ip":my_ip
    }
    
    r_ctn = requests.post(url,data=data)
    return r_ctn

while True:
	s = input("我：")
	print(go(s).text)
