import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import random as ran

#   starting screen
def starting_menu():
    screen = QMainWindow()
    screen.setCentralWidget(central_widget()) # sets the central widget of the main widget
    return screen

def central_widget():
    central_widget = QWidget()
    layout = QGridLayout(central_widget)

    # layout of central widget
    layout.addWidget(QLabel("Guess the Number!"), 1, 1)
    layout.addWidget(QPushButton("START"), 2, 1)
    layout.setRowStretch(0, 1)
    layout.setRowStretch(3, 1)
    layout.setRowStretch(1, 1)
    layout.setColumnStretch(0, 1)
    layout.setColumnStretch(3, 1)

    # css
    layout.itemAt(0).widget().setStyleSheet('font-size: 50px;') # label
    layout.itemAt(1).widget().setStyleSheet('padding: 10px; font-size: 20px') # start button

    layout.itemAt(1).widget().clicked.connect(start_button_func)

    return central_widget

def start_button_func():
    main.setCurrentIndex(main.currentIndex() + 1)

# game screens
def game_screen():
    screen = QWidget()
    layout = QGridLayout(screen)
    correct = ran.randint(1, 10)

    # layout of game screen
    layout.addWidget(QLabel(': )'), 1, 1)
    layout.addWidget(QLabel('0'), 2, 1)
    layout.addWidget(number_row(), 3, 1)
    layout.setRowStretch(0, 1)
    layout.setRowStretch(4, 1)
    layout.setColumnStretch(0, 1)
    layout.setColumnStretch(3, 1)
    for i in range(2): # label css and alignement
        layout.itemAt(i).widget().setAlignment(Qt.AlignCenter)
        layout.itemAt(i).widget().setStyleSheet('font-size: 30px;')


    # button functions
    '''
    for i in range(layout.itemAt(2).widget().layout().count()):
        btns.addButton(layout.itemAt(2).widget().layout().itemAt(i).widget())
    test = QPushButton("hi")
    layout.addWidget(test)
    btns.addButton(test)
    print(btns.buttons())
    btns.buttonClicked.connect(lambda: print('hello'))
    '''
    layout.itemAt(2).widget().layout().itemAt(0).widget().clicked.connect(lambda:guess_button(layout.itemAt(2).widget().layout().itemAt(0).widget(), layout.itemAt(0).widget(), layout.itemAt(1).widget(), correct))
    layout.itemAt(2).widget().layout().itemAt(1).widget().clicked.connect(lambda:guess_button(layout.itemAt(2).widget().layout().itemAt(1).widget(), layout.itemAt(0).widget(), layout.itemAt(1).widget(), correct))
    layout.itemAt(2).widget().layout().itemAt(2).widget().clicked.connect(lambda:guess_button(layout.itemAt(2).widget().layout().itemAt(2).widget(), layout.itemAt(0).widget(), layout.itemAt(1).widget(), correct))
    layout.itemAt(2).widget().layout().itemAt(3).widget().clicked.connect(lambda:guess_button(layout.itemAt(2).widget().layout().itemAt(3).widget(), layout.itemAt(0).widget(), layout.itemAt(1).widget(), correct))
    layout.itemAt(2).widget().layout().itemAt(4).widget().clicked.connect(lambda:guess_button(layout.itemAt(2).widget().layout().itemAt(4).widget(), layout.itemAt(0).widget(), layout.itemAt(1).widget(), correct))
    layout.itemAt(2).widget().layout().itemAt(5).widget().clicked.connect(lambda:guess_button(layout.itemAt(2).widget().layout().itemAt(5).widget(), layout.itemAt(0).widget(), layout.itemAt(1).widget(), correct))
    layout.itemAt(2).widget().layout().itemAt(6).widget().clicked.connect(lambda:guess_button(layout.itemAt(2).widget().layout().itemAt(6).widget(), layout.itemAt(0).widget(), layout.itemAt(1).widget(), correct))
    layout.itemAt(2).widget().layout().itemAt(7).widget().clicked.connect(lambda:guess_button(layout.itemAt(2).widget().layout().itemAt(7).widget(), layout.itemAt(0).widget(), layout.itemAt(1).widget(), correct))
    layout.itemAt(2).widget().layout().itemAt(8).widget().clicked.connect(lambda:guess_button(layout.itemAt(2).widget().layout().itemAt(8).widget(), layout.itemAt(0).widget(), layout.itemAt(1).widget(), correct))
    layout.itemAt(2).widget().layout().itemAt(9).widget().clicked.connect(lambda:guess_button(layout.itemAt(2).widget().layout().itemAt(9).widget(), layout.itemAt(0).widget(), layout.itemAt(1).widget(), correct))
    return screen

def number_row():
    row = QWidget()
    layout = QHBoxLayout(row)
    for i in range(10):
        layout.addWidget(QPushButton(str(i + 1)))
    return row

    # game functions
def guess_button(button, hint, guess, answer):
    button_number = int(button.text())
    button.setEnabled(False)

    # game logic
    if answer == button_number:
        hint.setText('You got it!')
        button.setStyleSheet('background: green;')
    else:
        button.setStyleSheet('background: red;')
        guess.setNum(int(guess.text()) + 1)
        if answer < button_number:
            hint.setText('Lower!')
        else:
            hint.setText('Higher!')

    pass

if __name__ == "__main__":
    # starts the app
    app = QApplication(sys.argv)

    # css
    css = '''
    QWidget{
        background: #D3D3D3;
    }
    
    '''
    app.setStyleSheet(css)

    # scenes
    main = QStackedWidget()
    main.addWidget(starting_menu())
    main.addWidget(game_screen())
    main.setGeometry(50, 50, 1500, 750)
    main.show()
    sys.exit(app.exec_())