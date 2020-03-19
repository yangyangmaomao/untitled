import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QSpinDemo(QWidget):
    def __init__(self):
        super(QSpinDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QSliderDemo示例")

        layout = QVBoxLayout()
        self.label1 = QLabel("当前值")
        self.label1.setAlignment(Qt.AlignCenter)

        self.sp = QSpinBox()
        self.sp.setMinimum(0)
        self.sp.setMaximum(200)
        self.sp.setValue(50)
        self.sp.valueChanged.connect(self.valuechanged)
        layout.addWidget(self.label1)
        layout.addWidget(self.sp)

        self.setLayout(layout)
    def valuechanged(self):
        self.label1.setText('当前值：'+str(self.sp.value()))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinDemo()
    main.show()
    sys.exit(app.exec_())