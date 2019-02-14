# conding=utf-8
'''
@author: Jingcheng Xu
@software: PyCharm
@time: 2018/12/11
'''

import sys,os
import pandas as pd
from Import_Data_Func_fortest import *

pd.set_option('display.max_columns', None)

#datafiles = ['D:/PycharmProjects/宝钢/GUI_Coal_Base/原始数据.csv','D:/PycharmProjects/宝钢/GUI_Coal_Base/原始数据.xls','D:/PycharmProjects/宝钢/GUI_Coal_Base/原始数据.xlsx']
#datafiles = ['原始数据.xlsx','原始数据-2.xlsx']
datafiles = ['原始数据.xlsx']

#if (not os.path.exists('原始数据.csv')) and (not os.path.exists('年平均分级数据.csv')):
dfs = read_data(datafiles)
#dfs.to_csv('原始数据.csv',encoding='gb2312',index=0)
base_dfs = get_Base_coal(dfs)
#dfs = mean_by_year(dfs)
#dfs = init_level(dfs)
#dfs.to_csv('年平均分级数据.csv',encoding='gb2312',index=0)
#file_origin = open('原始数据.csv')
#file_mean = open('年平均分级数据.csv')
#df_origin = pd.read_csv(file_origin,encoding='utf-8')
#df_mean = pd.read_csv(file_mean,encoding='utf-8')

print(base_dfs)


