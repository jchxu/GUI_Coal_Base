# conding=utf-8
'''
@author: Jingcheng Xu
@software: PyCharm
@time: 2018/12/11
'''

import sys
import pandas as pd
from Import_Data_Func import *

pd.set_option('display.max_columns', None)

#datafiles = ['D:/PycharmProjects/宝钢/GUI_Coal_Base/原始数据.csv','D:/PycharmProjects/宝钢/GUI_Coal_Base/原始数据.xls','D:/PycharmProjects/宝钢/GUI_Coal_Base/原始数据.xlsx']
datafiles = ['原始数据.xlsx','原始数据 - 副本.xlsx']
dfs = read_data(datafiles)
dfs.to_csv('原始数据.csv',encoding="utf_8_sig",index=0)
dfs = mean_by_year(dfs)
dfs = init_level(dfs)
dfs.to_csv('年平均分级数据.csv',encoding="utf_8_sig",index=0)


print(dfs)