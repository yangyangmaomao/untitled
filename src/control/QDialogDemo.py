import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QDialogDemo(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QDialogDemo演示")
        self.resize(300,300)

        self.button = QPushButton("弹出窗口",self)
        self.button.move(150,150)
        self.button.clicked.connect(self.showDialog)
    def showDialog(self):
        dialog = QDialog()
        dialog.move(140,140)
        button = QPushButton('确定',dialog)
        button.clicked.connect(dialog.close)
        dialog.setWindowTitle("提示")
        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())