# coding=utf-8

import sys,os,re
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox
from Import_Data import Ui_Import_Window    #导入“导入数据”窗口
from MainWindows import Ui_MainWindow       #导入程序主窗口窗口
from coal_index_dialog import Ui_coal_index_dialog      #导入“分煤种指标库”窗口
from base_coal_dialog import Ui_base_coal_dialog        #导入“基础煤种库”窗口
from classic_coal_dialog import Ui_classic_coal_dialog     #导入“经典煤种库”窗口
from new_coal_dialog import Ui_new_coal_dialog          #导入“新煤种库”窗口
from mine_info_dialog import Ui_mine_info_dialog        #导入“煤矿/矿山信息”窗口
from index_trend_dialog import Ui_index_trend_dialog    #导入“质量变化趋势”窗口
from Import_Data_Func import *      #导入数据的相关函数

### 导入数据的窗口界面 ###
class Import_Window(QtWidgets.QMainWindow,Ui_Import_Window):
    df_origin = pd.DataFrame
    df_mean = pd.DataFrame
    def __init__(self):
        super(Import_Window, self).__init__()
        self.setupUi(self)

    # 打开文件浏览窗口，选择数据文件
    def find_files(self):
        datafiles, filetype = QtWidgets.QFileDialog.getOpenFileNames(self, "浏览选取煤种数据文件", "./",filter='Excel Files(*.xlsx *.xls);;CSV Files(*.csv)')
        self.textEdit.setText('')
        if len(datafiles) > 0:
            # 文本框中显示要读取的文件
            self.textEdit.append('此次将读取以下数据文件:')
            for item in datafiles:
                self.textEdit.append(item)
            self.textEdit.append('\n开始读取原始数据文件:')
            dfs = read_data(self,datafiles)  #读取原始数据
            dfs = dfs.sort_values(by=['煤种', '煤名称', '年份'], ascending=[True, True, True])
            dfs = dfs.reset_index(drop=True)
            if '序号' in dfs.columns.tolist():
                del dfs['序号']
            dfs.to_csv('原始数据.csv', encoding='gb2312', index=0)
            self.textEdit.append('\n已读取原始数据\n请点击“打开主界面”按钮”')
            QMessageBox.warning(self, "打开主界面", "已读取原始数据\n请点击“打开主界面”按钮")

##### 追加读取数据，合并保存
    def append_load_files(self):
        # 如有，首先读取已有原始数据
        if os.path.exists('原始数据.csv'):
            self.textEdit.setText('')
            self.textEdit.append('首先读取已有原始数据.csv文件\n')
            old_file = open('原始数据.csv')
            old_dfs = pd.read_csv(old_file, encoding='utf-8')
        # 打开浏览窗口，获取要追加读取的文件
        datafiles, filetype = QtWidgets.QFileDialog.getOpenFileNames(self, "浏览选取要追加的煤种数据文件", "./",filter='Excel Files(*.xlsx *.xls);;CSV Files(*.csv)')
        if len(datafiles) > 0:
            # 文本框中显示要读取的文件
            self.textEdit.append('计划追加读取以下数据文件:')
            for item in datafiles:
                self.textEdit.append(item)
            self.textEdit.append('\n开始追加读取原始数据文件:')
            new_dfs = read_data(self,datafiles)  #读取原始数据
        # 合并新老数据文件
        if not (old_dfs.empty):
            dfs = pd.concat([old_dfs,new_dfs], ignore_index=True, sort=False)
        else:
            dfs = new_dfs
        dfs = dfs.sort_values(by=['煤种','煤名称','年份'], ascending=[True,True,True])
        dfs = dfs.reset_index(drop=True)
        if '序号' in dfs.columns.tolist():
            del dfs['序号']
        dfs.to_csv('原始数据.csv', encoding='gb2312', index=0)
        self.textEdit.append('\n已追加读取原始数据\n请点击“打开主界面”按钮”')
        QMessageBox.warning(self, "打开主界面", "已追加读取原始数据\n请点击“打开主界面”按钮")



    # 打开程序主界面
    def openmain(self):
        if os.path.exists('原始数据.csv'):# and os.path.exists('年均数据.csv') :
            MainWindow.show()       #打开主窗口
            ImportWindow.close()    #关闭数据导入窗口
        else:
            print('缺少原始数据csv文件,请先导入数据!')
            QMessageBox.warning(self, "缺少原始数据", "缺少原始数据csv文件,请先导入数据!")
            exit()
            #if os.path.exists('原始数据.csv'): QMessageBox.warning(self, "缺少数据文件", "缺少年均数据.csv文件!")
            #elif os.path.exists('年均数据.csv'): QMessageBox.warning(self, "缺少数据文件", "缺少原始数据.csv文件!")
            #else: QMessageBox.warning(self, "缺少数据文件", "缺少原始数据.csv文件和年均数据.csv文件!")

