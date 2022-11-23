from calculator import Screen
from PyQt5 import QtCore
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


# ---------------------------------------------------- MAIN APP ----------------------------------------------------- #

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        self.ui = Screen()
        self.ui.setupUi(self)

        # ---------------------- SETUP --------------------- #

        self.numbers = ""
        self.op = ""
        self.history = ""
        self.result = None
        self.clear = False
        self.comma = False
        self.division_error = False
        self.numbers_shown = ""

        # -------------- TO ADJUST FONT SIZE ---------------- #

        self.font = self.ui.digits.font()
        self.font.pointSize = 39
        self.font.setPointSize(self.font.pointSize)
        self.metrics = QFontMetrics(self.font)
        self.width = self.metrics.width("999.999.999")

        # -------------------- BUTTONS --------------------- #

        # Texting

        self.ui.btn0.clicked.connect(self.texts)
        self.ui.btn1.clicked.connect(self.texts)
        self.ui.btn2.clicked.connect(self.texts)
        self.ui.btn3.clicked.connect(self.texts)
        self.ui.btn4.clicked.connect(self.texts)
        self.ui.btn5.clicked.connect(self.texts)
        self.ui.btn6.clicked.connect(self.texts)
        self.ui.btn7.clicked.connect(self.texts)
        self.ui.btn8.clicked.connect(self.texts)
        self.ui.btn9.clicked.connect(self.texts)
        self.ui.btncomma.clicked.connect(self.texts)

        # Operation

        self.ui.btnplus.clicked.connect(self.operation)
        self.ui.btnmin.clicked.connect(self.operation)
        self.ui.btndiv.clicked.connect(self.operation)
        self.ui.btnmul.clicked.connect(self.operation)
        self.ui.btnmod.clicked.connect(self.operation)

        self.ui.btneq.clicked.connect(self.show_result)

        # Clear

        self.ui.btnc.clicked.connect(self.delete)
        self.ui.btnce.clicked.connect(self.delete)
        self.ui.btndel.clicked.connect(self.delete)

    # --------------------------------------------- KEY PRESS EVENTS ------------------------------------------------ #

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_0:
            self.ui.btn0.click()
        elif event.key() == QtCore.Qt.Key_1:
            self.ui.btn1.click()
        elif event.key() == QtCore.Qt.Key_2:
            self.ui.btn2.click()
        elif event.key() == QtCore.Qt.Key_3:
            self.ui.btn3.click()
        elif event.key() == QtCore.Qt.Key_4:
            self.ui.btn4.click()
        elif event.key() == QtCore.Qt.Key_5:
            self.ui.btn5.click()
        elif event.key() == QtCore.Qt.Key_6:
            self.ui.btn6.click()
        elif event.key() == QtCore.Qt.Key_7:
            self.ui.btn7.click()
        elif event.key() == QtCore.Qt.Key_8:
            self.ui.btn8.click()
        elif event.key() == QtCore.Qt.Key_9:
            self.ui.btn9.click()
        elif event.key() == QtCore.Qt.Key_Comma:
            self.ui.btncomma.click()
        elif event.key() == QtCore.Qt.Key_Plus:
            self.ui.btnplus.click()
        elif event.key() == QtCore.Qt.Key_Minus:
            self.ui.btnmin.click()
        elif event.key() == QtCore.Qt.Key_Asterisk:
            self.ui.btnmul.click()
        elif event.key() == QtCore.Qt.Key_Slash:
            self.ui.btndiv.click()
        elif event.key() == QtCore.Qt.Key_Return:
            self.ui.btneq.click()
        elif event.key() == QtCore.Qt.Key_Backspace:
            self.ui.btndel.click()
        elif event.key() == QtCore.Qt.Key_Delete:
            self.ui.btnce.click()
        elif event.key() == QtCore.Qt.Key_Escape:
            self.ui.btnc.click()

        event.accept()

    # --------------------------------------------- DELETE BUTTONS ------------------------------------------------ #

    def delete(self):

        btn = self.sender()

        # ---------------------------- Delete Everything ---------------------------- #

        if btn.text() == "C":
            self.ui.result.clear()
            self.ui.digits.clear()
            self.numbers = ""
            self.op = ""
            self.division = ""
            self.result = None
            self.comma = False
            self.font.setPointSize(39)
            self.ui.digits.setFont(self.font)

        # ----------------------------- Delete Digits ------------------------------ #

        elif btn.text() == "CE":
            self.ui.digits.clear()
            self.numbers = ""
            self.comma = False
            self.font.setPointSize(39)
            self.ui.digits.setFont(self.font)

        # -------------------------- Delete Last Digits ---------------------------- #

        else:
            self.numbers = self.numbers[:-1]
            if "." not in self.numbers:  # To check if comma is deleted and reused again
                self.comma = False
            self.number_to_show()
            self.font_size()

    # ------------------------------------------------- TEXTING ---------------------------------------------------- #

    def texts(self):
        if len(self.numbers) <= 14:  # You can calculate maximum 15 digit numbers.
            btn = self.sender()

            if btn.text() == ",":
                if not self.comma:  # If comma is not used already
                    self.numbers += "."
                    self.comma = True
            else:
                self.numbers += btn.text()

            self.number_to_show()
            self.font_size()

            if self.clear:  # If we calculated something already, clear the history.
                self.ui.result.clear()
                self.clear = False

    # --------------------------------------------- NUMBERS TO SHOW ------------------------------------------------ #

    def number_to_show(self):
        self.numbers_shown = ""  # Clear everytime the function is called.

        # Split numbers if comma exist, so that we can reformat the part before comma adding "." after every digit.
        if "." in self.numbers:
            left = self.numbers.split(".")[0]
            right = "," + self.numbers.split(".")[1]
        else:
            left = self.numbers
            right = ""

        # Add "." after every number. "3456987,78276" -> "3.456.987,78276"
        count = 1
        add = False  # If True add dot in the next iteration.

        for i in left[::-1]:  # From right to left, if digits is 3x add dot.
            if count % 3 == 0:
                add = True
                self.numbers_shown += i
                count += 1
            else:
                if add:
                    self.numbers_shown += "." + i
                    add = False
                    count = -1
                else:
                    self.numbers_shown += i
                    count += 1

        self.numbers_shown = self.numbers_shown[::-1] + right  # Reverse of numbers_shon + float points (if not empty)
        self.ui.digits.setText(self.numbers_shown)

    # ----------------------------------------- ADJUST DYNAMIC FONT SIZE ------------------------------------------- #

    def font_size(self):
        if len(self.ui.digits.text()) == 0:  # If there is no numbers set font size back to 39
            self.font.setPointSize(39)

        width = self.metrics.width(self.ui.digits.text())

        if width < self.width:  # If the width is less than "999.999.999"
            self.font.setPointSize(39)
        else:
            rate = self.width / width  # If not, the new font size is = font size * old width / new width
            self.font.setPointSize(int(self.font.pointSize * rate))

        self.ui.digits.setFont(self.font)
        self.ui.digits.setText(self.ui.digits.text())

    # ----------------------------------------------- CALCULATIONS -------------------------------------------------- #

    def operation(self):

        if self.clear:  # If we calculated something already, clear the history.
            self.ui.result.clear()
            self.clear = False

        if self.result is not None:  # If there is already a value in result, old number
            if self.op:  # And if an operation is already exist
                if self.numbers:  # If you typed any number, new numbers

                    self.calc()  # Calculate
                    self.op = ""  # Clear operation after using

        else:  # If there is no result value create one

            if self.numbers:  # If there is numbers, result is float(number)
                self.result = float(self.numbers)
            else:
                self.result = 0  # If not it is just 0

        op = self.sender()  # New operation
        self.op = op.text()

        # ----- CONVERTING INTEGER ----- #

        if float(self.result).is_integer():  # If the result can be integer, convert it
            self.result = int(self.result)

        # ------- ZERO DIVISION -------- #

        if self.division_error:  # If there is a zero division error
            self.error()

        else:  # If everything wen right show the new history.
            self.ui.result.setText(str(self.result) + " " + self.op)

        # Clear new numbers
        self.numbers = ""
        self.comma = False

    # ------------------------------------------- ZERO DIVISION ERROR ---------------------------------------------- #

    def error(self):
        self.ui.result.setText(str(self.result) + " " + self.op + " " + self.numbers + " = ")
        self.ui.digits.setText("Cannot divide by zero!")
        self.font_size()
        self.reset()

    # --------------------------------------------- RESET EVERYTHING ----------------------------------------------- #

    def reset(self):
        # Clear every history

        self.numbers = ""
        self.op = ""
        self.result = None
        self.clear = True
        self.comma = False
        self.division_error = False

    # ------------------------------------------------ CALCULATE --------------------------------------------------- #

    def calc(self):
        if self.op == "+":
            self.result += float(self.numbers)
        elif self.op == "-":
            self.result -= float(self.numbers)
        elif self.op == "x":
            self.result *= float(self.numbers)
        elif self.op == "÷":
            try:
                self.result /= float(self.numbers)
            except ZeroDivisionError:
                self.division_error = True
        else:
            try:
                self.result %= float(self.numbers)
            except ZeroDivisionError:
                self.division_error = True

    # ----------------------------------------------- SHOW RESULT -------------------------------------------------- #

    def show_result(self):

        if self.result is None:  # If there is nothing, pass.
            if not self.numbers:
                pass

            else:  # If there is no result already, show the numbers, if it's just a comma, pass
                if self.numbers_shown == ",":
                    pass
                else:
                    self.ui.digits.setText(self.numbers_shown)
                    self.ui.result.setText(self.numbers_shown + " = ")

        else:
            if not self.numbers:  # If there is a result and an operation but not a number is written

                # Change the last operation to equal sign and show result in the valid format
                self.ui.result.setText(str(self.result) + " = ")
                self.numbers = str(self.result)
                self.number_to_show()
                self.ui.digits.setText(self.numbers_shown)

            else:

                self.ui.result.setText(str(self.result) + " " + self.op + " " + self.numbers + " = ")  # Show history
                self.calc()  # Last calculation

                if float(self.result).is_integer():
                    self.result = int(self.result)

                # ------- ZERO DIVISION -------- #

                if self.division_error:  # If there is a zero division error
                    self.error()

                else:  # If everything wen right show the new history.
                    self.numbers = str(self.result)
                    self.number_to_show()
                    self.font_size()

                    self.ui.digits.setText(self.numbers_shown)

        self.reset()  # Reset everything at the end of the calculation


# ------------------------------------------------- RUN APPLICATION ------------------------------------------------- #

def application():
    win = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(win.exec_())


application()
