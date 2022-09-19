import sys
import random as ran

from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\\develop\\Python\\design\\gacha.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.setFixedSize(400, 300)

        global acc1, acc2
        acc1 = 100000
        acc2 = 1000

        self.btn_cal.clicked.connect(self.cal)

        self.rb_acc1.clicked.connect(self.acc_func)
        self.rb_acc2.clicked.connect(self.acc_func)
        self.rb_acc3.clicked.connect(self.acc_func)

    def acc_func(self):
        global acc1, acc2

        if self.rb_acc1.isChecked():
            self.pb_bar.setValue(0)
            acc1 = 10000
            acc2 = 100
            self.pb_bar.setRange(0, acc1)
        elif self.rb_acc2.isChecked():
            self.pb_bar.setValue(0)
            acc1 = 100000
            acc2 = 1000
            self.pb_bar.setRange(0, acc1)
        elif self.rb_acc3.isChecked():
            self.pb_bar.setValue(0)
            acc1 = 1000000
            acc2 = 10000
            self.pb_bar.setRange(0, acc1)

    def cal(self):
        global acc1, acc2

        try:
            p = float(self.txt_pro.toPlainText()) * 0.01
            d = int(self.txt_do.toPlainText())
            want = int(self.txt_want.toPlainText())
        except:
            self.result.setPlainText("잘못된 값이 입력되었습니다.")
        else:
            if(p > 100 * (10 ** 10) or d <= 0 or want <= 0 or d < want):
                self.result.setPlainText("잘못된 값이 입력되었습니다.")
            else:
                t = 0
                b = 1
                x = 0

                if (p >= 0.1):
                    w2 = 1
                else:
                    w2 = 1.07

                while 1:
                    w = 2 ** x
                    r = p * w
                    if (r >= 0.1):
                        break
                    else:
                        x += 1

                p1 = (r / 0.01) * 0.01

                for j in range(acc1):
                    k = j + 1

                    self.pb_bar.setValue(k)

                    m = 0
                    for i in range(d):  # d번
                        # n = ran.randrange(10 ** 12) # 숫자 랜덤
                        if (ran.random() < p):  # p% 확률
                            m += 1
                    if (m >= want):  # want회 이상 당첨 횟수
                        t += 1

                per = t / acc2

                while 1:
                    t = 0
                    for j in range(10000):
                        m = 0
                        for i in range(b):  # b번
                            # n = ran.randrange(10 ** 12) # 숫자 랜덤
                            if (ran.random() < p1):  # p% 확률
                                m += 1
                        if (m >= 1):  # 1회 이상 당첨 횟수
                            t += 1
                    per1 = t / 100

                    if (per1 <= 99):
                        b += 1
                    else:
                        break

                bww = round(b * w * w2)

                # self.result.setPlainText(p1 + "%")
                self.result.setPlainText(str(want) + "회 이상 나올 확률 : " + str(per) + "%")
                self.result.append("\n99%의 확률로 1회 이상 당첨 : " + str(format(bww, ',')))

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()