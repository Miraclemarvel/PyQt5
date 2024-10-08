import sys
from tkinter import Widget

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QGroupBox, QMainWindow, QRadioButton,\
    QHBoxLayout


class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.resize(300, 300)
        self.setWindowTitle("垂直布局")

        container = QVBoxLayout()

        hobby_box = QGroupBox("爱好")
        v_layout = QVBoxLayout()
        btn1 = QRadioButton("抽烟")
        btn2 = QRadioButton("喝酒")
        btn3 = QRadioButton("烫头")
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        hobby_box.setLayout(v_layout)

        gender_box = QGroupBox("性别")
        h_layout = QHBoxLayout()
        btn4 = QRadioButton("男")
        btn5 = QRadioButton("女")
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)
        gender_box.setLayout(h_layout)

        container.addWidget(hobby_box)
        container.addWidget(gender_box)



        self.setLayout(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = myWindow()
    w.show()

    app.exec_()