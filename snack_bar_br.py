import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql


snack_bar = uic.loadUiType("snack_bar.ui")[0]

class WindowClass(QMainWindow, snack_bar) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(0)
        self.mainpage_button.clicked.connect(self.mainpage)
        self.signup_main_button.clicked.connect(self.signup_page)
        self.signup_cancle_button.clicked.connect(self.homepage)
        self.question_add_button.clicked.connect(self.question_add)
        self.question_cancle_button.clicked.connect(self.mainpage)
        self.back_button.clicked.connect(self.manager_page)
        self.manager_question.clicked.connect(self.manager_page)
        self.manager_question.clicked.connect(self.manager_page)
        self.manager_inventory.clicked.connect(self.manager_page)
        self.payment_cancle_button.clicked.connect(self.homepage)
        self.salesback_button.clicked.connect(self.homepage)
        self.question_button.clicked.connect(self.question)
        self.shopping_button.clicked.connect(self.shopping_basket)
        self.payment_cancle_button.clicked.connect(self.mainpage)
        self.salesback_button.clicked.connect(self.mainpage)
        self.signup_confirm_button.clicked.connect(self.homepage)
        self.manager_inventory.clicked.connect(self.question)
        self.logout_main_button.clicked.connect(self.homepage)
        self.logout_manager_button.clicked.connect(self.homepage)


    # 홈페이지 첫화면
    def homepage(self):
        self.stackedWidget.setCurrentIndex(0)

    # 회원가입 페이지
    def signup_page(self):
        self.stackedWidget.setCurrentIndex(1)

    # 로그인후 가장 먼저 보이는 메뉴 창
    def mainpage(self):
        self.stackedWidget.setCurrentIndex(2)

    # 문의하기 게시판
    def question(self):
        self.stackedWidget.setCurrentIndex(3)
        db = pymysql.connect(host='localhost', port=3306, user='root', password='0000', db='snack', charset='utf8')
        cursor = db.cursor()
        cursor.execute("SELECT * from snack.question")
        questionlist = cursor.fetchall()
        print(questionlist)
        self.QandA_list.setRowCount(len(questionlist))
        self.QandA_list.setColumnCount(len(questionlist[0]))
        self.QandA_list.setHorizontalHeaderLabels(['주문번호', '아이디', '내용', '시간','답변'])
        for i in range(len(questionlist)):
            for j in range(len(questionlist[i])):
                self.QandA_list.setItem(i, j, QTableWidgetItem(str(questionlist[i][j])))
        # self.QandA_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.QandA_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def question_add(self):
        check = QMessageBox.question(self, ' ','등록 하겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if check == QMessageBox.Yes:
            QMessageBox.information(self, ' ','문의가 등록되었습니다.')


        else:
            QMessageBox.information(self, ' ', '상품주문으로 돌아갑니다.')



   # 관리자 재고확인하기
    def inventory_view(self):
        self.stackedWidget.setCurrentIndex(4)

    # 장바구니
    def shopping_basket(self):
        self.stackedWidget.setCurrentIndex(5)

    # 관리자 매출확인
    def sales_view(self):
        self.stackedWidget.setCurrentIndex(6)

    # 관리자용 메인화면
    def manager_page(self):
        self.stackedWidget.setCurrentIndex(7)

    # 관리자 문의함확인하기
    def question_view(self):
        self.stackedWidget.setCurrentIndex(8)



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()