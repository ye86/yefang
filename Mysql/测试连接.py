import pymysql
  
# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='yefang', charset='utf8')
# 创建游标
cursor = conn.cursor()
  
# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from yefang")

print(effect_row) 
# 执行SQL，并返回受影响行数
#effect_row = cursor.execute("update yefang set pass = '123' where nid = %s", (11,))
  
# 执行SQL，并返回受影响行数,执行多次
#effect_row = cursor.executemany("insert into yefang(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])
  
  
# 提交，不然无法保存新建或者修改的数据
conn.commit()
  
# 关闭游标
cursor.close()
# 关闭连接
conn.close()

