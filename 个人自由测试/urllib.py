from urllib import request 

host = "https://www.baidu.com"
my_paper = request.Request(host)
my_paper.add_header("Content-Type","application/json; charset=utf-8")
his_reply = request.urlopen(my_paper).read().decode("utf-8")
if his_reply:
    print(his_reply)
