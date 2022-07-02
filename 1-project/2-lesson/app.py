import sys
from PyQt5.QtWidgets import QApplication, QFormLayout, QPushButton, QWidget

def window():
    app = QApplication(sys.argv)
    #screen
    screen_2 = QWidget()

    layout = QFormLayout()
    layout.addRow("Row 1", QPushButton("Button 1"))
    layout.addRow("Row 2", QPushButton("Button 2"))
    layout.addRow("Row 3", QPushButton("Button 3"))
    
    screen_2.setLayout(layout)
    screen_2.setGeometry(0, 0, 500, 500)
    screen_2.show()
    sys.exit(app.exec_())

window()

'''
    main_screen = QStackedWidget()
    main_screen.addWidget(screen_2)
    main_screen.addWidget(win)

    main_screen.setGeometry(100, 100, 500, 500)
    main_screen.show()
    '''