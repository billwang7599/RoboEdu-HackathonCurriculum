from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
win = QWidget() # window

# set window pos and win size (x, y, width, height)
win.setGeometry(100, 100, 500, 500)

button = QPushButton('I am a button', win)
label = QLabel('I am a label', win)

button.move(50, 50)
button.setText('hello')
button.resize(100, 100)
print(button.x())

win.show()
sys.exit(app.exec_())

