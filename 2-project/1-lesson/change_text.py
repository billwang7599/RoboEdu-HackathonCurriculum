import sys
from PyQt5.QtWidgets import *

def change_text():
    child_layout = parent_layout.itemAt(0).widget().layout()
    child_label = child_layout.itemAt(0).widget()
    child_line_edit = child_layout.itemAt(2).widget()
    
    child_label.setText(child_line_edit.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # parent screen
    parent = QWidget()
    parent_layout = QGridLayout(parent)
    

    # child widget
    child = QWidget()
    child_layout = QHBoxLayout(child)

    parent_layout.addWidget(child) # adds horizontal box to grid


    # child widget's widgets
    child_layout.addWidget(QLabel("Hello world!"))
    child_layout.addWidget(QPushButton("Click me to change text"))
    child_layout.addWidget(QLineEdit(""))

        # widget functions
    parent_layout.itemAt(0).widget().layout().itemAt(1).widget().clicked.connect(lambda : change_text())

    parent.setGeometry(50, 50, 500, 500)
    parent.show()
    sys.exit(app.exec_())