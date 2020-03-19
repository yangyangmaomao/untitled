import sys
from PyQt5.QtWidgets import *

class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QComboBoxDemo示例")
        layout = QVBoxLayout()

        self.label1 = QLabel("示例")
        self.cb = QComboBox()
        self.cb.addItems(['python','java','c','c++','c#','ruby'])
        self.cb.currentIndexChanged.connect(self.currentIndexChanged)

        layout.addWidget(self.label1)
        layout.addWidget(self.cb)

        self.setLayout(layout)

    def currentIndexChanged(self):
        self.label1.setText(self.cb.currentText())
        for i in range(self.cb.count()):
            print('you choose No.'+str(i)+':'+self.cb.currentText()+',total number:'+str(self.cb.count()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())
