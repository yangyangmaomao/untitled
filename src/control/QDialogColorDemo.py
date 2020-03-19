import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class QDialogColorDemo(QWidget):
    def __init__(self):
        super(QDialogColorDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QDialogColorDemo演示")

        layout = QVBoxLayout()
        self.button = QPushButton("选择颜色")
        self.button.clicked.connect(self.ColorChange)
        self.label = QLabel("这是测试文字")
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def ColorChange(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText,color)
        self.label.setPalette(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogColorDemo()
    main.show()
    sys.exit(app.exec_())
