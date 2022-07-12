import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import json
import random

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

    for i in range(6):
        layout.addWidget(guess_row(i))
    
    submit = QPushButton("Submit")
    layout.addWidget(submit)

    # submit button function
    layout.itemAt(6).widget().clicked.connect(submit_function)

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
        if row[i].text().lower() == correct_word[i].lower(): # if at index i the letters are the safe
            row[i].setStyleSheet('background: green;')
            letter_correct += 1
        elif row[i].text().lower() in correct_word.values(): # if one of the guess letter are in the word
            row[i].setStyleSheet('background: yellow;')
        else: # no letters match
            row[i].setStyleSheet('background: red;')
    
    if letter_correct == 5: # win if all 5 letters are right
        win_screen()
    elif turn == 5: # if last turn and press submit and not all letters are right
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

    # name
    name = QLineEdit()
    layout.addWidget(name, 3, 3)
    name.setPlaceholderText("Insert name here")

    # button
    winners = QPushButton("Submit and see previous winners")
    layout.addWidget(winners, 3, 2)
    winners.clicked.connect(lambda: see_winners(name.text()))

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

# winners screen
def see_winners(winner_name):
    # add name to data
    json_file = open("data.json", "r+")
    names = json.load(json_file)
    names["winners"].append(winner_name)
    json_file.seek(0)
    json.dump(names, json_file, indent = 4)
    json_file.close()

    main.setCurrentIndex(4) # moves to winners screen

def winners_screen():
    win = QWidget()
    layout = QVBoxLayout(win)
    json_file = open("data.json")
    names = json.load(json_file)["winners"]
    json_file.close()
    for name in names:
        layout.addWidget(QLabel(name))
    
    layout.insertStretch(-1, 1)

    return win

# data manipulation | JSON
def load_json():
    json_file = open('data.json') # opens the json file
    words = json.load(json_file)["5_letter_words"] # stores the word list into the variable words
    word = words[random.randint(0, len(words) - 1)]
    json_file.close()

    return word

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # game variables
    word = load_json()
    turn = 0
    print(word)

    # app screens
    main = QStackedWidget()
    main.addWidget(starting_win())
    main.addWidget(game_screen())
    main.addWidget(win_screen())
    main.addWidget(lose_screen())
    main.addWidget(winners_screen())

    main.setGeometry(50, 50, 500, 500)
    main.show()
    sys.exit(app.exec_())

