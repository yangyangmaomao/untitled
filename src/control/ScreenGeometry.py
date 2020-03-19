import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget,QToolTip
from PyQt5.QtGui import QIcon,QFont

def onClick_Button():
    print("我爱你")
    QMessageBox('遇到了一个错误')


app = QApplication(sys.argv)
app.setWindowIcon(QIcon('./kof/A.ICO'))
widget = QWidget()
btn = QPushButton(widget)
btn.setText("新建按钮")
btn.clicked.connect(onClick_Button)
btn.move(75,75)
widget.resize(400,400) #设置工作区的高度，不包含标题栏
widget.move(400,400)
widget.setWindowTitle("标题党")
widget.show()

sys.exit(app.exec_())