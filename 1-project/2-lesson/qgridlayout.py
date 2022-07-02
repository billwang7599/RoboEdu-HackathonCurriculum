import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget


app = QApplication(sys.argv)
#screen
screen = QWidget()

layout = QGridLayout(screen)
layout.addWidget(QPushButton("Left-Top"), 1, 1)
layout.addWidget(QPushButton("Left-Botom"), 2, 1)
layout.addWidget(QPushButton("Right-Top"), 1, 2)
layout.addWidget(QPushButton("Right-Bottom"), 2, 2)

screen.setGeometry(0, 0, 500, 500)
screen.show()

sys.exit(app.exec_())