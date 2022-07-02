import sys
from PyQt5.QtWidgets import QApplication, QFormLayout, QPushButton, QWidget, QHBoxLayout, QStackedWidget, QVBoxLayout


# screens
def screen_1():
    screen_1 = QWidget()
    layout = QHBoxLayout(screen_1)

    next_button = QPushButton("next")

    layout.addWidget(QPushButton("Left-Most"))
    layout.addWidget(QPushButton("Center"))
    layout.addWidget(next_button)

    next_button.clicked.connect(next_screen)

    return screen_1


def screen_2():
    screen_2 = QWidget()
    previous_button = QPushButton("Previous")

    layout = QVBoxLayout(screen_2)
    layout.addWidget(QPushButton("Up-Most"))
    layout.addWidget(QPushButton("Center"))
    layout.addWidget(previous_button)

    previous_button.clicked.connect(previous_screen)
    
    return screen_2

# button functions
def next_screen():
    main.setCurrentIndex(main.currentIndex() + 1)

def previous_screen():
    main.setCurrentIndex(main.currentIndex() - 1)

if __name__ == "__main__":
    # main
    app = QApplication(sys.argv)
   
    main = QStackedWidget()
    main.addWidget(screen_1())
    main.addWidget(screen_2())

    main.setGeometry(100, 100, 500, 500)
    main.setCurrentIndex(0)
    main.show()
    sys.exit(app.exec_())