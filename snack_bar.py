import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql
from datetime import datetime

snack_bar = uic.loadUiType("snack_bar.ui")[0]

class WindowClass(QMainWindow, snack_bar) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(0)
        self.mainpage_button.clicked.connect(self.mainpage)
        self.signup_main_button.clicked.connect(self.signup_page)
        self.signup_cancle_button.clicked.connect(self.homepage)
        self.question_add_button.clicked.connect(self.mainpage)
        self.question_cancle_button.clicked.connect(self.mainpage)
        self.back_button.clicked.connect(self.manager_page)
        self.manager_question.clicked.connect(self.manager_page)
        self.manager_question.clicked.connect(self.manager_page)
        self.manager_inventory.clicked.connect(self.manager_page)
        # self.payment_cancle_button.clicked.connect(self.homepage)
        self.salesback_button.clicked.connect(self.homepage)
        self.question_button.clicked.connect(self.question)
        self.shopping_button.clicked.connect(self.shopping_basket)
        self.payment_cancle_button.clicked.connect(self.mainpage)
        self.salesback_button.clicked.connect(self.mainpage)
        self.signup_confirm_button.clicked.connect(self.signup)
        self.manager_inventory.clicked.connect(self.question)
        self.overlap_button.clicked.connect(self.double_check)
        self.logout_main_button.clicked.connect(self.homepage)
        self.logout_manager_button.clicked.connect(self.homepage)
        self.tableWidget_2.cellDoubleClicked.connect(self.del_request)
        self.shopping_list_del.clicked.connect(self.del_request)
        # self.kimbap_plus.clicked.connect(self.dsf)
        # self.tuna_kimbap_plus.clicked.connect(self.dsf)
        self.payment_button.clicked.connect(self.purchase)


    # 홈페이지 첫화면
    def homepage(self):
        self.id_check.clear()
        self.name_check.clear()
        self.pw_check.clear()
        self.pw2_check.clear()
        self.add_check.clear()
        self.phon_check.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.kimbap_plus.setValue(0)
        self.tuna_kimbap_plus_2.setValue(0)
        self.Cheese_kimbap_plus_2.setValue(0)
        self.bokki_plus_3.setValue(0)
        self.rabokki_plus_3.setValue(0)
        self.Cheese_bokki_plus.setValue(0)
        self.pig_Stew_plus_3.setValue(0)
        self.tuna_Stew_plus.setValue(0)
        self.tableWidget_2.clear()
        self.stackedWidget.setCurrentIndex(0)

    def open_db(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='qwer1234', db='snack', charset='utf8')
        self.c = self.conn.cursor()

    def signup(self):
        if self.id_check.text() == '' or self.name_check.text() == '' or self.pw_check.text() == '' or self.pw2_check.text() == '' or self.add_check.text() == '' or self.phon_check.text() == '':
            QMessageBox.critical(self, "에러", "빈칸을 전부 입력해주세요")
        elif self.pw_check.text() != self.pw2_check.text():
            QMessageBox.critical(self, "에러", "비밀번호와 비밀번호확인이 일치하지 않습니다.")
        elif bool(self.login_okay) == False:
            QMessageBox.critical(self, "에러", "중복확인을 해주세요")
        elif bool(self.buyer_Confirm_button.isChecked()) == False and bool(self.seller_Confirm_button.isChecked()) == False:
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
        self.open_db()
        self.c.execute(f'SELECT 아이디 FROM user WHERE 아이디 = "{self.id_check.text()}"')
        checking = self.c.fetchall()
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

    # 회원가입 페이지
    def signup_page(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.login_okay = False
        self.stackedWidget.setCurrentIndex(1)


    # 로그인후 가장 먼저 보이는 메뉴 창
    def mainpage(self):
        self.open_db()
        self.c.execute(f'SELECT 아이디, `사업자 여부` FROM user WHERE 아이디 = "{self.lineEdit.text()}" and 비밀번호 = "{self.lineEdit_2.text()}"')
        self.login_infor = self.c.fetchall()
        self.conn.close()
        if self.login_infor == ():
            QMessageBox.critical(self, "에러", "아이디나 비밀번호가 틀립니다.")
        else:
            if self.login_infor[0][1] == '개인':
                self.stackedWidget.setCurrentIndex(2)
            elif self.login_infor[0][1] == '사업자':
                self.stackedWidget.setCurrentIndex(7)

    def menu_counting(self):
        self.kimbap_plus.setStep(0)

    # 문의하기 게시판
    def question(self):
        self.stackedWidget.setCurrentIndex(3)

   # 관리자 재고확인하기
    def inventory_view(self):
        self.stackedWidget.setCurrentIndex(4)

    # 장바구니
    def shopping_basket(self):
        self.total_bill = 0
        self.request_list = []
        # 장바구니에서 메뉴고르는 페이지로 돌아왔을때 다 0으로 초기화해주면 다시 고르려는것도 사라지니까 이거 생각좀 해야할듯
        if self.kimbap_plus.value() != 0:
            self.request_list.append(['김밥', str(self.kimbap_plus.value()), str(self.tuna_kimbap_plus_2.value() * 9000)])
        if self.tuna_kimbap_plus_2.value() != 0:
            self.request_list.append(['참치김밥', str(self.tuna_kimbap_plus_2.value()), str(self.tuna_kimbap_plus_2.value()*11000)])
        if self.Cheese_kimbap_plus_2.value() != 0:
            self.request_list.append(['치즈김밥', str(self.Cheese_kimbap_plus_2.value()), str(self.Cheese_kimbap_plus_2.value() * 11000)])
        if self.bokki_plus_3.value() != 0:
            self.request_list.append(['떡볶이', str(self.bokki_plus_3.value()), str(self.bokki_plus_3.value() * 15000)])
        if self.rabokki_plus_3.value() != 0:
            self.request_list.append(['라볶이', str(self.rabokki_plus_3.value()), str(self.rabokki_plus_3.value() * 17000)])
        if self.Cheese_bokki_plus.value() != 0:
            self.request_list.append(['치즈떡볶이', str(self.Cheese_bokki_plus.value()), str(self.Cheese_bokki_plus.value() * 17000)])
        if self.pig_Stew_plus_3.value() != 0:
            self.request_list.append(['돼지김치찌개', str(self.pig_Stew_plus_3.value()), str(self.pig_Stew_plus_3.value() * 14000)])
        if self.tuna_Stew_plus.value() != 0:
            self.request_list.append(['참치김치찌개', str(self.tuna_Stew_plus.value()), str(self.tuna_Stew_plus.value()*18000)])
        print(self.request_list)
        self.stackedWidget.setCurrentIndex(5)
        if self.request_list != []:
            self.tablesetting()
        else:
            self.bill_result.setText("총액:0원")
            self.tableWidget_2.clear()

    def purchase(self):
        now = datetime.now()
        self.open_db()
        self.c.execute(f'select 주문번호 from request')
        store = self.c.fetchall()
        for i in range(len(self.request_list[0])):
            self.c.execute(
                f'INSERT INTO request (주문번호, 아이디, 상품명, 수량, 금액, 시간) VALUES ("{}", "{self.login_infor[0][0]}", "{self.request_list[0][0]}", "{self.request_list[0][1]}", "{self.request_list[0][2]}", now())')
        self.conn.commit()
        self.conn.close()
        # order_num += 1

    # 관리자 매출확인
    def sales_view(self):
        self.stackedWidget.setCurrentIndex(6)

    # 관리자용 메인화면
    def manager_page(self):
        self.stackedWidget.setCurrentIndex(7)

    # 관리자 문의함확인하기
    def question_view(self):
        self.stackedWidget.setCurrentIndex(8)

    def del_request(self):
        QMessageBox.information(self, "확인", "장바구니에서 삭제합니다")
        list_row = self.tableWidget_2.currentRow()
        del_list = self.request_list[list_row]
        cancel_re = int(self.request_list[list_row][1]) - 1
        if self.request_list[list_row][0] == '김밥':
            self.kimbap_plus.setValue(cancel_re)
            self.request_list[list_row][2] = str(self.kimbap_plus.value()*9000)
        elif self.request_list[list_row][0] == '참치김밥':
            self.tuna_kimbap_plus_2.setValue(cancel_re)
            self.request_list[list_row][2] = str(self.tuna_kimbap_plus_2.value()*11000)
        elif self.request_list[list_row][0] == '치즈김밥':
            self.Cheese_kimbap_plus_2.setValue(cancel_re)
            self.request_list[list_row][2] = str(self.Cheese_kimbap_plus_2.value() * 11000)
        elif self.request_list[list_row][0] == '떡볶이':
            self.bokki_plus_3.setValue(cancel_re)
            self.request_list[list_row][2] = str(self.bokki_plus_3.value() * 15000)
        elif self.request_list[list_row][0] == '라볶이':
            self.rabokki_plus_3.setValue(cancel_re)
            self.request_list[list_row][2] = str(self.rabokki_plus_3.value() * 17000)
        elif self.request_list[list_row][0] == '치즈떡볶이':
            self.Cheese_bokki_plus.setValue(cancel_re)
            self.request_list[list_row][2] = str(self.Cheese_bokki_plus.value() * 17000)
        elif self.request_list[list_row][0] == '돼지김치찌개':
            self.pig_Stew_plus_3.setValue(cancel_re)
            self.request_list[list_row][2] = str(self.pig_Stew_plus_3.value() * 14000)
        elif self.request_list[list_row][0] == '참치김치찌개':
            self.tuna_Stew_plus.setValue(cancel_re)
            self.request_list[list_row][2] = str(self.tuna_Stew_plus.value()*18000)
        self.request_list[list_row][1] = str(cancel_re)
        if cancel_re == 0:
            self.request_list.remove(del_list)
        print(self.request_list)
        if self.request_list != []:
            self.tablesetting()
        else:
            self.bill_result.setText("총액:0원")
            self.kimbap_plus.setValue(0)
            self.tuna_kimbap_plus_2.setValue(0)
            self.Cheese_kimbap_plus_2.setValue(0)
            self.bokki_plus_3.setValue(0)
            self.rabokki_plus_3.setValue(0)
            self.Cheese_bokki_plus.setValue(0)
            self.pig_Stew_plus_3.setValue(0)
            self.tuna_Stew_plus.setValue(0)
            self.tableWidget_2.clear()
    def tablesetting(self):
        self.total_bill = 0
        for i in range(len(self.request_list)):
            self.total_bill += int(self.request_list[i][2])
        totaltext = "총액:" + str(self.total_bill) + "원"
        self.bill_result.setText(totaltext)
        self.tableWidget_2.setRowCount(len(self.request_list))
        self.tableWidget_2.setColumnCount(len(self.request_list[0]))
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(self.request_list)):
            for j in range(len(self.request_list[0])):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(self.request_list[i][j]))

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()