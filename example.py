from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, \
    QPushButton

import sys
from datetime import datetime


class AgeCalculator(QWidget):
    # Overriding the __init__ in QWidget
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        # This is the gird layout that stores all the other widgets
        grid = QGridLayout()

        # a label that takes the name
        name_label = QLabel("Name: ")
        self.name_line_edit = QLineEdit()

        # a label that takes the date of birth
        date_label = QLabel("Date of Birth MM/DD/YYYY: ")
        self.date_line_edit = QLineEdit()

        # Button that starts the calculation
        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)

        # Outputs the result
        self.output_label = QLabel("")

        # Adding all the widgets into the grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_label, 1, 0)
        grid.addWidget(self.date_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        # sets the grid into a layout to be presented for the user
        self.setLayout(grid)

    def calculate_age(self):
        """Calculates the age of the user"""
        # gets current year
        current_year = datetime.now().year
        date_of_birth = self.date_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year

        # Subtracts the current year from the user's date of birth and displays their age
        age = current_year - year_of_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old")


# Constructs the application
app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
