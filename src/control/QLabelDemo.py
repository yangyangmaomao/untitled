import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QMainWindow,QLabel
from PyQt5.QtGui import QPalette,QPixmap
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel()
        label2 = QLabel()
        label3 = QLabel()
        label4 = QLabel()

        label1.setText("这是一个文本标签")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.white)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href = 'www.baidu.com'>感谢支持本软件</a>")

        label1.linkHovered.connect(self.linkHovered)
        label2.setOpenExternalLinks(True)
        label2.linkActivated.connect(self.linkClick)

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)

        self.setLayout(vbox)


    def linkHovered(self):
        print('鼠标滑过')

    def linkClick(self):
        print('鼠标点击')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QLabelDemo()
    mainwindow.show()
    sys.exit(app.exec_())