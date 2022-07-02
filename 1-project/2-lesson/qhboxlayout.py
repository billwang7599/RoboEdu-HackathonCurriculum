from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget
import sys

app = QApplication(sys.argv)
#screen
screen = QWidget()
layout = QHBoxLayout(screen)
layout.addWidget(QPushButton("Left-Most"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Right-Most"))

screen.setGeometry(100, 100, 500, 500)
screen.show()
sys.exit(app.exec_())