import sys
from PyQt5.QtWidgets import QApplication, QFormLayout, QPushButton, QWidget, QHBoxLayout, QStackedWidget, QVBoxLayout


# screens
def screen_1():
    screen_1 = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton("Up-Most"), 4)
    layout.addWidget(QPushButton("Center"), 4)
    layout.addWidget(QPushButton("Down-Most"), 2)
    layout.addWidget(sub_widget_1(), 1)    #importing sub widget to main widget screen

    screen_1.setLayout(layout)

    return screen_1

# sub widget
def sub_widget_1():
    sub = QWidget()
    layout = QHBoxLayout()
    layout.addWidget(QPushButton("Left-Most"))
    layout.addWidget(QPushButton("Center"))
    layout.addWidget(QPushButton("Right-Most"))

    sub.setLayout(layout)

    return sub

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
        background: red;
    }
    '''

    app.setStyleSheet(style)
    main = QStackedWidget()
    main.addWidget(screen_1())

    main.setGeometry(100, 100, 500, 500)
    main.setCurrentIndex(0)
    main.show()
    sys.exit(app.exec_())