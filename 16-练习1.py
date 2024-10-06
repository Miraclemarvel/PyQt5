import sys
import time

from ui_16 import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit


class Login(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.userList = {"sk":"123456", "elysia":"1111"}
        self.loginBtn.clicked.connect(self.login)

    def login(self):
        user = self.userEdit.text()
        password = self.passwordEdit.text()

        for i in range(5):
            print("正在登录，还剩%d秒"%(5-i))
            time.sleep(1)

        if self.userList.get(user) == password:
            self.textEdit.append("登录成功！欢迎%s" % user)
        else:
            self.textEdit.append("登录失败！用户名或密码错误！请重试")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Login()
    w.show()

    app.exec_()