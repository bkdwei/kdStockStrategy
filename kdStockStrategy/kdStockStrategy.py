'''
Created on 2019年5月3日

@author: bkd
'''
from os.path import expanduser
import sqlite3
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from xlrd import open_workbook

from .dlg_average import dlg_average
from .fileutil import get_file_realpath
from .kdStockStrategy_ui import Ui_mainWindow


class kdStockStrategy(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.last_dir = None
        self.stock_name = "300etf"

    @pyqtSlot()
    def on_pb_import_excel_clicked(self):
        seleted_file, _ = QFileDialog.getOpenFileName(
            self, '导入excel文件', self.get_last_dir(), '*.xls', '')
        if seleted_file:
            print(seleted_file)
            book = open_workbook(seleted_file)
            for sheet in book.sheets():
                self.read_excel(sheet)

    def read_excel(self, sheet):
        # 判断有效sheet
        if sheet.nrows > 0 and sheet.ncols > 0:
            total_rows = []
            for row in range(1, sheet.nrows):  # 行，跳过表头
                row_data = []
                for col in range(sheet.ncols):  # 列
                    data = sheet.cell(row, col).value
#                     print(row,col,data)
                    # excel表格内容数据类型转换 float->int，unicode->utf-8
                    if col == 0:
                        data = data.split(",")[0]
                    if col == 1:
                        row_data.append(self.le_stockname.text())
                    if col in (5, 6):
                        data *= 100
                    row_data.append(data)
#                 print("进度:" + str(row) + "/" + str(sheet.nrows))
                if self.check_data_length(row_data, row):
                    total_rows.append(row_data)
            self.insert_sqlite(total_rows)
    # 检查row_data长度

    def check_data_length(self, row_data, row):
        #         print(row, len(row_data), row_data)
        if len(row_data) == 12:
            #             self.insert_sqlite(row_data)
            return True
        else:
            print(str(row) + "不够十一个字段")
            return False

    def insert_sqlite(self, total_rows):
        # 打开数据库（不存在时会创建数据库）
        con = sqlite3.connect(get_file_realpath("../data/kdStockStrategy.db"))
        try:
            # 插入数据不要使用拼接字符串的方式，容易收到sql注入攻击
            cur = con.cursor()
            for single_row in total_rows:
                print(len(single_row), single_row)
                cur.execute("insert into history(trade_date,stock_name,open_price,high,low,close_price,gains,amplitude,total_hands,amount,change_hands,deal_number) values(?,?,?,?,?,?,?,?,?,?,?,?)", single_row)
            con.commit()
        except sqlite3.Error as e:
            print("An error occurred: " + str(e))
        finally:
            print("insert all data finish")
            cur.close()
            con.close()
#             获取上一次打开的目录

    def get_last_dir(self):
        if self.last_dir:
            return self.last_dir
        else:
            #             return expanduser("~")
            return get_file_realpath("../data")

    @pyqtSlot()
    def on_pb_excute_strategy_clicked(self):
        cash = self.le_cash.text()

        con = sqlite3.connect(get_file_realpath("../data/kdStockStrategy.db"))
        cur = con.cursor()
        cur.execute(
            "select * from history where stock_name = '{}' order by trade_date".format(self.le_stockname.text()))
        records = cur.fetchall()
        print(records)

        for record in records:
            pass

    @pyqtSlot()
    def on_action_average_triggered(self):
        print("g")
        self.dlg_average = dlg_average()
        self.dlg_average.show()


def main():
    app = QApplication(sys.argv)
    win = kdStockStrategy()
    win.show()
    sys.exit(app.exec_())
