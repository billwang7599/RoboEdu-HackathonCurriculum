from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

            # window
    # set the title
    win.setWindowTitle("Project 1")

    # set window pos and win size (x, y, width, height)
    win.setGeometry(100, 100, 500, 500)
    # set fixed width and height
    win.setFixedWidth(500)
    win.setFixedHeight(500)

            # label
    # prints "Hello world" onto app
    label = QtWidgets.QLabel("test start", win)
    #replaces text with new text 
    label.setText("Start the count!")
    label.setNum(0)
    label.adjustSize()
    label.move(int(win.width()/2 - label.width()/2), label.height()) # moves label to middle of screen

            # button 
    button = QPushButton("Click me", win)
    button.move(int(win.width()/2 - button.width()/2) , 300)
    # Connect the button to the function
    button.clicked.connect(lambda : button_output(win, label))
    

    win.show()
    sys.exit(app.exec_())

def button_output(win, text):
    text.setNum(int(text.text()) + 1)

    # adjust label size so text fits
    text.adjustSize()
    text.move(win.width()/2 - text.width()/2, text.height())

window()
