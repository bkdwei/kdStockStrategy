# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/bkd/pyqt/kdStockStrategy/kdStockStrategy/kdStockStrategy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(594, 426)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_import_excel = QtWidgets.QPushButton(self.centralwidget)
        self.pb_import_excel.setGeometry(QtCore.QRect(210, 10, 89, 25))
        self.pb_import_excel.setObjectName("pb_import_excel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.label.setObjectName("label")
        self.le_stockname = QtWidgets.QLineEdit(self.centralwidget)
        self.le_stockname.setGeometry(QtCore.QRect(80, 10, 113, 25))
        self.le_stockname.setObjectName("le_stockname")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 67, 17))
        self.label_2.setObjectName("label_2")
        self.le_cash = QtWidgets.QLineEdit(self.centralwidget)
        self.le_cash.setGeometry(QtCore.QRect(90, 80, 113, 25))
        self.le_cash.setObjectName("le_cash")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 120, 67, 17))
        self.label_4.setObjectName("label_4")
        self.pb_excute_strategy = QtWidgets.QPushButton(self.centralwidget)
        self.pb_excute_strategy.setGeometry(QtCore.QRect(450, 110, 89, 25))
        self.pb_excute_strategy.setObjectName("pb_excute_strategy")
        self.de_begin = QtWidgets.QDateEdit(self.centralwidget)
        self.de_begin.setGeometry(QtCore.QRect(90, 110, 111, 26))
        self.de_begin.setDateTime(QtCore.QDateTime(QtCore.QDate(2006, 1, 1), QtCore.QTime(0, 0, 0)))
        self.de_begin.setObjectName("de_begin")
        self.de_end = QtWidgets.QDateEdit(self.centralwidget)
        self.de_end.setGeometry(QtCore.QRect(310, 110, 111, 26))
        self.de_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 5, 1), QtCore.QTime(0, 0, 0)))
        self.de_end.setObjectName("de_end")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 67, 17))
        self.label_5.setObjectName("label_5")
        self.le_max_price = QtWidgets.QLineEdit(self.centralwidget)
        self.le_max_price.setGeometry(QtCore.QRect(90, 160, 113, 25))
        self.le_max_price.setObjectName("le_max_price")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 160, 67, 17))
        self.label_6.setObjectName("label_6")
        self.le_min_price = QtWidgets.QLineEdit(self.centralwidget)
        self.le_min_price.setGeometry(QtCore.QRect(320, 160, 113, 25))
        self.le_min_price.setObjectName("le_min_price")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_import_excel.setText(_translate("MainWindow", "导入excel"))
        self.label.setText(_translate("MainWindow", "股票名称"))
        self.le_stockname.setText(_translate("MainWindow", "300etf"))
        self.label_2.setText(_translate("MainWindow", "起始金额"))
        self.le_cash.setText(_translate("MainWindow", "20000"))
        self.label_3.setText(_translate("MainWindow", "开始时间"))
        self.label_4.setText(_translate("MainWindow", "结束时间"))
        self.pb_excute_strategy.setText(_translate("MainWindow", "执行策略"))
        self.label_5.setText(_translate("MainWindow", "最高价"))
        self.le_max_price.setText(_translate("MainWindow", "4.3"))
        self.label_6.setText(_translate("MainWindow", "最低价"))
        self.le_min_price.setText(_translate("MainWindow", "2.5"))

