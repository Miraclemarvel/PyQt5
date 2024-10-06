import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QDial, QSpinBox


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        container = QHBoxLayout()

        self.dial = QDial()
        self.spinBox = QSpinBox()

        container.addWidget(self.dial)
        container.addWidget(self.spinBox)

        self.setLayout(container)

        self.dial.valueChanged.connect(self.on_dial_changed)
        self.spinBox.valueChanged.connect(self.on_spinBox_changed)

    def on_dial_changed(self):
        self.spinBox.setValue(self.dial.value())

    def on_spinBox_changed(self):
        self.dial.setValue(self.spinBox.value())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()


