import sys
from PyQt5.QtWidgets import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QGridLayout(window)

    layout.addWidget(QLineEdit()) # added a widget where we can insert text
    layout.itemAt(0).widget().setPlaceholderText('hello world')

    window.setGeometry(50, 50, 500, 500)
    window.show()
    sys.exit(app.exec_())