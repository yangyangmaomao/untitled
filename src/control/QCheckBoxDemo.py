import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QCheckBoxDemo示例')
        layout = QHBoxLayout()

        self.checkBox1 = QCheckBox("复选框1")
        self.checkBox1.setChecked(True)
        self.checkBox2 = QCheckBox("复选框2")

        self.checkBox1.stateChanged.connect(self.checkBoxState)
        self.checkBox2.stateChanged.connect(self.checkBoxState)

        layout.addWidget(self.checkBox1)
        layout.addWidget(self.checkBox2)
        self.setLayout(layout)


    def checkBoxState(self):
        self.checkBoxSender = self.sender()
        if self.checkBoxSender.isChecked() == True:
            print(self.checkBoxSender.text()+'被选中')
        else:
            print(self.checkBoxSender.text()+'未被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())