import sys
from PyQt5.QtWidgets import QApplication, QFormLayout, QPushButton, QWidget

app = QApplication(sys.argv)
#screen
screen = QWidget()

layout = QFormLayout(screen)
layout.addRow("Row 1", QPushButton("Button 1"))
layout.addRow("Row 2", QPushButton("Button 2"))
layout.addRow("Row 3", QPushButton("Button 3"))


screen.setGeometry(0, 0, 500, 500)
screen.show()

sys.exit(app.exec_())