### 读取程序保存的数据文件
#class Read_CSVData():
#    if os.path.exists('原始数据.csv'):
#        file_origin = open('原始数据.csv')
#        df_origin = pd.read_csv(file_origin, encoding='utf-8')
    #if os.path.exists('时间段分级数据.csv'):
    #    file_regionmean = open('时间段分级数据.csv')
    #    df_regionmean = pd.read_csv(file_regionmean, encoding='utf-8')
    #if os.path.exists('年均数据.csv'):
    #    file_yearmean = open('年均数据.csv')
    #    df_yearmean = pd.read_csv(file_yearmean, encoding='utf-8')
    #if os.path.exists('基础煤种时间段分级数据.csv'):
    #    file_base = open('基础煤种时间段分级数据.csv')
    #    df_base = pd.read_csv(file_base, encoding='utf-8')
    #if os.path.exists('经典煤种数据.csv'):
    #    file_classic = open('经典煤种数据.csv')
    #    df_classic = pd.read_csv(file_classic, encoding='utf-8')
    #if os.path.exists('新煤种数据.csv'):
    #    file_new = open('新煤种数据.csv')
    #    df_new = pd.read_csv(file_new, encoding='utf-8')

### 数据库程序的主界面 ###
class Main_Window(QtWidgets.QMainWindow,Ui_MainWindow):
    #print(Read_CSVData.df_mean)
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)

### 分品种煤质指标数据窗口 ###
class Coal_Index_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_coal_index_dialog()
        self.child.setupUi(self)
    # 根据已选下拉列表筛选并显示数据
    def screening_btn_click(self):
        # 获取分品种分时间段煤种数据
        if os.path.exists('原始数据.csv'):
            file_origin = open('原始数据.csv')
            df_origin = pd.read_csv(file_origin, encoding='utf-8')
        else:
            print('缺少原始数据csv文件,请先导入数据！')
            exit()
        #df_origin = Read_CSVData.df_origin
        df_yearregion = mean_by_yearregion(df_origin)
        df = init_level(df_yearregion)  # 5个指标分级
        #print(df)
        df.to_csv('时间段分级数据.csv', encoding='gb2312', index=0)
        #coal_Place = self.child.comboBox_1.currentText()
        coal_Kind = self.child.comboBox_2.currentText()
        coal_Year = self.child.comboBox_3.currentText()
        coal_Quality = self.child.comboBox_4.currentText()
        coal_HotStr = self.child.comboBox_5.currentText()
        coal_Hard = self.child.comboBox_6.currentText()
        coal_Ash = self.child.comboBox_7.currentText()
        coal_Std = self.child.comboBox_8.currentText()
        # 根据下拉列表截取数据
        #df = self.df_yearregion
        if (not coal_Kind == '所有'): df = df[df.煤种 == coal_Kind]
        if (not coal_Year == '所有'): df = df[df.年份 == coal_Year]
        if (not coal_Quality == '所有'): df = df[df.煤质分级 == coal_Quality]
        if (not coal_HotStr == '所有'): df = df[df.热强度分级 == coal_HotStr]
        if (not coal_Hard == '所有'): df = df[df.硬煤分类 == coal_Hard]
        if (not coal_Ash == '所有'): df = df[df.灰分分级 == coal_Ash]
        if (not coal_Std == '所有'): df = df[df.硫分分级 == coal_Std]
        df = df.reset_index(drop=True)
        self.child.label_num.setText('共计%d条数据.' % len(df))
        # 表格行数、列标题设置
        self.child.result_table.setRowCount(len(df))
        table_header = ['年份','国家','煤种','产地','煤名称','煤质分级','热强度分级','硬煤分类','Ad','灰分分级','Std','硫分分级','Vd','CRI','CSR','lgMF','TD','DI150_15','M40_M10','Y','X','G','Rr','TI','Pd','K2O_Na2O','内水分','粒级分布','元素分析','堆密度','灰成分','发热量','全水分']        #df.columns.values.tolist()
        self.child.result_table.setColumnCount(len(table_header))
        self.child.result_table.setHorizontalHeaderLabels(table_header)
        # 表格内容填充
        for index,row in df.iterrows():
            for j in range(len(table_header)):
                #inputitem = str(row[table_header[j]])
                itemvalue = str(row[table_header[j]])
                inputitem = numformat(itemvalue)
                newItem = QtWidgets.QTableWidgetItem(inputitem)
                newItem.setTextAlignment(0x0004|0x0080)   #水平/垂直居中
                self.child.result_table.setItem(index,j,newItem)
        # 表格格式设置
        self.child.result_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  #选中一行
        self.child.result_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents) #自适应调整列宽

