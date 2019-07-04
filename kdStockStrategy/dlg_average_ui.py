# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/dev/workspace/kdStockStrategy/kdStockStrategy\dlg_average.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlg_average(object):
    def setupUi(self, dlg_average):
        dlg_average.setObjectName("dlg_average")
        dlg_average.resize(453, 367)
        self.gridLayout = QtWidgets.QGridLayout(dlg_average)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(dlg_average)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lb_middle_price = QtWidgets.QLabel(dlg_average)
        self.lb_middle_price.setObjectName("lb_middle_price")
        self.gridLayout.addWidget(self.lb_middle_price, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(dlg_average)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 2, 1, 1)
        self.sp_base_stock = QtWidgets.QSpinBox(dlg_average)
        self.sp_base_stock.setMaximum(500000000)
        self.sp_base_stock.setProperty("value", 20000)
        self.sp_base_stock.setObjectName("sp_base_stock")
        self.gridLayout.addWidget(self.sp_base_stock, 0, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(dlg_average)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)
        self.dbsp_max_price = QtWidgets.QDoubleSpinBox(dlg_average)
        self.dbsp_max_price.setDecimals(3)
        self.dbsp_max_price.setProperty("value", 0.71)
        self.dbsp_max_price.setObjectName("dbsp_max_price")
        self.gridLayout.addWidget(self.dbsp_max_price, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(dlg_average)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lb_target_benefit = QtWidgets.QLabel(dlg_average)
        self.lb_target_benefit.setObjectName("lb_target_benefit")
        self.gridLayout.addWidget(self.lb_target_benefit, 1, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(dlg_average)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(dlg_average)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dbsp_min_price = QtWidgets.QDoubleSpinBox(dlg_average)
        self.dbsp_min_price.setDecimals(3)
        self.dbsp_min_price.setProperty("value", 0.45)
        self.dbsp_min_price.setObjectName("dbsp_min_price")
        self.gridLayout.addWidget(self.dbsp_min_price, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(dlg_average)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(dlg_average)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.lb_ten_pecent_increase = QtWidgets.QLabel(dlg_average)
        self.lb_ten_pecent_increase.setObjectName("lb_ten_pecent_increase")
        self.gridLayout.addWidget(self.lb_ten_pecent_increase, 3, 1, 1, 1)
        self.te_ladder = QtWidgets.QTextEdit(dlg_average)
        self.te_ladder.setObjectName("te_ladder")
        self.gridLayout.addWidget(self.te_ladder, 7, 0, 1, 4)
        self.label_16 = QtWidgets.QLabel(dlg_average)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 5, 0, 1, 1)
        self.lb_total_increase = QtWidgets.QLabel(dlg_average)
        self.lb_total_increase.setObjectName("lb_total_increase")
        self.gridLayout.addWidget(self.lb_total_increase, 4, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(dlg_average)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 2, 1, 1)
        self.pb_calculate_strategy = QtWidgets.QPushButton(dlg_average)
        self.pb_calculate_strategy.setObjectName("pb_calculate_strategy")
        self.gridLayout.addWidget(self.pb_calculate_strategy, 8, 0, 1, 1)
        self.dbsp_current_price = QtWidgets.QDoubleSpinBox(dlg_average)
        self.dbsp_current_price.setDecimals(3)
        self.dbsp_current_price.setProperty("value", 0.45)
        self.dbsp_current_price.setObjectName("dbsp_current_price")
        self.gridLayout.addWidget(self.dbsp_current_price, 2, 3, 1, 1)
        self.pb_calculate_trade_amount = QtWidgets.QPushButton(dlg_average)
        self.pb_calculate_trade_amount.setObjectName("pb_calculate_trade_amount")
        self.gridLayout.addWidget(self.pb_calculate_trade_amount, 8, 1, 1, 1)
        self.lb_trade_amount = QtWidgets.QLabel(dlg_average)
        self.lb_trade_amount.setObjectName("lb_trade_amount")
        self.gridLayout.addWidget(self.lb_trade_amount, 4, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(dlg_average)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.sp_current_stock = QtWidgets.QSpinBox(dlg_average)
        self.sp_current_stock.setObjectName("sp_current_stock")
        self.gridLayout.addWidget(self.sp_current_stock, 3, 3, 1, 1)

        self.retranslateUi(dlg_average)
        QtCore.QMetaObject.connectSlotsByName(dlg_average)

    def retranslateUi(self, dlg_average):
        _translate = QtCore.QCoreApplication.translate
        dlg_average.setWindowTitle(_translate("dlg_average", "平均价策略"))
        self.label_3.setText(_translate("dlg_average", "中间价"))
        self.lb_middle_price.setText(_translate("dlg_average", "0"))
        self.label_12.setText(_translate("dlg_average", "当前价格"))
        self.label_9.setText(_translate("dlg_average", "底仓"))
        self.label.setText(_translate("dlg_average", "最高价"))
        self.lb_target_benefit.setText(_translate("dlg_average", "0"))
        self.label_10.setText(_translate("dlg_average", "目标盈利"))
        self.label_2.setText(_translate("dlg_average", "最低价"))
        self.label_5.setText(_translate("dlg_average", "10%涨幅"))
        self.label_7.setText(_translate("dlg_average", "总涨幅"))
        self.lb_ten_pecent_increase.setText(_translate("dlg_average", "0"))
        self.label_16.setText(_translate("dlg_average", "阶梯"))
        self.lb_total_increase.setText(_translate("dlg_average", "0"))
        self.label_13.setText(_translate("dlg_average", "当前仓位"))
        self.pb_calculate_strategy.setText(_translate("dlg_average", "计算"))
        self.pb_calculate_trade_amount.setText(_translate("dlg_average", "计算交易"))
        self.lb_trade_amount.setText(_translate("dlg_average", "0"))
        self.label_4.setText(_translate("dlg_average", "交易股数"))
