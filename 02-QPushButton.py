import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()

    width = w.width()
    height = w.height()

    w.setWindowTitle("按钮")

    btn = QPushButton("点我！")

    btn.setParent(w)

    btn.setGeometry(width/2, height/2, 60, 20)

    w.show()

    app.exec_()