# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:21:30 2018

@author: yefang
"""

filename = "1.xls"

# xlrd主要是用来读取excel文件,导入模块
import xlrd
'''
#打开Excel文件读取数据
    data = xlrd.open_workbook(filename)
#        excel中最重要的方法就是book和sheet的操作。
#   1）获取book中一个工作表
        table = data.sheets()[0]          #通过索引顺序获取
        table = data.sheet_by_index(sheet_indx)) #通过索引顺序获取
        table = data.sheet_by_name(sheet_name)#通过名称获取

# 以上三个函数都会返回一个xlrd.sheet.Sheet()对象

    names = data.sheet_names()    #返回book中所有工作表的名字

data.sheet_loaded(sheet_name or indx)   # 检查某个sheet是否导入完毕
#    2）行的操作

         nrows = table.nrows  #获取该sheet中的有效行数

         table.row(rowx)  #返回由该行中所有的单元格对象组成的列表

         table.row_slice(rowx)  #返回由该列中所有的单元格对象组成的列表

         table.row_types(rowx, start_colx=0, end_colx=None)    #返回由该行中所有单元格的数据类型组成的列表

         table.row_values(rowx, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表

         table.row_len(rowx) #返回该列的有效单元格长度
         
        3）列(colnum)的操作
         ncols = table.ncols   #获取列表的有效列数

         table.col(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表

         table.col_slice(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表

         table.col_types(colx, start_rowx=0, end_rowx=None)    #返回由该列中所有单元格的数据类型组成的列表

         table.col_values(colx, start_rowx=0, end_rowx=None)   #返回由该列中所有单元格的数据组成的列表
        
         4）单元格的操作
         table.cell(rowx,colx)   #返回单元格对象

         table.cell_type(rowx,colx)    #返回单元格中的数据类型

         table.cell_value(rowx,colx)   #返回单元格中的数据

         table.cell_xf_index(rowx, colx)   # 暂时还没有搞懂
'''