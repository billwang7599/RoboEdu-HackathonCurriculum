from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys


def window():
    win = QMainWindow()

        # window
    # set the title
    win.setWindowTitle("Project 1")

    # set window pos and win size (x, y, width, height)
    win.setGeometry(100, 100, 500, 500)

            # label
    label = QtWidgets.QLabel("0", win)
    label.adjustSize()
    label.move(int(win.width()/2 - label.width()/2), label.height()) # moves label to middle of screen

            # button 
    button = QPushButton("Click me", win)
    button.move(int(win.width()/2 - button.width()/2) , 300)
    # Connect the button to the function
    button.clicked.connect(lambda : button_output(win, label))
    

    win.show()

def button_output(win, text):
    text.setText(str(int(text.text()) + 1))

    # adjust label size so text fits
    text.adjustSize()
    text.move(win.width()/2 - text.width()/2, text.height())

app = QApplication(sys.argv)
window()
sys.exit(app.exec_())
