# conding=utf-8
'''
@author: Jingcheng Xu
@software: PyCharm
@time: 2018/12/11
'''

import sys
import pandas as pd
from Import_Data_Func import *

datafiles = ['D:/Documents/PycharmProjects/宝钢/GUI_Coal_Base/原始数据.csv','D:/Documents/PycharmProjects/宝钢/GUI_Coal_Base/原始数据.xls','D:/Documents/PycharmProjects/宝钢/GUI_Coal_Base/原始数据.xlsx']
dfs = read_data(datafiles)
