import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget

app = QApplication(sys.argv)
#screen
screen = QWidget()
layout = QVBoxLayout(screen)
layout.addWidget(QPushButton("Up-Most"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Down-Most"))
layout.insertStretch(-1, 1)
layout.insertSpacing(1, 20)

screen.setGeometry(0, 0, 500, 500)
screen.show()

sys.exit(app.exec_())