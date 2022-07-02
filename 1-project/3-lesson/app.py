import sys
from PyQt5.QtWidgets import QApplication, QFormLayout, QPushButton, QWidget, QHBoxLayout, QStackedWidget, QVBoxLayout


# functions to initialize different widgets
# each widget is essentially a scene that's shown
def screen_1():
    screen_1 = QWidget()

    layout = QHBoxLayout()

    next_button = QPushButton("next")
    next_button.setStyleSheet('background: blue')

    layout.addWidget(QPushButton("Left-Most"))
    layout.addWidget(QPushButton("Center"))
    layout.addWidget(next_button)
    
    screen_1.setLayout(layout)

    next_button.clicked.connect(next_screen)

    return screen_1


def screen_2():
    screen_2 = QWidget()

    previous_button = QPushButton("Previous")
    previous_button.setStyleSheet('background: green')

    layout = QVBoxLayout()
    layout.addWidget(QPushButton("Up-Most"))
    layout.addWidget(QPushButton("Center"))
    layout.addWidget(previous_button)
        
    screen_2.setLayout(layout)

    previous_button.clicked.connect(previous_screen)
    
    return screen_2

# button functions
def next_screen():
    main.setCurrentIndex(main.currentIndex() + 1)

def previous_screen():
    main.setCurrentIndex(main.currentIndex() - 1)

# main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # sets style to global objects
    # doesn't work for specific buttons since they're not accessible through global scope
    style = '''
    QWidget{
        background: grey;
    }
    QPushButton{
        background: red
    }

    '''

    app.setStyleSheet(style)
    main = QStackedWidget()
    main.addWidget(screen_1())
    main.addWidget(screen_2())

    main.setGeometry(100, 100, 500, 500)
    main.setCurrentIndex(0)
    main.show()
    sys.exit(app.exec_())