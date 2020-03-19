import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp

class QLineEditValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')
        #创建表单布局
        formLayout = QFormLayout()
        #创建输入框
        intLineEdit =  QLineEdit()
        doubleLineEdit = QLineEdit()
        ValidatorLineEdit = QLineEdit()
        #布局
        formLayout.addRow(intLineEdit)
        formLayout.addRow(doubleLineEdit)
        formLayout.addRow(ValidatorLineEdit)

        #整数校验器

        intvalidator = QIntValidator()
        intvalidator.setRange(1,99)

        #浮点数校验器
        doubleValidator = QDoubleValidator()
        doubleValidator.setRange(-360,360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)

        #设置校验器
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator()
        validator.setRegExp(reg)

        intLineEdit.setValidator(intvalidator)
        doubleLineEdit.setValidator(doubleValidator)
        ValidatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())




