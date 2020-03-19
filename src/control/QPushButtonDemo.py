import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QPushButtonDemo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton')

        layout = QFormLayout()
        self.butt1 = QPushButton('button1')
        self.butt1.setCheckable(False)
        self.butt1.toggle()
        self.butt1.clicked.connect(self.linkAca)
        layout.addRow(self.butt1)

        self.setLayout(layout)

    def linkAca(self):
        print('按下了按钮')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec())