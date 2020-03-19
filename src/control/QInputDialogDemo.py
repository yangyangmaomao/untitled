import sys
from PyQt5.QtWidgets import *

class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QInputDialogDemo演示")

        layout = QGridLayout()

        self.button1 = QPushButton("获取列表中的选项")
        self.lineEdit1 = QLineEdit()
        self.button2 = QPushButton("获取字符串")
        self.lineEdit2 = QLineEdit()
        self.button3 = QPushButton("获取整数")
        self.lineEdit3 = QLineEdit()
        layout.addWidget(self.button1,0,0)
        layout.addWidget(self.lineEdit1,0,1)
        layout.addWidget(self.button2,1,0)
        layout.addWidget(self.lineEdit2,1,1)
        layout.addWidget(self.button3,2,0)
        layout.addWidget(self.lineEdit3,2,1)

        self.button1.clicked.connect(self.getItem)
        self.button2.clicked.connect(self.getText)
        self.button3.clicked.connect(self.getInt)

        self.setLayout(layout)
    def getItem(self):
        items = ('python','c','c++','c#','java','Ruby')
        #ok这个变量是用来表示对话框中的OK键是否被按下，如果按下就返回True，否则返回False
        item,ok = QInputDialog.getItem(self,"获取列表中的选项","请选择语言",items)
        if item and ok:
            self.lineEdit1.setText(item)
    def getText(self):
        text,ok = QInputDialog.getText(self,"文本输入框","输入姓名")
        if text:
            self.lineEdit2.setText(text)
    def getInt(self):
        num,ok = QInputDialog.getInt(self,"整数输入框","输入数字")
        if num:
            self.lineEdit3.setText(str(num))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())