### 基础煤种指标数据窗口 ###
class Base_Coal_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_base_coal_dialog()
        self.child.setupUi(self)
    # 根据已选下拉列表筛选并显示数据
    def screening_btn_click(self):
        # 获取基础煤种数据
        if os.path.exists('原始数据.csv'):
            file_origin = open('原始数据.csv')
            df_origin = pd.read_csv(file_origin, encoding='utf-8')
        else:
            print('缺少原始数据csv文件,请先导入数据！')
            exit()
        #df_origin = Read_CSVData.df_origin
        base_dfs = get_Base_coal(df_origin)  # 获取基础煤种数据
        if (base_dfs.empty):
            self.child.label_num.setText('无基础煤种!')
            QMessageBox.warning(self, "无基础煤种", "当前数据中未筛选出基础煤种数据!")
        else:
            base_dfs = mean_by_yearregion(base_dfs)
            df = init_level(base_dfs)  # 5个指标分级
            df.to_csv('基础煤种时间段分级数据.csv', encoding='gb2312', index=0)
            # 根据下拉列表中的数值筛选数据
            #coal_Place = self.child.comboBox_1.currentText()
            coal_Kind = self.child.comboBox_2.currentText()
            coal_Year = self.child.comboBox_3.currentText()
            coal_Quality = self.child.comboBox_4.currentText()
            coal_HotStr = self.child.comboBox_5.currentText()
            coal_Hard = self.child.comboBox_6.currentText()
            coal_Ash = self.child.comboBox_7.currentText()
            coal_Std = self.child.comboBox_8.currentText()
            #df = Read_CSVData.df_base
            if (not coal_Kind == '所有'): df = df[df.煤种 == coal_Kind]
            if (not coal_Year == '所有'): df = df[df.年份 == coal_Year]
            if (not coal_Quality == '所有'): df = df[df.煤质分级 == coal_Quality]
            if (not coal_HotStr == '所有'): df = df[df.热强度分级 == coal_HotStr]
            if (not coal_Hard == '所有'): df = df[df.硬煤分类 == coal_Hard]
            if (not coal_Ash == '所有'): df = df[df.灰分分级 == coal_Ash]
            if (not coal_Std == '所有'): df = df[df.硫分分级 == coal_Std]
            df = df.reset_index(drop=True)
            self.child.label_num.setText('共计%d条数据.' % len(df))
            # 表格行数、列标题设置
            self.child.result_table.setRowCount(len(df))
            table_header = ['年份','国家','煤种','产地','煤名称','入选原因','煤质分级','热强度分级','硬煤分类','Ad','灰分分级','Std','硫分分级','Vd','CRI','CSR','lgMF','TD','DI150_15','M40_M10','Y','X','G','Rr','TI','Pd','K2O_Na2O','内水分','粒级分布','元素分析','堆密度','灰成分','发热量','全水分']        #df.columns.values.tolist()
            self.child.result_table.setColumnCount(len(table_header))
            self.child.result_table.setHorizontalHeaderLabels(table_header)
            # 表格内容填充
            for index,row in df.iterrows():
                for j in range(len(table_header)):
                    itemvalue = str(row[table_header[j]])
                    inputitem = numformat(itemvalue)
                    newItem = QtWidgets.QTableWidgetItem(inputitem)
                    newItem.setTextAlignment(0x0004|0x0080)   #水平/垂直居中
                    self.child.result_table.setItem(index,j,newItem)
            # 表格格式设置
            self.child.result_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  #选中一行
            self.child.result_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents) #自适应调整列宽

