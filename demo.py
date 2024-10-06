from PyQt5 import QtWidgets
from PyQt5.QtCore import *
import sys


def getQtVersion() -> str:

    print(QT_VERSION_STR)
    return QT_VERSION_STR


if __name__ == '__main__':
    getQtVersion()

a = ["123", "456", "789"]
print("\n".join(a))
print(sys.version)