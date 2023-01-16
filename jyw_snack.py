import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("snack_bar.ui")[0]

hos = '127.0.0.1'
por = 3306
use = 'root'
pw = '0000'


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.conn = p.connect(host=hos, port=por, user=use, password=pw, db='snack', charset='utf8')
        self.c = self.conn.cursor()
        self.conn.close()

    def open_db(self):
        self.conn = p.connect(host=hos, port=por, user=use, password=pw, db='snack', charset='utf8')
        self.c = self.conn.cursor()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()