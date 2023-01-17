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

        self.ordering()

    def ordering(self):
        self.open_db()
        self.c.execute(f'select a.재료, if(max(a.수량) > min(b.수량), "구매", "보류"), min(b.단가) from bom a left join inventory b on a.재료 = b.재료 group by 재료;')
        article = self.c.fetchall()
        article_list = list()
        for i in article:
            if i[1] == '구매':
                self.c.execute(f'update inventory set 수량 = 수량 + 구매량 where 재료 ="{i[0]}";')
                article_list.append([i[0], i[2]])
        print(article_list)
        self.conn.close()

    def open_db(self):
        self.conn = p.connect(host=hos, port=por, user=use, password=pw, db='snack', charset='utf8')
        self.c = self.conn.cursor()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()