import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

# button function
def button_function(new_name):
    with open("exercise.json", "r+") as json_file:
        data = json.load(json_file)
        data["names"].append(new_name)
        json_file.seek(0)
        json.dump(data, json_file, indent = 4)

app = QApplication(sys.argv)
# app screens
main = QWidget()
layout = QVBoxLayout(main)

# get data from JSON
with open("exercise.json") as json_file:
    data = json.load(json_file)["names"]

for name in data:
    layout.addWidget(QLabel(name))
input = QLineEdit()
submit = QPushButton("Submit")
layout.addWidget(input)
layout.addWidget(submit)
layout.addStretch(1)
submit.clicked.connect(lambda: button_function(input.text())) # connect to button function

main.setGeometry(50, 50, 500, 500)
main.show()
sys.exit(app.exec_())