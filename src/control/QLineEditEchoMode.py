from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('文本输入的回显模式')

        formLayout = QFormLayout()
        Normal = QLineEdit('normal格式')
        NoEcho = QLineEdit('NoEcho格式')
        Password = QLineEdit('Password格式')
        PasswordEchoOnEdit = QLineEdit('PasswordEchoOnEdit格式')

        formLayout.addRow(Normal)
        formLayout.addRow(NoEcho)
        formLayout.addRow(Password)
        formLayout.addRow(PasswordEchoOnEdit)

        Normal.setPlaceholderText("normal模式2")
        NoEcho.setPlaceholderText("NoEcho格式2")
        Password.setPlaceholderText("password格式2")
        PasswordEchoOnEdit.setPlaceholderText("PasswordEchoOnEdit格式2")

        Normal.setEchoMode(QLineEdit.Normal)
        NoEcho.setEchoMode(QLineEdit.NoEcho)
        Password.setEchoMode(QLineEdit.Password)
        PasswordEchoOnEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())
