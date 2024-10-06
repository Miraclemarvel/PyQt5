import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import Qt

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建一个QWidget
    w = QWidget()
    # 设置标题
    w.setWindowTitle("看看我图标帅吗")
    # 设置图标
    w.setWindowIcon(QIcon('cat.jpg'))

    # w.setWindowFlags(Qt.Qt.CustomizeWindowHint) # 去掉标题栏的代码

    # 显示QWidget
    w.show()

    app.exec()