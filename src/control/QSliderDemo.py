import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QSliderDemo示例")

        layout = QVBoxLayout()
        self.label1 = QLabel("这是一个PyQt5程序")
        self.label1.setAlignment(Qt.AlignCenter)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setValue(20)
        self.slider.setMaximum(50)
        self.slider.setMinimum(10)
        self.slider.setSingleStep(5)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.valueChanged.connect(self.valueChange)

        layout.addWidget(self.label1)
        layout.addWidget(self.slider)

        self.setLayout(layout)

    def valueChange(self):
        size = self.sender().value()
        print('当前值：%s' % self.sender().value())
        self.label1.setFont(QFont('Arial',size))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())
