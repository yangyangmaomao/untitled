import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("RadioButton展示")

        layout = QFormLayout()
        self.button1 = QRadioButton("按钮1")
        self.button1.setCheckable(True)

        self.button2 = QRadioButton("按钮2")
        #self.button2.setCheckable(True)

        self.button1.toggled.connect(self.buttonState)
        self.button2.toggled.connect(self.buttonState)

        layout.addRow(self.button1)
        layout.addRow(self.button2)

        self.setLayout(layout)

    def buttonState(self):
        buttonRadioSender = self.sender()

        if buttonRadioSender.isChecked() == True:
            print('<' + buttonRadioSender.text()+'>被选中')
        else:
            print('<' + buttonRadioSender.text()+'>没有被取消选中状态')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())