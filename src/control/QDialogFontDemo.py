import sys
from PyQt5.QtWidgets import *

class QDialogFontDemo(QWidget):
    def __init__(self):
        super(QDialogFontDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QDialogFontDemo演示")

        layout = QVBoxLayout()
        self.button = QPushButton("选择字体")
        self.button.clicked.connect(self.FontChange)
        self.label = QLabel("这是测试字体")
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def FontChange(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogFontDemo()
    main.show()
    sys.exit(app.exec_())
