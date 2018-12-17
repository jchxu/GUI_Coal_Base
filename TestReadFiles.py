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
datafiles = ['原始数据.xlsx']
dfs = read_data(datafiles)
dfs = mean_by_year(dfs)
dfs = init_level(dfs)

print(dfs)