import sys

from PyQt5.QtWidgets import QApplication, QWidget

import demo
from demo import getQtVersion

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()

    w.setWindowTitle("第一个PyQt")

    w.show()

    app.exec_()
