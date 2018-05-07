import os
 
print ("\n欢迎大家跟我一起学Python")
 
system=os.name                                                            #获取系统的类型
if(system=="nt"):
    print ("您使用的操作系统是windows")
    print ("使用windows表示的特定路径分割符是 "+os.sep)               #获取系统的分隔符
    print ("您的电脑系统的终止符效果"+os.linesep)                     #获取系统换行符
else:
    print ("您使用的操作系统是Linux")
    print ("使用windows表示的特定路径分割符是 "+os.sep)
    print ("您的电脑系统的终止符是"+os.linesep)
 
path=os.getcwd()                                                       #获得当前目录
print ("您运行本程序所在目录是 "+path)
 
print ("你电脑的Path环境变量为 "+os.getenv("Path"))                        #获取环境变量的值os.putenv(key,value)可以设置环境变量的值
 
print ("你当前文件夹中的文件有：")
print (os.listdir(path))                                                       #获取文件夹中的所有文件
if(os.path.exists("test.txt")):                                                #判断文件是否存在
    os.remove("test.txt")                                                #删除指定文件
    print ("\n删除成功")
else:
    print ("\n文件不存在")
print ("咱们来删除一个文件，删除后的结果：")
print (os.listdir(path))                                
 
# print ("\n查看您的ip：\n")
# ip = os.system("ipconfig")
# print (ip)                                               #执行系统命令
 
filepath1="C:\\Python27"
filepath2="C:\\Python27os.py"
 
if(os.path.isfile(filepath2)):                                                #判断是不是文件
    print (filepath2 + "是一个文件")
else:
    print (filepath2 + "不是一个文件")
if(os.path.isfile(filepath1)):
    print (filepath1 + "是一个文件")
else:
    print (filepath1 + "不是一个文件\n")
 
name=os.path.basename(__file__)
print ("本程序的大小为:")
print (os.path.getsize(name))                                                #获取文件大小
name=os.path.abspath(name)                                                 #获取文件的绝对路径
print ("\n本程序的绝对路径是:\n"+name)                
 
 
print ("\n本程序的路径的文件名分别为：")
print (os.path.split(name))                                               #将文件名和路径分开
 
files=os.path.splitext(name)                                              #将文件名和扩展分开
print ("\n本程序的扩展为:\n"+files[1])
 
print ("\n本程序的文件名为:\n"+os.path.basename(name))   #获取文件的名字
 
print ("\n本程序的路径为:\n"+os.path.dirname(name))     #获取文件的路径
