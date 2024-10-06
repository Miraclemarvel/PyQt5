import sys
import time

from PyQt5.QtCore import QThread

from ui_17 import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication

class MyThread(QThread):
    def run(self):
        for i in range(5):
            print("正在登录中...还剩%ds"%(5-i))
            time.sleep(1)
        print("登陆成功！")

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Btn_1.clicked.connect(self.on_Btn1_clicked)
        self.Btn_2.clicked.connect(self.on_Btn2_clicked)

    def on_Btn1_clicked(self):
        for i in range(5):
            print("正在登录中...还剩%ds" % (5 - i))
            time.sleep(1)
        print("登陆成功！")

    def on_Btn2_clicked(self):
        self.thread = MyThread()
        self.thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()