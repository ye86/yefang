# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:01:56 2018

@author: yefang
"""


def 考勤表转换(filename,new_="new_"):    
    import xlrd     # xlrd主要是用来读取excel文件,导入模块
    
     
    data = xlrd.open_workbook(filename)  # 打开Excel文件读取数据
    
    #   获取EXCEL中第一个工作表
    table = data.sheets()[0]          #通过索引顺序获取
    
    
    姓名 = table.col_values(1, start_rowx=0, end_rowx=None)  # 读取姓名列
    
    
    日期时间 = table.col_values(3, start_rowx=0, end_rowx=None) # 读取时间列
    
    总行数 = table.nrows  #获取总行数
    
    人数 = len(list(set(姓名)))
    
    
    # 逐条分析打卡时间,分配到newxls(人数,31)
    
    newxls=[[0 for col in range(32)] for row in range(人数)]  #生成二维列表
    
    # 初使化列表,全部填空
    newxls[0][0]="姓名"
    for i in range(1,32):
        newxls[0][i]=(str(i) + "号")
        for j in range(1,人数):
            newxls[j][i] = ""
    
    
    
    
    
    import datetime
    d0 = datetime.date(1900,1,1)
    日期时间[0] = int(日期时间[1]) -1
    d1 = d0 + datetime.timedelta(days=int(日期时间[0]))
    
    行数 = 0
    列数 = 1
    
    for nrows_i in range(1,总行数):
        # 获得写入行数
        if 姓名[nrows_i] != 姓名[nrows_i-1]:
            行数 += 1
            newxls[行数][0]=姓名[nrows_i]  #  写入姓名列
    
        # 获得写入列数
        d1 = d0 + datetime.timedelta(days=int(日期时间[nrows_i]-2))
        列数 = d1.day
        # 获得写入数据
        if 姓名[nrows_i] != 姓名[nrows_i-1] or 日期时间[nrows_i] - 日期时间[nrows_i-1] >= 0.007:   #  当姓名与上一行不一致，或者 时间与上一行相差大于10分钟，触发写入
            打卡时间=日期时间[nrows_i] - int(日期时间[nrows_i])
            打卡小时=int(打卡时间*24)
            打卡分钟=int(打卡时间*24*60)-打卡小时*60
    #        if len(打卡分钟) == 1:
    #            打卡分钟 = "0"+str(打卡分钟)
            if newxls[行数][列数]=="":
                newxls[行数][列数] += ('%02d:%02d'% (打卡小时,打卡分钟))  #写入不换行的打卡时间
            else:
                newxls[行数][列数] += ('\n%02d:%02d'% (打卡小时,打卡分钟))  #写入换行的打卡时间
            
            
    # 写入xls
    import xlwt
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    #样式设置
    #设置列宽
    for colnum in range(1,32):
        sheet1.col(colnum).width = 256*7   # 设置1-31列的宽度为7个字符
    #新建alignment：
    alignment = xlwt.Alignment()
    
    # 设置行居中，
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    
    # 设置列居中，alignment.vert = xlwt.Alignment.VERT_CENTER
    
    # 设置自动换行，
    
    alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
    
    #新建font，font = xlwt.Font()
    
    #字体加粗，font.bold = True
    
    #设置字体大小，font.height = 12 * 20，12号的字体
    
    #设置为宋体，font.name = "SimSun"
    
    #新建borders，borders = xlwt.Borders()
    
    #设置表格宽度，borders.left = xlwt.Borders.THIN
    
    #新建style，
    style = xlwt.XFStyle()
    
    #为style设置alignment，
    style.alignment = alignment
    
    #为style设置font，style.font = font
    
    #为style设置borders，style.borders = borders
    
    #向sheet页中写入数据
    
    for i in range(人数):
        for j in range(32):
            sheet1.write(i,j,newxls[i][j],style)    
            
    
    workbook.save(new_+filename)
            
            
            
if __name__ == "__main__":
    考勤表转换('1.xls')  
    
            
            