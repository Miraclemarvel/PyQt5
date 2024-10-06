import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = uic.loadUi("./test_1.ui")
    ui.show()

    app.exec_()