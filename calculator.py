from PyQt5 import QtCore, QtGui, QtWidgets


class Screen(object):
    def __init__(self):
        self.result = None
        self.btn8 = None
        self.btnmin = None
        self.btndel = None
        self.btn4 = None
        self.btn3 = None
        self.btn9 = None
        self.btn7 = None
        self.btn6 = None
        self.btneq = None
        self.digits = None
        self.btn2 = None
        self.btn1 = None
        self.btnmul = None
        self.btn0 = None
        self.btnmod = None
        self.btnc = None
        self.btnce = None
        self.btncomma = None
        self.btn5 = None
        self.btndiv = None
        self.btnplus = None
        self.gridLayout = None
        self.gridLayoutWidget = None
        self.centralwidget = None

    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(511, 687)
        Window.setFixedSize(511, 687)
        Window.setLayoutDirection(QtCore.Qt.LeftToRight)
        Window.setStyleSheet("background-color: rgb(27, 27, 27);\n")
        Window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 230, 392, 411))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.btnplus = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnplus.sizePolicy().hasHeightForWidth())
        self.btnplus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnplus.setFont(font)
        self.btnplus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnplus.setStyleSheet("QPushButton {\n"
                                   "background-color: rgb(40, 40, 40);\n"
                                   "color: rgb(0, 100, 255);\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "background-color: rgb(25, 25, 25);\n"
                                   "color: rgb(50, 150, 255);\n"
                                   "}\n")
        self.btnplus.setObjectName("btnplus")
        self.gridLayout.addWidget(self.btnplus, 4, 3, 1, 1)
        self.btndiv = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btndiv.sizePolicy().hasHeightForWidth())
        self.btndiv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btndiv.setFont(font)
        self.btndiv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btndiv.setStyleSheet("QPushButton {\n"
                                  "background-color: rgb(40, 40, 40);\n"
                                  "color: rgb(0, 100, 255);\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "background-color: rgb(25, 25, 25);\n"
                                  "color: rgb(50, 150, 255);\n"
                                  "}\n")
        self.btndiv.setObjectName("btndiv")
        self.gridLayout.addWidget(self.btndiv, 0, 3, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn5.setFont(font)
        self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn5.setStyleSheet("QPushButton {\n"
                                "background-color: rgb(54, 54, 54);\n"
                                "color: rgb(0, 255, 0);\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "background-color: rgb(30, 30, 30);\n"
                                "color: rgb(50, 255, 50);\n"
                                "}\n"
                                "")
        self.btn5.setObjectName("btn5")
        self.gridLayout.addWidget(self.btn5, 2, 1, 1, 1)
        self.btndel = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btndel.sizePolicy().hasHeightForWidth())
        self.btndel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btndel.setFont(font)
        self.btndel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btndel.setStyleSheet("QPushButton {\n"
                                  "background-color: rgb(40, 40, 40);\n"
                                  "color: rgb(0, 100, 255);\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "background-color: rgb(25, 25, 25);\n"
                                  "color: rgb(50, 150, 255);\n"
                                  "}\n"
                                  "")
        self.btndel.setObjectName("btndel")
        self.gridLayout.addWidget(self.btndel, 0, 0, 1, 1)
        self.btncomma = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btncomma.sizePolicy().hasHeightForWidth())
        self.btncomma.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btncomma.setFont(font)
        self.btncomma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btncomma.setStyleSheet("QPushButton {\n"
                                    "background-color: rgb(54, 54, 54);\n"
                                    "color: rgb(255, 170, 0);\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "background-color: rgb(30, 30, 30);\n"
                                    "color: rgb(255, 217, 0);\n"
                                    "}\n"
                                    "")
        self.btncomma.setObjectName("btncomma")
        self.gridLayout.addWidget(self.btncomma, 6, 2, 1, 1)
        self.btnmod = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnmod.sizePolicy().hasHeightForWidth())
        self.btnmod.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnmod.setFont(font)
        self.btnmod.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnmod.setStyleSheet("QPushButton {\n"
                                  "background-color: rgb(54, 54, 54);\n"
                                  "color: rgb(255, 170, 0);\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "background-color: rgb(30, 30, 30);\n"
                                  "color: rgb(255, 217, 0);\n"
                                  "}\n"
                                  "")
        self.btnmod.setObjectName("btnmod")
        self.gridLayout.addWidget(self.btnmod, 6, 0, 1, 1)
        self.btneq = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btneq.sizePolicy().hasHeightForWidth())
        self.btneq.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btneq.setFont(font)
        self.btneq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btneq.setStyleSheet("QPushButton {\n"
                                 "    background-color: rgb(255, 170, 0);\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: rgb(255, 217, 0);\n"
                                 "}")
        self.btneq.setObjectName("btneq")
        self.gridLayout.addWidget(self.btneq, 6, 3, 1, 1)
        self.btnc = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnc.sizePolicy().hasHeightForWidth())
        self.btnc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnc.setFont(font)
        self.btnc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnc.setStyleSheet("QPushButton {\n"
                                "background-color: rgb(40, 40, 40);\n"
                                "color: rgb(0, 100, 255);\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "background-color: rgb(25, 25, 25);\n"
                                "color: rgb(50, 150, 255);\n"
                                "}\n"
                                "")
        self.btnc.setObjectName("btnc")
        self.gridLayout.addWidget(self.btnc, 0, 1, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn6.setFont(font)
        self.btn6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn6.setStyleSheet("QPushButton {\n"
                                "background-color: rgb(54, 54, 54);\n"
                                "color: rgb(0, 255, 0);\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "background-color: rgb(30, 30, 30);\n"
                                "color: rgb(50, 255, 50);\n"
                                "}\n"
                                "")
        self.btn6.setObjectName("btn6")
        self.gridLayout.addWidget(self.btn6, 2, 2, 1, 1)
        self.btn0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn0.sizePolicy().hasHeightForWidth())
        self.btn0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn0.setFont(font)
        self.btn0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn0.setStyleSheet("QPushButton {\n"
                                "background-color: rgb(54, 54, 54);\n"
                                "color: rgb(0, 255, 0);\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "background-color: rgb(30, 30, 30);\n"
                                "color: rgb(50, 255, 50);\n"
                                "}\n"
                                "")
        self.btn0.setObjectName("btn0")
        self.gridLayout.addWidget(self.btn0, 6, 1, 1, 1)
        self.btnmin = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnmin.sizePolicy().hasHeightForWidth())
        self.btnmin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnmin.setFont(font)
        self.btnmin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnmin.setStyleSheet("QPushButton {\n"
                                  "background-color: rgb(40, 40, 40);\n"
                                  "color: rgb(0, 100, 255);\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "background-color: rgb(25, 25, 25);\n"
                                  "color: rgb(50, 150, 255);\n"
                                  "}\n"
                                  "")
        self.btnmin.setObjectName("btnmin")
        self.gridLayout.addWidget(self.btnmin, 2, 3, 1, 1)
        self.btnmul = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnmul.sizePolicy().hasHeightForWidth())
        self.btnmul.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btnmul.setFont(font)
        self.btnmul.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnmul.setStyleSheet("QPushButton {\n"
                                  "background-color: rgb(40, 40, 40);\n"
                                  "color: rgb(0, 100, 255);\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "background-color: rgb(25, 25, 25);\n"
                                  "color: rgb(50, 150, 255);\n"
                                  "}\n"
                                  "")
        self.btnmul.setObjectName("btnmul")
        self.gridLayout.addWidget(self.btnmul, 1, 3, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn4.setFont(font)
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn4.setStyleSheet("QPushButton {\n"
                                "background-color: rgb(54, 54, 54);\n"
                                "color: rgb(0, 255, 0);\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "background-color: rgb(30, 30, 30);\n"
                                "color: rgb(50, 255, 50);\n"
                                "}\n"
                                "")
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 2, 0, 1, 1)
        self.btnce = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnce.sizePolicy().hasHeightForWidth())
        self.btnce.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnce.setFont(font)
        self.btnce.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnce.setStyleSheet("QPushButton {\n"
                                 "background-color: rgb(40, 40, 40);\n"
                                 "color: rgb(0, 100, 255);\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "background-color: rgb(25, 25, 25);\n"
                                 "color: rgb(50, 150, 255);\n"
                                 "}\n"
                                 "")
        self.btnce.setObjectName("btnce")
        self.gridLayout.addWidget(self.btnce, 0, 2, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn7.setFont(font)
        self.btn7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn7.setStyleSheet("QPushButton {\n"
                                "background-color: rgb(54, 54, 54);\n"
                                "color: rgb(0, 255, 0);\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "background-color: rgb(30, 30, 30);\n"
                                "color: rgb(50, 255, 50);\n"
                                "}\n"
                                "")
        self.btn7.setObjectName("btn7")
        self.gridLayout.addWidget(self.btn7, 1, 0, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn1.setStyleSheet("QPushButton {\n"
                                "background-color: rgb(54, 54, 54);\n"
                                "color: rgb(0, 255, 0);\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "background-color: rgb(30, 30, 30);\n"
                                "color: rgb(50, 255, 50);\n"
                                "}\n"
                                "")
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 4, 0, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn8.setFont(font)
        self.btn8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn8.setStyleSheet("QPushButton {\n"
                                "background-color: rgb(54, 54, 54);\n"
                                "color: rgb(0, 255, 0);\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "background-color: rgb(30, 30, 30);\n"
                                "color: rgb(50, 255, 50);\n"
                                "}\n"
                                "")
        self.btn8.setObjectName("btn8")
        self.gridLayout.addWidget(self.btn8, 1, 1, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn2.setStyleSheet("QPushButton {\n"
                                "background-color: rgb(54, 54, 54);\n"
                                "color: rgb(0, 255, 0);\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "background-color: rgb(30, 30, 30);\n"
                                "color: rgb(50, 255, 50);\n"
                                "}\n"
                                "")
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 4, 1, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn9.setFont(font)
        self.btn9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn9.setStyleSheet("QPushButton {\n"
                                "background-color: rgb(54, 54, 54);\n"
                                "color: rgb(0, 255, 0);\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "background-color: rgb(30, 30, 30);\n"
                                "color: rgb(50, 255, 50);\n"
                                "}\n"
                                "")
        self.btn9.setObjectName("btn9")
        self.gridLayout.addWidget(self.btn9, 1, 2, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn3.setFont(font)
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn3.setStyleSheet("QPushButton {\n"
                                "background-color: rgb(54, 54, 54);\n"
                                "color: rgb(0, 255, 0);\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "background-color: rgb(30, 30, 30);\n"
                                "color: rgb(50, 255, 50);\n"
                                "}\n"
                                "")
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 4, 2, 1, 1)
        self.digits = QtWidgets.QLineEdit(self.centralwidget)
        self.digits.setGeometry(QtCore.QRect(60, 100, 391, 101))
        font = QtGui.QFont()
        font.setPointSize(39)
        self.digits.setFont(font)
        self.digits.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.digits.setFocusPolicy(QtCore.Qt.NoFocus)
        self.digits.setStyleSheet("color: rgb(0, 255, 0);\n"
                                  "background-color: rgb(0, 0, 0);\n"
                                  "padding: 10px 10px 10px 10px;\n"
                                  "border: 1px solid green;\n"
                                  "border-top: 0;")
        self.digits.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.digits.setProperty("point", "")
        self.digits.setObjectName("digits")
        self.result = QtWidgets.QLineEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(60, 60, 391, 41))
        self.result.setStyleSheet("color: rgb(0, 170, 0);\n"
                                  "background-color: rgb(0, 0, 0);\n"
                                  "padding: 10px 10px 10px 10px;\n"
                                  "border: 1px solid green;\n"
                                  "border-bottom: 0;")
        self.result.setReadOnly(True)
        self.result.setPlaceholderText("")
        self.result.setObjectName("result")
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Basic Calculator"))
        self.btnplus.setText(_translate("Window", "+"))
        self.btndiv.setText(_translate("Window", "÷"))
        self.btn5.setText(_translate("Window", "5"))
        self.btndel.setText(_translate("Window", "Delete"))
        self.btncomma.setText(_translate("Window", ","))
        self.btnmod.setText(_translate("Window", "%"))
        self.btneq.setText(_translate("Window", "="))
        self.btnc.setText(_translate("Window", "C"))
        self.btn6.setText(_translate("Window", "6"))
        self.btn0.setText(_translate("Window", "0"))
        self.btnmin.setText(_translate("Window", "-"))
        self.btnmul.setText(_translate("Window", "x"))
        self.btn4.setText(_translate("Window", "4"))
        self.btnce.setText(_translate("Window", "CE"))
        self.btn7.setText(_translate("Window", "7"))
        self.btn1.setText(_translate("Window", "1"))
        self.btn8.setText(_translate("Window", "8"))
        self.btn2.setText(_translate("Window", "2"))
        self.btn9.setText(_translate("Window", "9"))
        self.btn3.setText(_translate("Window", "3"))
        self.digits.setPlaceholderText(_translate("Window", "0"))
