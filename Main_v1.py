# coding=utf-8

import sys
from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import QDialog
from Import_Data import Ui_Import_Window
from MainWindows import Ui_MainWindow
from coal_index_dialog import Ui_coal_index_dialog
#from classic_dialog import Ui_classic_dialog
#from new_dialog import Ui_new_dialog
#from mine_dialog import Ui_mine_dialog
#from trend_dialog import Ui_trend_dialog

#################### Templete ################################
### 导入数据的窗口界面 ###
class Import_Window(QtWidgets.QMainWindow,Ui_Import_Window):
    def __init__(self):
        super(Import_Window, self).__init__()
        self.setupUi(self)

### 数据库程序的主界面 ###
class Main_Window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)

### 分品种煤质指标数据库窗口 ###
class Coal_index_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_coal_index_dialog()
        self.child.setupUi(self)

#class Major_Window(QDialog):
#    def __init__(self):
#        QDialog.__init__(self)
#        self.child = Ui_major_dialog()
#        self.child.setupUi(self)
#
#class Classic_Window(QDialog):
#    def __init__(self):
#        QDialog.__init__(self)
#        self.child = Ui_classic_dialog()
#        self.child.setupUi(self)
#
#class New_Window(QDialog):
#    def __init__(self):
#        QDialog.__init__(self)
#        self.child = Ui_new_dialog()
#        self.child.setupUi(self)
#
#class Mine_Window(QDialog):
#    def __init__(self):
#        QDialog.__init__(self)
#        self.child = Ui_mine_dialog()
#        self.child.setupUi(self)
#
#class Trend_Window(QDialog):
#    def __init__(self):
#        QDialog.__init__(self)
#        self.child = Ui_trend_dialog()
#        self.child.setupUi(self)


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
    CoalIndexWindow = Coal_index_Window()
    #BaseWindow = Base_Window()
    #ClassicWindow = Classic_Window()
    #NewWindow = New_Window()
    #MineWindow = Mine_Window()
    #TrendWindow = Trend_Window()
    MainWindow.coal_index.clicked.connect(CoalIndexWindow.show)
    #MainWindow.minor_lib.clicked.connect(MinorWindow.show)
    #MainWindow.base_coal.clicked.connect(BaseWindow.show)
    #MainWindow.classic_coal.clicked.connect(ClassicWindow.show)
    #MainWindow.new_coal.clicked.connect(NewWindow.show)
    #MainWindow.mine_info.clicked.connect(MineWindow.show)
    #MainWindow.trend.clicked.connect(TrendWindow.show)

    ImportWindow.show()
    ImportWindow.Open_Main.clicked.connect(MainWindow.show)
    ImportWindow.Open_Main.clicked.connect(ImportWindow.close)
    #MainWindow.show()
    sys.exit(app.exec_())