### 经典煤种指标数据窗口 ###
class Classic_Coal_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_classic_coal_dialog()
        self.child.setupUi(self)
    # 根据已选下拉列表筛选并显示数据
    def screening_btn_click(self):
        ## 获取经典煤种数据
        if os.path.exists('原始数据.csv'):
            file_origin = open('原始数据.csv')
            df_origin = pd.read_csv(file_origin, encoding='utf-8')
        else:
            print('缺少原始数据csv文件,请先导入数据！')
            exit()
        #df_origin = Read_CSVData.df_origin
        yeardfs = mean_by_year(df_origin)
        yeardfs = init_level(yeardfs)
        #allyearregiondfs = mean_by_yearregion(df_origin)
        #allyearregiondfs = init_level(allyearregiondfs)   #5个指标分级
        df = get_Classic_coal(yeardfs)  # 获取经典煤种数据
        if (df.empty):
            self.child.label_num.setText('无经典煤种!')
            QMessageBox.warning(self, "无经典煤种", "当前数据中未筛选出经典煤种数据!")
        else:
            df.to_csv('经典煤种数据.csv', encoding='gb2312', index=0)
            # 根据下拉列表中的数值筛选数据
            #coal_Place = self.child.comboBox_1.currentText()
            coal_Kind = self.child.comboBox_2.currentText()
            coal_Year = self.child.comboBox_3.currentText()
            coal_Quality = self.child.comboBox_8.currentText()
            coal_HotStr = self.child.comboBox_4.currentText()
            coal_Hard = self.child.comboBox_5.currentText()
            coal_Ash = self.child.comboBox_6.currentText()
            coal_Std = self.child.comboBox_7.currentText()
            #df = Read_CSVData.df_classic
            if (not coal_Kind == '所有'): df = df[df.煤种 == coal_Kind]
            if (not coal_Year == '所有'): df = df[df.年份 == coal_Year]
            if (not coal_Quality == '所有'): df = df[df.煤质分级 == coal_Quality]
            if (not coal_HotStr == '所有'): df = df[df.热强度分级 == coal_HotStr]
            if (not coal_Hard == '所有'): df = df[df.硬煤分类 == coal_Hard]
            if (not coal_Ash == '所有'): df = df[df.灰分分级 == coal_Ash]
            if (not coal_Std == '所有'): df = df[df.硫分分级 == coal_Std]
            df = df.reset_index(drop=True)
            self.child.label_num.setText('共计%d条数据.' % len(df))
            # 表格行数、列标题设置
            self.child.result_table.setRowCount(len(df))
            table_header = ['年份','国家','煤种','产地','煤名称','入选原因','煤质分级','热强度分级','硬煤分类','Ad','灰分分级','Std','硫分分级','Vd','CRI','CSR','lgMF','TD','DI150_15','M40_M10','Y','X','G','Rr','TI','Pd','K2O_Na2O','内水分','粒级分布','元素分析','堆密度','灰成分','发热量','全水分']        #df.columns.values.tolist()
            self.child.result_table.setColumnCount(len(table_header))
            self.child.result_table.setHorizontalHeaderLabels(table_header)
            # 表格内容填充
            for index,row in df.iterrows():
                for j in range(len(table_header)):
                    itemvalue = str(row[table_header[j]])
                    inputitem = numformat(itemvalue)
                    newItem = QtWidgets.QTableWidgetItem(inputitem)
                    newItem.setTextAlignment(0x0004|0x0080)   #水平/垂直居中
                    self.child.result_table.setItem(index,j,newItem)
            # 表格格式设置
            self.child.result_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  #选中一行
            self.child.result_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents) #自适应调整列宽


### 新煤种指标数据窗口 ###
class New_Coal_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_new_coal_dialog()
        self.child.setupUi(self)
    # 根据已选下拉列表筛选并显示数据
    def screening_btn_click(self):
        ## 获取新煤种数据
        if os.path.exists('原始数据.csv'):
            file_origin = open('原始数据.csv')
            df_origin = pd.read_csv(file_origin, encoding='utf-8')
        else:
            print('缺少原始数据csv文件,请先导入数据！')
            exit()
        #df_origin = Read_CSVData.df_origin
        new_dfs = get_New_coal(df_origin)  # 获取新煤种数据
        if (new_dfs.empty):
            self.child.label_num.setText('无新煤种!')
            QMessageBox.warning(self, "无新煤种", "当前数据中未筛选出新煤种数据!")
        else:
            df = init_level(new_dfs)  # 5个指标分级
            df.to_csv('新煤种数据.csv', encoding='gb2312', index=0)
            #coal_Place = self.child.comboBox_1.currentText()
            coal_Kind = self.child.comboBox_2.currentText()
            coal_Year = self.child.comboBox_3.currentText()
            coal_Quality = self.child.comboBox_8.currentText()
            coal_HotStr = self.child.comboBox_4.currentText()
            coal_Hard = self.child.comboBox_5.currentText()
            coal_Ash = self.child.comboBox_6.currentText()
            coal_Std = self.child.comboBox_7.currentText()
            # 根据下拉列表中的数值筛选数据
            #df = Read_CSVData.df_new
            if (not coal_Kind == '所有'): df = df[df.煤种 == coal_Kind]
            if (not coal_Year == '所有'): df = df[df.年份 == coal_Year]
            if (not coal_Quality == '所有'): df = df[df.煤质分级 == coal_Quality]
            if (not coal_HotStr == '所有'): df = df[df.热强度分级 == coal_HotStr]
            if (not coal_Hard == '所有'): df = df[df.硬煤分类 == coal_Hard]
            if (not coal_Ash == '所有'): df = df[df.灰分分级 == coal_Ash]
            if (not coal_Std == '所有'): df = df[df.硫分分级 == coal_Std]
            df = df.reset_index(drop=True)
            self.child.label_num.setText('共计%d条数据.' % len(df))
            # 表格行数、列标题设置
            self.child.result_table.setRowCount(len(df))
            table_header = ['年份','国家','煤种','产地','煤名称','煤质分级','热强度分级','硬煤分类','Ad','灰分分级','Std','硫分分级','Vd','CRI','CSR','lgMF','TD','DI150_15','M40_M10','Y','X','G','Rr','TI','Pd','K2O_Na2O','内水分','粒级分布','元素分析','堆密度','灰成分','发热量','全水分']        #df.columns.values.tolist()
            self.child.result_table.setColumnCount(len(table_header))
            self.child.result_table.setHorizontalHeaderLabels(table_header)
            # 表格内容填充
            for index,row in df.iterrows():
                for j in range(len(table_header)):
                    itemvalue = str(row[table_header[j]])
                    inputitem = numformat(itemvalue)
                    newItem = QtWidgets.QTableWidgetItem(inputitem)
                    newItem.setTextAlignment(0x0004|0x0080)   #水平/垂直居中
                    self.child.result_table.setItem(index,j,newItem)
            # 表格格式设置
            self.child.result_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  #选中一行
            self.child.result_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents) #自适应调整列宽

### 煤矿/矿山信息窗口 ###
class Mine_Info_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_mine_info_dialog()
        self.child.setupUi(self)

