# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 787)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.coal_index = QtWidgets.QPushButton(self.centralwidget)
        self.coal_index.setGeometry(QtCore.QRect(60, 200, 200, 50))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.coal_index.setFont(font)
        self.coal_index.setObjectName("coal_index")
        self.base_coal = QtWidgets.QPushButton(self.centralwidget)
        self.base_coal.setGeometry(QtCore.QRect(380, 200, 200, 50))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.base_coal.setFont(font)
        self.base_coal.setObjectName("base_coal")
        self.classic_coal = QtWidgets.QPushButton(self.centralwidget)
        self.classic_coal.setGeometry(QtCore.QRect(690, 200, 200, 50))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.classic_coal.setFont(font)
        self.classic_coal.setObjectName("classic_coal")
        self.new_coal = QtWidgets.QPushButton(self.centralwidget)
        self.new_coal.setGeometry(QtCore.QRect(60, 500, 200, 50))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.new_coal.setFont(font)
        self.new_coal.setObjectName("new_coal")
        self.mine_info = QtWidgets.QPushButton(self.centralwidget)
        self.mine_info.setGeometry(QtCore.QRect(380, 500, 200, 50))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mine_info.setFont(font)
        self.mine_info.setObjectName("mine_info")
        self.index_trend = QtWidgets.QPushButton(self.centralwidget)
        self.index_trend.setGeometry(QtCore.QRect(690, 500, 200, 50))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.index_trend.setFont(font)
        self.index_trend.setObjectName("index_trend")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(80, 40, 160, 160))
        self.label.setMinimumSize(QtCore.QSize(160, 160))
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("主库.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(400, 40, 160, 160))
        self.label_3.setMinimumSize(QtCore.QSize(160, 160))
        self.label_3.setMaximumSize(QtCore.QSize(100, 100))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("基础煤种.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(710, 40, 160, 160))
        self.label_4.setMinimumSize(QtCore.QSize(160, 160))
        self.label_4.setMaximumSize(QtCore.QSize(100, 100))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("经典煤.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(710, 340, 160, 160))
        self.label_5.setMinimumSize(QtCore.QSize(160, 160))
        self.label_5.setMaximumSize(QtCore.QSize(100, 100))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("趋势.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(80, 340, 160, 160))
        self.label_6.setMinimumSize(QtCore.QSize(160, 160))
        self.label_6.setMaximumSize(QtCore.QSize(100, 100))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("新煤.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(400, 340, 160, 160))
        self.label_7.setMinimumSize(QtCore.QSize(160, 160))
        self.label_7.setMaximumSize(QtCore.QSize(100, 100))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("矿山.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 630, 341, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setObjectName("label_8")
        self.quit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn.setGeometry(QtCore.QRect(850, 700, 100, 50))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.coal_index.clicked.connect(MainWindow.coal_index_click)
        #self.base_coal.clicked.connect(MainWindow.base_coal_click)
        #self.classic_coal.clicked.connect(MainWindow.classic_coal_click)
        #self.new_coal.clicked.connect(MainWindow.new_coal_click)
        #self.mine_info.clicked.connect(MainWindow.mine_info_click)
        #self.index_trend.clicked.connect(MainWindow.index_trend_click)
        self.quit_btn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "煤炭资源数据库"))
        self.coal_index.setText(_translate("MainWindow", "分品种指标库"))
        self.base_coal.setText(_translate("MainWindow", "基础煤种库"))
        self.classic_coal.setText(_translate("MainWindow", "经典煤种库"))
        self.new_coal.setText(_translate("MainWindow", "新煤种库"))
        self.mine_info.setText(_translate("MainWindow", "矿山信息"))
        self.index_trend.setText(_translate("MainWindow", "质量变化趋势分析"))
        self.label_8.setText(_translate("MainWindow", "煤炭资源数据库 V1.0"))
        self.quit_btn.setText(_translate("MainWindow", "退出"))

