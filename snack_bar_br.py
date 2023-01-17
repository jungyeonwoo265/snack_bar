import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql
import datetime as dt

snack_bar = uic.loadUiType("snack_bar.ui")[0]


class WindowClass(QMainWindow, snack_bar):
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
        self.signup_confirm_button.clicked.connect(self.signup)
        self.manager_inventory.clicked.connect(self.question)

        self.logout_main_button.clicked.connect(self.homepage)
        self.logout_manager_button.clicked.connect(self.homepage)
        self.manager_question.clicked.connect(self.question_view)
        self.manager_sales_del.clicked.connect(self.manager_question_del)
        self.manager_question_view.cellClicked.connect(self.cellclicked_event)
        self.manager_question_view.cellDoubleClicked.connect(self.cellclicked_event)
        self.manager_sales_add.clicked.connect(self.manager_question_add)
        self.logout_manager_button_3.clicked.connect(self.manager_page)




    # 홈페이지 첫화면
    def homepage(self):
        self.stackedWidget.setCurrentIndex(0)
        self.id_check.clear()
        self.name_check.clear()
        self.pw_check.clear()
        self.pw2_check.clear()
        self.add_check.clear()
        self.phon_check.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def open_db(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='0000', db='snack', charset='utf8')
        self.c = self.conn.cursor()


    def signup(self):
        if self.id_check.text() == '' or self.name_check.text() == '' or self.pw_check.text() == '' or self.pw2_check.text() == '' or self.add_check.text() == '' or self.phon_check.text() == '':
            QMessageBox.critical(self, "에러", "빈칸을 전부 입력해주세요")
        elif self.pw_check.text() != self.pw2_check.text():
            QMessageBox.critical(self, "에러", "비밀번호와 비밀번호확인이 일치하지 않습니다.")
        elif bool(self.login_okay) == False:
            QMessageBox.critical(self, "에러", "중복확인을 해주세요")
        elif bool(self.buyer_Confirm_button.isChecked()) == False and bool(
                self.seller_Confirm_button.isChecked()) == False:
            QMessageBox.critical(self, "에러", "사업자 또는 개인 선택해주세요")
        else:
            information = 'a'
            if self.buyer_Confirm_button.isChecked():
                information = self.buyer_Confirm_button.text()
            elif self.seller_Confirm_button.isChecked():
                information = self.seller_Confirm_button.text()
            self.open_db()
            self.c.execute(f'INSERT INTO user (아이디, 비밀번호, 이름, 주소, 전화번호, `사업자 여부`) VALUES ("{self.id_check.text()}", "{self.pw_check.text()}", "{self.name_check.text()}", "{self.add_check.text()}", "{self.phon_check.text()}", "{information}")')
            self.conn.commit()
            self.conn.close()
            QMessageBox.information(self, "확인", "회원가입에 성공하셨습니다")
            self.id_check.clear()
            self.name_check.clear()
            self.pw_check.clear()
            self.pw2_check.clear()
            self.add_check.clear()
            self.phon_check.clear()
            self.stackedWidget.setCurrentIndex(0)

    def double_check(self):
        self.db_open()
        self.c.execute(f'SELECT 아이디 FROM user WHERE 아이디 = "{self.id_check.text()}"')
        checking = self.cur.fetchall()
        self.conn.close()
        print(checking)

        if self.id_check.text() == '':
            QMessageBox.critical(self, "에러", "아이디를 입력해주세요")
        elif checking != ():
            QMessageBox.critical(self, "에러", "중복된 아이디 입니다")
        else:
            QMessageBox.information(self, "확인", "사용가능한 아이디입니다")
            self.login_okay = True
            self.id_check.textChanged.connect(self.signup_page)

    def signup_page(self):
        self.login_okay = False
        self.stackedWidget.setCurrentIndex(1)


    def mainpage(self):
        self.open_db()
        self.c.execute(f'SELECT * FROM user WHERE 아이디 = "{self.lineEdit.text()}" and 비밀번호 = "{self.lineEdit_2.text()}"')
        self.login_infor = self.c.fetchall()
        self.conn.close()
        print(self.login_infor)
        print(self.login_infor[0][0])
        if self.login_infor == ():
            QMessageBox.critical(self, "에러", "아이디나 비밀번호가 틀립니다.")
        else:
            self.logined = True
            if self.login_infor[0][5] == '개인':
                self.stackedWidget.setCurrentIndex(2)
            elif self.login_infor[0][5] == '사업자':
                self.stackedWidget.setCurrentIndex(7)

    # 회원가입 페이지
    # def signup_page(self):
    #     self.stackedWidget.setCurrentIndex(1)

    # 로그인후 가장 먼저 보이는 메뉴 창
    # def mainpage(self):
    #     self.stackedWidget.setCurrentIndex(2)

    # 문의하기 게시판
    def question(self):

        self.stackedWidget.setCurrentIndex(3)
        self.open_db()
        self.c.execute("SELECT * from snack.question")
        self.questionlist = self.c.fetchall()
        # print(self.questionlist)
        self.QandA_list.setRowCount(len(self.questionlist))
        self.QandA_list.setColumnCount(len(self.questionlist[0]))
        self.QandA_list.setHorizontalHeaderLabels(['주문번호', '아이디', '내용', '시간','답변'])
        for i in range(len(self.questionlist)):
            for j in range(len(self.questionlist[i])):
                self.QandA_list.setItem(i, j, QTableWidgetItem(str(self.questionlist[i][j])))
        self.QandA_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.conn.close()

    def question_add(self):
        self.time = dt.datetime.now()
        self.today = self.time.strftime('%Y-%m-%d %H:%M:%S')
        print(self.today)
        check = QMessageBox.question(self, ' ','등록 하겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if check == QMessageBox.Yes:
            self.open_db()
            self.c.execute(f"insert into snack.question (아이디,내용,시간) values ('{self.login_infor[0][0]}','{self.QandA_lineEdit.text()}','{self.today}')")
            self.conn.commit()
            self.c.execute("SELECT * from snack.question")
            self.questionlist = self.c.fetchall()
            print(self.questionlist)
            self.conn.close()
            self.QandA_list.setRowCount(len(self.questionlist))
            self.QandA_list.setColumnCount(len(self.questionlist[0]))
            self.QandA_list.setHorizontalHeaderLabels(['주문번호', '아이디', '내용', '시간', '답변'])
            for i in range(len(self.questionlist)):
                for j in range(len(self.questionlist[i])):
                    self.QandA_list.setItem(i, j, QTableWidgetItem(str(self.questionlist[i][j])))
            self.QandA_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
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
        self.open_db()
        self.c.execute("SELECT * from snack.question")
        self.questionlist = self.c.fetchall()
        print(self.questionlist)
        print(self.manager_question_view.currentRow())

        self.manager_question_view.setRowCount(len(self.questionlist))
        self.manager_question_view.setColumnCount(len(self.questionlist[0]))
        self.manager_question_view.setHorizontalHeaderLabels(['주문번호', '아이디', '내용', '시간', '답변'])
        for i in range(len(self.questionlist)):
            for j in range(len(self.questionlist[i])):
                self.manager_question_view.setItem(i, j, QTableWidgetItem(str(self.questionlist[i][j])))
        self.manager_question_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.conn.close()

    def manager_question_add(self):
        check = QMessageBox.question(self, ' ', '답변 하겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if check == QMessageBox.Yes:
            self.open_db()
            self.c.execute(f"update snack.question set 답변 ='{self.manager_line_add.text()}' where 내용 = '{self.cellchoice}'")
            self.conn.commit()
            QMessageBox.information(self, ' ', '답변이 등록되었습니다.')
            self.manager_line_add.clear()
            self.c.execute("SELECT * from snack.question")
            self.questionlist = self.c.fetchall()
            print(self.questionlist)
            self.manager_question_view.setRowCount(len(self.questionlist))
            self.manager_question_view.setColumnCount(len(self.questionlist[0]))
            self.manager_question_view.setHorizontalHeaderLabels(['주문번호', '아이디', '내용', '시간', '답변'])
            for i in range(len(self.questionlist)):
                for j in range(len(self.questionlist[i])):
                    self.manager_question_view.setItem(i, j, QTableWidgetItem(str(self.questionlist[i][j])))
            self.manager_question_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.conn.close()
        else:
            QMessageBox.information(self, ' ', '문의함으로 돌아갑니다.')

    def manager_question_del(self):
        check = QMessageBox.question(self, ' ', '삭제 하겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        self.manager_line_add.text()
        if check == QMessageBox.Yes:
            self.open_db()
            self.c.execute(f"delete from snack.question where 내용 = '{self.cellchoice}'")
            self.conn.commit()
            self.c.execute("SELECT * from snack.question")
            self.questionlist = self.c.fetchall()
            print(self.questionlist)
            QMessageBox.information(self, ' ', '삭제되었습니다.')
        else:
            QMessageBox.information(self, ' ', '문의함으로 돌아갑니다.')

        self.manager_question_view.setRowCount(len(self.questionlist))
        self.manager_question_view.setColumnCount(len(self.questionlist[0]))
        self.manager_question_view.setHorizontalHeaderLabels(['주문번호', '아이디', '내용', '시간', '답변'])
        for i in range(len(self.questionlist)):
            for j in range(len(self.questionlist[i])):
                self.manager_question_view.setItem(i, j, QTableWidgetItem(str(self.questionlist[i][j])))
        self.manager_question_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.conn.close()

    def cellclicked_event(self,row,col):
        self.data = self.manager_question_view.item(row,col)
        self.cellchoice = self.data.text()
        print(self.cellchoice)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()