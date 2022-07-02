import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QWidget

app = QApplication(sys.argv)
#screen
screen = QWidget()

layout = QGridLayout(screen)
layout.addWidget(QLabel("Top-most"), 0, 0, 1, 3) # at row: 0 | column: 0 | spans row*1 column*3
layout.addWidget(QLabel("Left-middle"), 1, 1) # at row: 1 | column: 1 | spans row*1 column*1
layout.addWidget(QLabel("Right-middle"), 1, 2) # at row: 1 | column: 2 | spans row*1 column*1
layout.addWidget(QLabel("Left-bottom"), 2, 0, 1, 2) # at row: 2 | column: 0 | spans row*1 column*2
layout.addWidget(QLabel("Right-Bottom"), 2, 2) # at row: 2 | column: 2 | spans row*1 column*1

screen.setGeometry(0, 0, 500, 500)
screen.show()

app.setStyleSheet('''QLabel{
    background: grey;
}''')

sys.exit(app.exec_())