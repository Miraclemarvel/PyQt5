import sys
import time

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QTextTable
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLabel, QVBoxLayout, QTextEdit


class MyWindow(QWidget):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedWidth(500)
        self.setFixedHeight(500)

        self.text = QTextEdit(self)
        self.text.setGeometry(48,20,400,350)


        btn = QPushButton("开始检测",self)
        btn.setGeometry(200, 400, 100, 40)
        btn.clicked.connect(self.check)

        self.my_signal.connect(self.my_slot)

    def my_slot(self, msg):
        print(msg)
        self.text.append(msg)

    def check(self):
        for index, ip in enumerate(["192.168.1.%d" %x for x in range(1, 255)]):
            msg = "正在检测" + ip + "上的漏洞"
            print(msg)
            self.text.append(msg)
            if index % 5 == 0:
                msg += ", 发现漏洞！"
                self.my_signal.emit(msg)
            time.sleep(0.01)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()