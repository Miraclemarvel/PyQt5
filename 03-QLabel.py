import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()

    width = w.width()
    height = w.height()

    w.setWindowTitle("文本")

    # # 下面创建一个Label，然后调用方法指定父类
    # label = QLabel("账号: ", w)
    # # 设置父对象
    # label.setParent(w)

    # 下面创建一个Label（纯文本），在创建的时候指定了父对象
    label = QLabel("账号: ", w)

    # 显示位置与大小 ： x, y , w, h
    label.setGeometry(20, 20, 30, 30)

    w.show()

    app.exec_()