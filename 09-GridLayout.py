import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, \
    QGridLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()


    def initUi(self):
        self.resize(300, 300)
        self.setWindowTitle("计算器")

        data = {
            0: ["7", "8", "9", "+", "("],
            1: ["4", "5", "6", "-", ")"],
            2: ["1", "2", "3", "*", "<-"],
            3: ["0", ".", "=", "/", "C"]
        }

        container = QVBoxLayout()

        edit = QLineEdit()
        edit.setPlaceholderText("请输入内容")
        container.addWidget(edit)

        grid = QGridLayout()

        for row, line_data in data.items():
            for col, number in enumerate(line_data):
                btn = QPushButton(number)
                grid.addWidget(btn, row, col)

        container.addLayout(grid)

        self.setLayout(container)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()