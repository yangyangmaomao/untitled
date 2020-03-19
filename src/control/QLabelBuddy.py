import sys
from PyQt5.QtWidgets import *

class QlabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Qlabel与伙伴控件')

        namelabel = QLabel('&Name',self)
        namelineEdit = QLineEdit(self)
        namelabel.setBuddy(namelineEdit)

        passwordlabel = QLabel('&Password',self)
        passwordlineEdit = QLineEdit(self)
        passwordlabel.setBuddy(passwordlineEdit)

        btnok = QPushButton('&OK')
        btncancel = QPushButton('&CANCEL')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(namelabel,0,0)
        mainLayout.addWidget(namelineEdit,0,1,1,2)
        mainLayout.addWidget(passwordlabel,1,0)
        mainLayout.addWidget(passwordlineEdit,1,1,1,2)
        mainLayout.addWidget(btnok,2,0)
        mainLayout.addWidget(btncancel,2,2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlabelBuddy()
    main.show()
    sys.exit(app.exec_())