### 煤种指标质量变化趋势窗口 ###
class Index_Trend_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_index_trend_dialog()
        self.child.setupUi(self)

    def screening_btn_click(self):
        # 获取分时间质量变化数据
        if os.path.exists('原始数据.csv'):
            file_origin = open('原始数据.csv')
            df_origin = pd.read_csv(file_origin, encoding='utf-8')
        else:
            print('缺少原始数据csv文件,请先导入数据！')
            exit()
        #df_origin = Read_CSVData.df_origin
        df_3years = df_origin[df_origin.年份 >= 2016]
        if not (df_3years.empty):
            df_3years = mean_by_year(df_3years)
        df_yearregion = df_origin[df_origin.年份 <2016]
        if not (df_yearregion.empty):
            df_yearregion = mean_by_yearregion(df_yearregion)
        if (not (df_3years.empty)) and (not (df_yearregion.empty)):
            df = pd.concat([df_yearregion,df_3years],ignore_index=True,sort=False)
        elif (df_3years.empty) and (df_yearregion.empty):
            print('无数据！')
        elif (df_3years.empty):
            df = df_yearregion
        elif (df_yearregion.empty):
            df = df_3years
        if not (df.empty):
            df.to_csv('质量变化趋势.csv', encoding='gb2312', index=0)
            # 根据下拉列表中的数值筛选数据
            coal_Kind = self.child.comboBox_2.currentText()
            df = df[df.煤种 == coal_Kind]
            xlocs = df.index.tolist()
            xlabels = []
            for item in df['年份'].tolist():
                xlabels.append(str(item))
            # 绘图
            maincols = ['CRI', 'CSR', 'DI150_15','Y','G', 'TD', 'lgMF','Ad', 'Std', 'Vd', 'Pd', 'K2O_Na2O']
            plt.rcParams['font.sans-serif'] = ['SimHei']
            fig = plt.figure(figsize=(16,16))
            fig.suptitle(coal_Kind+'各主要指标质量变化趋势')#, fontsize=18)
            for i in range(len(maincols)):
                specificY = df[df.年份 == '1999-2002'].loc[1,maincols[i]]
                ax = plt.subplot(3, 4, i+1)     # 设置子图位置。总从3行，4列。从上往下，从左往右，第i+1个子图
                ax.set_xlabel('时间段/年份')     # 设置X轴标题
                ax.set_ylabel(maincols[i])      # 设置Y轴标题
                plt.xticks(xlocs,xlabels,rotation=90)       # 设置X轴刻度文本
                plt.plot(df.index,df[maincols[i]],linestyle='dashed', marker='o',label=maincols[i],zorder=1)
                plt.scatter(1,specificY, label='1999-2002年间数据',s=100, marker='p', color='red',zorder=2)
                ax.legend(loc='lower right')  # 设置图例，自动选择位置
            plt.subplots_adjust(wspace=0.3, hspace=0.8)     # 调整子图间的间距
            plt.show()

    ######## Slot functions #############

    #def slot_major(self):
    #    print()
    #    price=self.price_box.toPlainText()
    #    self.results_window.setText("hi,PyQt5~")
    #    rate = self.tax_rate.value()
    #    self.results_window.setText(price*rate)
    #    self.label.text(price*rate)
    ######################################


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ImportWindow = Import_Window()
    MainWindow = Main_Window()
    CoalIndexWindow = Coal_Index_Window()
    BaseCoalWindow = Base_Coal_Window()
    ClassicCoalWindow = Classic_Coal_Window()
    NewCoalWindow = New_Coal_Window()
    MineInfoWindow = Mine_Info_Window()
    IndexTrendWindow = Index_Trend_Window()
    MainWindow.coal_index.clicked.connect(CoalIndexWindow.show)
    MainWindow.base_coal.clicked.connect(BaseCoalWindow.show)
    MainWindow.classic_coal.clicked.connect(ClassicCoalWindow.show)
    MainWindow.new_coal.clicked.connect(NewCoalWindow.show)
    MainWindow.mine_info.clicked.connect(MineInfoWindow.show)
    MainWindow.index_trend.clicked.connect(IndexTrendWindow.show)

    ImportWindow.show()     #程序启动默认显示“导入数据”窗口

    sys.exit(app.exec_())