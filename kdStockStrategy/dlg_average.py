from os.path import expanduser, join

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .dlg_average_ui import Ui_dlg_average


class dlg_average(QDialog, Ui_dlg_average):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    @pyqtSlot()
    def on_pb_calculate_strategy_clicked(self):
        max_price = self.dbsp_max_price.value()
        min_price = self.dbsp_min_price.value()
        middle_price = (max_price + min_price) / 2
        total_increase = round(max_price - min_price, 2)
        ten_pecentage_increase = round(total_increase / 10, 3)
        target_benefit = round((max_price - min_price) /
                               min_price * self.sp_base_stock.value(), 2)

        self.lb_middle_price.setText(str(middle_price))
        self.lb_ten_pecent_increase.setText(str(ten_pecentage_increase))
        self.lb_total_increase.setText(str(total_increase))
        self.lb_target_benefit.setText(str(target_benefit))
        self.dbsp_current_price.setSingleStep(ten_pecentage_increase)


#         阶梯计算
        str_ladder = ""
        for i in range(10):
            str_ladder = str_ladder + \
                str(i) + "    " + str(round(min_price +
                                            i * ten_pecentage_increase, 3)) + "\n"
            print(i)
        print(str_ladder)
        self.te_ladder.setText(str_ladder)

    @pyqtSlot()
    def on_pb_calculate_trade_amount_clicked(self):
        current_price = self.dbsp_current_price.value()
        base_stock = self.sp_base_stock.value()
        trade_amount = round(base_stock / 10 / current_price)
        self.lb_trade_amount.setText(str(trade_amount))

        min_price = self.dbsp_min_price.value()
        current_stock = round((1 - (current_price - min_price) /
                               min_price) * base_stock)
        print(current_stock)
        self.sp_current_stock.setValue(current_stock)
