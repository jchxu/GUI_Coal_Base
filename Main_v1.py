# coding=utf-8

import sys
import pandas as pd
from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import QDialog
from Import_Data import Ui_Import_Window    #导入“导入数据”窗口
from MainWindows import Ui_MainWindow       #导入程序主窗口窗口
from coal_index_dialog import Ui_coal_index_dialog      #导入“分煤种指标库”窗口
from base_coal_dialog import Ui_base_coal_dialog        #导入“基础煤种库”窗口
from classic_coal_dialog import Ui_base_coal_dialog     #导入“经典煤种库”窗口
from new_coal_dialog import Ui_new_coal_dialog          #导入“新煤种库”窗口
from mine_info_dialog import Ui_mine_info_dialog        #导入“煤矿/矿山信息”窗口
from index_trend_dialog import Ui_index_trend_dialog    #导入“质量变化趋势”窗口

datafile = []

### 导入数据的窗口界面 ###
class Import_Window(QtWidgets.QMainWindow,Ui_Import_Window):
    def __init__(self):
        super(Import_Window, self).__init__()
        self.setupUi(self)

    # 打开文件浏览窗口，选择数据文件
    def find_files(self):
        datafiles, filetype = QtWidgets.QFileDialog.getOpenFileNames(self, "浏览选取煤种数据文件", "./",filter='Excel Files(*.xlsx *.xls);;CSV Files(*.csv)')
        self.textEdit.setText('')
        if len(datafiles) > 0:
            self.textEdit.append('此次将读取以下数据文件:')
            for item in datafiles:
                self.textEdit.append(item)

    # 重新读取数据，合并保存
    def reload_files(self):
        print()


### 数据库程序的主界面 ###
class Main_Window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)

### 分品种煤质指标数据窗口 ###
class Coal_Index_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_coal_index_dialog()
        self.child.setupUi(self)

### 基础煤种指标数据窗口 ###
class Base_Coal_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_base_coal_dialog()
        self.child.setupUi(self)

### 经典煤种指标数据窗口 ###
class Classic_Coal_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_base_coal_dialog()
        self.child.setupUi(self)

### 新煤种指标数据窗口 ###
class New_Coal_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_new_coal_dialog()
        self.child.setupUi(self)

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
    ImportWindow.Open_Main.clicked.connect(MainWindow.show)         #打开主窗口
    ImportWindow.Open_Main.clicked.connect(ImportWindow.close)      #同时，关闭导入数据窗口

    sys.exit(app.exec_())