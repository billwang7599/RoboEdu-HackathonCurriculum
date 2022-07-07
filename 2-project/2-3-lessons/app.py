import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# game variables
word = 'train'

def starting_win():
    win = QWidget()
    layout = QGridLayout(win)
    title = QLabel('Wordle but worse')
    layout.addWidget(title, 2, 2, 1, 2)
    layout.addWidget(QPushButton('Start'), 3, 2)
    layout.addWidget(QPushButton('Quit'), 3, 3)

    # widget alignement
    layout.setRowStretch(2, 2)
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet('font-size: 50px')

    # button functions
    layout.itemAt(1).widget().clicked.connect(start_game)
    layout.itemAt(2).widget().clicked.connect(quit_game)

    # empty space
    layout.setRowStretch(1, 1)
    layout.setRowStretch(4, 1)
    layout.setColumnStretch(1, 1)
    layout.setColumnStretch(4, 1)

    return win

# start screen button functions
def start_game():
    main.setCurrentIndex(main.currentIndex() + 1)

def quit_game():
    app.quit()

# game screen
def game_screen():
    win = QWidget()
    layout = QVBoxLayout(win)

    for i in range(5):
        layout.addWidget(guess_row(i))
    
    submit = QPushButton("Submit")
    layout.addWidget(submit)

    # submit button function
    layout.itemAt(5).widget().clicked.connect(submit_function)

    return win

def guess_row(r):
    win = QWidget()
    layout = QHBoxLayout(win)
    for i in range(5): # creates the guess input boxes
        lineEdit = QLineEdit()
        layout.addWidget(lineEdit)
        if r > 0:
            lineEdit.setEnabled(False) # disables all boxes after first row
        lineEdit.setMaxLength(1)

    return win

# game function
def submit_function():
    global turn # gets the global variable turn since we need to edit turn variable
    row = {}
    correct_word = {}
    row_lay = main.currentWidget().layout().itemAt(turn).widget().layout()
    letter_correct = 0

    for i in range(5): # puts each letter of the correct word and button into a dictionary
        row[i] = row_lay.itemAt(i).widget()
        correct_word[i] = word[i]
    
    for i in range(row_lay.count()):
        if row[i].text().lower() == correct_word[i]: # if at index i the letters are the safe
            row[i].setStyleSheet('background: green;')
            letter_correct += 1
        elif row[i].text().lower() in correct_word.values(): # if one of the guess letter are in the word
            row[i].setStyleSheet('background: yellow;')
        else: # no letters match
            row[i].setStyleSheet('background: red;')
    
    if letter_correct == 5: # win if all 5 letters are right
        win_screen()
    elif turn == 4: # if last turn and press submit and not all letters are right
        lose_screen()

    else:
        turn += 1 # increments turn | not possible without global variable
        for i in range(row_lay.count()): # disables previous buttons and enables the next few buttons
            row_lay.itemAt(i).widget().setEnabled(False)
            main.currentWidget().layout().itemAt(turn).widget().layout().itemAt(i).widget().setEnabled(True)
        
# win screen
def win_screen():
    main.setCurrentIndex(2) # changes to win screen

    win = QWidget()
    layout = QGridLayout(win)
    title = QLabel('You got it! The word was: {}'.format(word.upper()))
    layout.addWidget(title, 2, 2, 1, 2)

    # widget alignement
    layout.setRowStretch(2, 2)
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet('font-size: 50px')

    # empty space
    layout.setRowStretch(1, 1)
    layout.setRowStretch(3, 1)

    return win

def lose_screen():
    main.setCurrentIndex(3) # changes to lose screen

    win = QWidget()
    layout = QGridLayout(win)
    title = QLabel('You lost! The word was: {}'.format(word.upper()))
    layout.addWidget(title, 2, 2, 1, 2)

    # widget alignement
    layout.setRowStretch(2, 2)
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet('font-size: 50px')

    # empty space
    layout.setRowStretch(1, 1)
    layout.setRowStretch(3, 1)

    return win

if __name__ == "__main__":
    app = QApplication(sys.argv)

    turn = 0

    main = QStackedWidget()
    main.addWidget(starting_win())
    main.addWidget(game_screen())
    main.addWidget(win_screen())
    main.addWidget(lose_screen())

    main.setGeometry(50, 50, 500, 500)
    main.show()
    sys.exit(app.exec_())