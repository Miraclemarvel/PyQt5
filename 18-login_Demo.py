import json
import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot

from ui_18 import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication


class LoginThread(QThread):
    login_signal = pyqtSignal(str)
    flag = "Waiting"
    user_password_json = None

    def __init__(self, login_status):
        super().__init__()
        self.login_complete_status = login_status
        self.login_signal.connect(self.login_requests)


    def run(self):
        while True:
            if self.flag == "Waiting":
                print("子线程准备接收用户输入")
                time.sleep(1)
            elif self.flag == "Logining":
                user_password_json = json.loads(self.user_password_json)
                user = user_password_json.get("user")
                password = user_password_json.get("password")
                print(user)
                print(password)
                r = json.dumps({"status":"200"})
                self.login_complete_status.emit(r)
                self.flag = "Waiting"
            else:
                break



    def login_requests(self, user_password_json):
        self.flag = "Logining"
        self.user_password_json = user_password_json


class MyWindow(QWidget, Ui_Form):
    login_status = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.login_thread = LoginThread(self.login_status)
        self.login_thread.start()

        self.login_status.connect(self.check_login_status)

    @pyqtSlot()
    def on_loginBtn_clicked(self):
        user = self.userEdit.text()
        password = self.passwordEdit.text()

        self.login_thread.login_signal.emit(json.dumps({"user":user, "password":password}))

    def check_login_status(self, status):
        status_dict = json.loads(status)

        if status_dict.get("status") == "200":
            self.login_thread.flag = "Completing"
            self.InfoBrowser.setText("登陆成功！欢迎！")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()
