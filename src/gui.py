# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_new.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QDialog, QDesktopWidget
from mathematica import Math

values = ["0"]
number = []
overwrite_flag = 0
log_flag = 0
root_flag = 0
pi = "3.14159265"

class Ui_Basic(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 652)
        MainWindow.setMinimumSize(QtCore.QSize(412, 652))
        MainWindow.setMaximumSize(QtCore.QSize(412, 652))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(38)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_07 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_07.setGeometry(QtCore.QRect(10, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_07.setFont(font)
        self.pushButton_07.setObjectName("pushButton_07")
        self.pushButton_08 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_08.setGeometry(QtCore.QRect(110, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_08.setFont(font)
        self.pushButton_08.setObjectName("pushButton_08")
        self.pushButton_09 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_09.setGeometry(QtCore.QRect(210, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_09.setFont(font)
        self.pushButton_09.setObjectName("pushButton_09")
        self.pushButton_06 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_06.setGeometry(QtCore.QRect(210, 330, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_06.setFont(font)
        self.pushButton_06.setObjectName("pushButton_06")
        self.pushButton_05 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_05.setGeometry(QtCore.QRect(110, 330, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_05.setFont(font)
        self.pushButton_05.setObjectName("pushButton_05")
        self.pushButton_04 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_04.setGeometry(QtCore.QRect(10, 330, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_04.setFont(font)
        self.pushButton_04.setObjectName("pushButton_04")
        self.pushButton_01 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_01.setGeometry(QtCore.QRect(10, 430, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_01.setFont(font)
        self.pushButton_01.setObjectName("pushButton_01")
        self.pushButton_02 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_02.setGeometry(QtCore.QRect(110, 430, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_02.setFont(font)
        self.pushButton_02.setObjectName("pushButton_02")
        self.pushButton_03 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_03.setGeometry(QtCore.QRect(210, 430, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_03.setFont(font)
        self.pushButton_03.setObjectName("pushButton_03")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 530, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(310, 430, 91, 191))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(210, 530, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(310, 330, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(310, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(310, 130, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(210, 130, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 130, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 391, 111))
        self.lineEdit.setMinimumSize(QtCore.QSize(391, 111))
        self.lineEdit.setMaximumSize(QtCore.QSize(391, 111))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(110, 130, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setObjectName("pushButton_28")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 412, 21))
        self.menubar.setObjectName("menubar")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.menuMode.setFont(font)
        self.menuMode.setObjectName("menuMode")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionBasic = QtWidgets.QAction(MainWindow)
        self.actionBasic.setObjectName("actionBasic")
        self.actionBasic.setCheckable(True)
        self.actionBasic.setChecked(True)
        self.actionUser_Manual = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.actionUser_Manual.setFont(font)
        self.actionUser_Manual.setObjectName("actionUser_Manual")
        self.actionAdvanced = QtWidgets.QAction(MainWindow)
        self.actionAdvanced.setObjectName("actionAdvanced")
        self.menuMode.addAction(self.actionBasic)
        self.menuMode.addAction(self.actionAdvanced)
        self.menuHelp.addAction(self.actionUser_Manual)
        self.menubar.addAction(self.menuMode.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_01, self.pushButton_02)
        MainWindow.setTabOrder(self.pushButton_02, self.pushButton_03)
        MainWindow.setTabOrder(self.pushButton_03, self.pushButton_04)
        MainWindow.setTabOrder(self.pushButton_04, self.pushButton_05)
        MainWindow.setTabOrder(self.pushButton_05, self.pushButton_06)
        MainWindow.setTabOrder(self.pushButton_06, self.pushButton_07)
        MainWindow.setTabOrder(self.pushButton_07, self.pushButton_08)
        MainWindow.setTabOrder(self.pushButton_08, self.pushButton_09)
        MainWindow.setTabOrder(self.pushButton_09, self.pushButton_10)
        MainWindow.setTabOrder(self.pushButton_10, self.pushButton_11)
        MainWindow.setTabOrder(self.pushButton_11, self.pushButton_12)
        MainWindow.setTabOrder(self.pushButton_12, self.pushButton_13)
        MainWindow.setTabOrder(self.pushButton_13, self.pushButton_14)
        MainWindow.setTabOrder(self.pushButton_14, self.pushButton_15)
        MainWindow.setTabOrder(self.pushButton_15, self.pushButton_16)
        MainWindow.setTabOrder(self.pushButton_16, self.pushButton_17)
        MainWindow.setTabOrder(self.pushButton_17, self.lineEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KalC00Lačka"))
        self.pushButton_07.setText(_translate("MainWindow", "7"))
        self.pushButton_08.setText(_translate("MainWindow", "8"))
        self.pushButton_09.setText(_translate("MainWindow", "9"))
        self.pushButton_06.setText(_translate("MainWindow", "6"))
        self.pushButton_05.setText(_translate("MainWindow", "5"))
        self.pushButton_04.setText(_translate("MainWindow", "4"))
        self.pushButton_01.setText(_translate("MainWindow", "1"))
        self.pushButton_02.setText(_translate("MainWindow", "2"))
        self.pushButton_03.setText(_translate("MainWindow", "3"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_12.setText(_translate("MainWindow", "="))
        self.pushButton_11.setText(_translate("MainWindow", "."))
        self.pushButton_13.setText(_translate("MainWindow", "+"))
        self.pushButton_14.setText(_translate("MainWindow", "-"))
        self.pushButton_15.setText(_translate("MainWindow", "×"))
        self.pushButton_16.setText(_translate("MainWindow", "÷"))
        self.pushButton_17.setText(_translate("MainWindow", "C"))
        self.pushButton_28.setText(_translate("MainWindow", "←"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionBasic.setText(_translate("MainWindow", "Basic"))
        self.actionUser_Manual.setText(_translate("MainWindow", "User Manual"))
        self.actionAdvanced.setText(_translate("MainWindow", "Advanced"))

        #################################################################################

        self.pushButton_01.clicked.connect(lambda: self.numbers("1"))
        self.pushButton_02.clicked.connect(lambda: self.numbers("2"))
        self.pushButton_03.clicked.connect(lambda: self.numbers("3"))
        self.pushButton_04.clicked.connect(lambda: self.numbers("4"))
        self.pushButton_05.clicked.connect(lambda: self.numbers("5"))
        self.pushButton_06.clicked.connect(lambda: self.numbers("6"))
        self.pushButton_07.clicked.connect(lambda: self.numbers("7"))
        self.pushButton_08.clicked.connect(lambda: self.numbers("8"))
        self.pushButton_09.clicked.connect(lambda: self.numbers("9"))
        self.pushButton_10.clicked.connect(lambda: self.numbers("0"))
        self.pushButton_11.clicked.connect(lambda: self.numbers("."))

        self.pushButton_13.clicked.connect(lambda: self.operand("+"))
        self.pushButton_14.clicked.connect(lambda: self.operand("-"))
        self.pushButton_15.clicked.connect(lambda: self.operand("*"))
        self.pushButton_16.clicked.connect(lambda: self.operand("/"))

        self.pushButton_12.clicked.connect(self.evaluate)
        self.pushButton_17.clicked.connect(self.clear)
        self.pushButton_28.clicked.connect(self.back)

        self.actionAdvanced.triggered.connect(self.change_ui)

        self.init()

#################################################################################

    def init(self):
        global overwrite_flag

        self.lineEdit.setText(''.join(values+number))
        overwrite_flag = 1

        self.fit()

    def back(self):
        global values, number

        try:
            if number:
                number.pop()
                self.lineEdit.setText(''.join(values+number))
            else:
                values.pop()
                self.lineEdit.setText(''.join(values+number))
        except:
            values = ["0"]
            self.lineEdit.setText(''.join(values+number))

        self.fit()

    def numbers(self, x):
        global values, number, overwrite_flag, log_flag, root_flag
        
        if overwrite_flag is 1:
            values = []
            overwrite_flag = 0
        
        if log_flag is 1 or root_flag is 1:
            if log_flag is 1:
                number.append(x)
                num = ''.join(number)
                self.lineEdit.setText("log("+str(num)+", "+str(values)+")")

            if root_flag is 1:
                number.append(x)
                num = ''.join(number)
                self.lineEdit.setText(str(num)+"√"+str(values))
            
        else: # len 1 bodka
            if x == "." and "." in number:
                pass
            elif x == "." and not number:
                number.append("0"+x)
            else:
                number.append(x)

            try:
                if number[0] == "0" and number[1] != ".":
                    number.pop(0)
            except:
                pass

            num = ''.join(number)
            
            if len(num) > 40: 
                number.pop()
                num = ''.join(number)

            self.lineEdit.setText(''.join(values)+num)

        self.fit()
    
    def operand(self, x):
        global values, number, overwrite_flag, log_flag, root_flag

        overwrite_flag = 0

        if log_flag == 1 or root_flag == 1:
            number.append(x)
            if log_flag == 1:
                self.lineEdit.setText("log("+str(''.join(number))+", "+str(values)+")")
            else:
                self.lineEdit.setText(''.join(number)+self.lineEdit.text())

        else:
            if number:
                values.append(''.join(number))
                number = []

            if not values:
                values.append("0")

            if x == "^" or x == "^2":
                values.insert(0,"(")
                values.append(")")

            if values[-1] == "*" or values[-1] == "/":
                values.pop()
            
            values.append(x)

            self.lineEdit.setText(''.join(values))

        self.fit()

    def evaluate(self):
        global values, number, overwrite_flag, log_flag, root_flag
        
        if log_flag == 1:
            try:
                result = Math(int(values)).log(int(''.join(number)))
                self.lineEdit.setText(str(result))
                values = [str(result)]
            except:
                self.lineEdit.setText("Syntax Error")
            
            number = []
            log_flag = 0
            overwrite_flag = 1

        elif root_flag == 1:
            try:
                result = Math(int(values)).root(int(''.join(number)))
                self.lineEdit.setText(str(result))
                values = [str(result)]
            except:
                self.lineEdit.setText("Syntax Error")
            
            number = []
            root_flag = 0
            overwrite_flag = 1

        else:
            print(values, number)
            expr = self.lineEdit.text()
            print(expr)
            result = Math(expr)
            self.lineEdit.setText(str(result))
            print(result)

            overwrite_flag = 1
            values = [str(result)]
            number = []

        self.fit()

    def clear(self):
        global values, number, overwrite_flag, log_flag, root_flag
        
        values = ["0"]
        number = []
        self.lineEdit.setText(values[0])

        log_flag = 0
        root_flag = 0
        overwrite_flag = 1

        self.fit()

    def fit(self):

        self.lineEdit.setCursorPosition(0)

        size = 38
        font = QtGui.QFont()
        font.setPointSize(size)

        if len(self.lineEdit.text()) > 13:
            i = len(self.lineEdit.text()) - 13
            j = 27

            while i > 0 :
                
                if i > 6:
                    
                    if size < 28:                        
                        
                        if j % 4 == 0 :
                            size += -1
                        j += -1
                    
                    else:
                        size += -1
                        
                else:
                    size += -2

                i += -1

        font.setPointSize(size)
        self.lineEdit.setFont(font)
        self.lineEdit.show()

class Ui_Advanced(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 652)
        MainWindow.setMinimumSize(QtCore.QSize(612, 652))
        MainWindow.setMaximumSize(QtCore.QSize(612, 652))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(38)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_07 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_07.setGeometry(QtCore.QRect(210, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_07.setFont(font)
        self.pushButton_07.setObjectName("pushButton_07")
        self.pushButton_08 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_08.setGeometry(QtCore.QRect(310, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_08.setFont(font)
        self.pushButton_08.setObjectName("pushButton_08")
        self.pushButton_09 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_09.setGeometry(QtCore.QRect(410, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_09.setFont(font)
        self.pushButton_09.setObjectName("pushButton_09")
        self.pushButton_06 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_06.setGeometry(QtCore.QRect(410, 330, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_06.setFont(font)
        self.pushButton_06.setObjectName("pushButton_06")
        self.pushButton_05 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_05.setGeometry(QtCore.QRect(310, 330, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_05.setFont(font)
        self.pushButton_05.setObjectName("pushButton_05")
        self.pushButton_04 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_04.setGeometry(QtCore.QRect(210, 330, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_04.setFont(font)
        self.pushButton_04.setObjectName("pushButton_04")
        self.pushButton_01 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_01.setGeometry(QtCore.QRect(210, 430, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_01.setFont(font)
        self.pushButton_01.setObjectName("pushButton_01")
        self.pushButton_02 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_02.setGeometry(QtCore.QRect(310, 430, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_02.setFont(font)
        self.pushButton_02.setObjectName("pushButton_02")
        self.pushButton_03 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_03.setGeometry(QtCore.QRect(410, 430, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_03.setFont(font)
        self.pushButton_03.setObjectName("pushButton_03")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 530, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(510, 430, 91, 191))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(410, 530, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(510, 330, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(510, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(510, 130, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(410, 130, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(210, 130, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 591, 111))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(50)###19) ###
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(10, 430, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(10, 530, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(10, 330, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(110, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(10, 130, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(110, 130, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(110, 330, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(110, 430, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(110, 530, 91, 91))
        self.pushButton_27.setSizeIncrement(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(38)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_27.setMouseTracking(False)
        self.pushButton_27.setToolTip("")
        self.pushButton_27.setStatusTip("")
        self.pushButton_27.setWhatsThis("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(310, 130, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setObjectName("pushButton_28")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menubar.setObjectName("menubar")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.menuMode.setFont(font)
        self.menuMode.setObjectName("menuMode")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionBasic = QtWidgets.QAction(MainWindow)
        self.actionBasic.setObjectName("actionBasic")
        self.actionUser_Manual = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.actionUser_Manual.setFont(font)
        self.actionUser_Manual.setObjectName("actionUser_Manual")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAdvanced = QtWidgets.QAction(MainWindow)
        self.actionAdvanced.setObjectName("actionAdvanced")
        self.actionAdvanced.setCheckable(True)
        self.actionAdvanced.setChecked(True)
        self.menuMode.addAction(self.actionBasic)
        self.menuMode.addAction(self.actionAdvanced)
        self.menuHelp.addAction(self.actionUser_Manual)
        self.menubar.addAction(self.menuMode.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_01, self.pushButton_02)
        MainWindow.setTabOrder(self.pushButton_02, self.pushButton_03)
        MainWindow.setTabOrder(self.pushButton_03, self.pushButton_04)
        MainWindow.setTabOrder(self.pushButton_04, self.pushButton_05)
        MainWindow.setTabOrder(self.pushButton_05, self.pushButton_06)
        MainWindow.setTabOrder(self.pushButton_06, self.pushButton_07)
        MainWindow.setTabOrder(self.pushButton_07, self.pushButton_08)
        MainWindow.setTabOrder(self.pushButton_08, self.pushButton_09)
        MainWindow.setTabOrder(self.pushButton_09, self.pushButton_10)
        MainWindow.setTabOrder(self.pushButton_10, self.pushButton_11)
        MainWindow.setTabOrder(self.pushButton_11, self.pushButton_12)
        MainWindow.setTabOrder(self.pushButton_12, self.pushButton_13)
        MainWindow.setTabOrder(self.pushButton_13, self.pushButton_14)
        MainWindow.setTabOrder(self.pushButton_14, self.pushButton_15)
        MainWindow.setTabOrder(self.pushButton_15, self.pushButton_16)
        MainWindow.setTabOrder(self.pushButton_16, self.pushButton_17)
        MainWindow.setTabOrder(self.pushButton_17, self.pushButton_18)
        MainWindow.setTabOrder(self.pushButton_18, self.pushButton_19)
        MainWindow.setTabOrder(self.pushButton_19, self.pushButton_20)
        MainWindow.setTabOrder(self.pushButton_20, self.pushButton_21)
        MainWindow.setTabOrder(self.pushButton_21, self.pushButton_22)
        MainWindow.setTabOrder(self.pushButton_22, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.pushButton_25)
        MainWindow.setTabOrder(self.pushButton_25, self.pushButton_26)
        MainWindow.setTabOrder(self.pushButton_26, self.pushButton_27)
        MainWindow.setTabOrder(self.pushButton_27, self.pushButton_23)
        MainWindow.setTabOrder(self.pushButton_23, self.pushButton_24)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KalC00Lačka"))
        self.pushButton_07.setText(_translate("MainWindow", "7"))
        self.pushButton_08.setText(_translate("MainWindow", "8"))
        self.pushButton_09.setText(_translate("MainWindow", "9"))
        self.pushButton_06.setText(_translate("MainWindow", "6"))
        self.pushButton_05.setText(_translate("MainWindow", "5"))
        self.pushButton_04.setText(_translate("MainWindow", "4"))
        self.pushButton_01.setText(_translate("MainWindow", "1"))
        self.pushButton_02.setText(_translate("MainWindow", "2"))
        self.pushButton_03.setText(_translate("MainWindow", "3"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_12.setText(_translate("MainWindow", "="))
        self.pushButton_11.setText(_translate("MainWindow", "."))
        self.pushButton_13.setText(_translate("MainWindow", "+"))
        self.pushButton_14.setText(_translate("MainWindow", "-"))
        self.pushButton_15.setText(_translate("MainWindow", "×"))
        self.pushButton_16.setText(_translate("MainWindow", "÷"))
        self.pushButton_17.setText(_translate("MainWindow", "C"))
        self.pushButton_21.setText(_translate("MainWindow", "x²"))
        self.pushButton_22.setText(_translate("MainWindow", "x!"))
        self.pushButton_20.setText(_translate("MainWindow", "xⁿ"))
        self.pushButton_18.setText(_translate("MainWindow", "ln(x)"))
        self.pushButton_19.setText(_translate("MainWindow", "logₙ(x)"))
        self.pushButton_23.setText(_translate("MainWindow", "("))
        self.pushButton_24.setText(_translate("MainWindow", ")"))
        self.pushButton_25.setText(_translate("MainWindow", "ⁿ√x"))
        self.pushButton_26.setText(_translate("MainWindow", "²√x"))
        self.pushButton_27.setText(_translate("MainWindow", "π"))
        self.pushButton_28.setText(_translate("MainWindow", "←"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionBasic.setText(_translate("MainWindow", "Basic"))
        self.actionUser_Manual.setText(_translate("MainWindow", "User Manual"))
        self.actionAdvanced.setText(_translate("MainWindow", "Advanced"))

#################################################################################

        self.pushButton_01.clicked.connect(lambda: self.numbers("1"))
        self.pushButton_02.clicked.connect(lambda: self.numbers("2"))
        self.pushButton_03.clicked.connect(lambda: self.numbers("3"))
        self.pushButton_04.clicked.connect(lambda: self.numbers("4"))
        self.pushButton_05.clicked.connect(lambda: self.numbers("5"))
        self.pushButton_06.clicked.connect(lambda: self.numbers("6"))
        self.pushButton_07.clicked.connect(lambda: self.numbers("7"))
        self.pushButton_08.clicked.connect(lambda: self.numbers("8"))
        self.pushButton_09.clicked.connect(lambda: self.numbers("9"))
        self.pushButton_10.clicked.connect(lambda: self.numbers("0"))
        self.pushButton_11.clicked.connect(lambda: self.numbers("."))
        self.pushButton_23.clicked.connect(lambda: self.numbers("("))
        self.pushButton_24.clicked.connect(lambda: self.numbers(")"))
        self.pushButton_27.clicked.connect(lambda: self.numbers(pi))

        self.pushButton_13.clicked.connect(lambda: self.operand("+"))
        self.pushButton_14.clicked.connect(lambda: self.operand("-"))
        self.pushButton_15.clicked.connect(lambda: self.operand("*"))
        self.pushButton_16.clicked.connect(lambda: self.operand("/"))
        self.pushButton_20.clicked.connect(lambda: self.operand("^"))
        self.pushButton_21.clicked.connect(lambda: self.operand("^2"))

        self.pushButton_22.clicked.connect(self.factorial)
        self.pushButton_18.clicked.connect(self.ln)
        self.pushButton_19.clicked.connect(self.log)
        self.pushButton_25.clicked.connect(self.root)
        self.pushButton_26.clicked.connect(self.sqroot)

        self.pushButton_12.clicked.connect(self.evaluate)
        self.pushButton_17.clicked.connect(self.clear)
        self.pushButton_28.clicked.connect(self.back)

        self.actionBasic.triggered.connect(self.change_ui)

        self.init()

#################################################################################

    def init(self):
        global overwrite_flag

        self.lineEdit.setText(''.join(values+number))
        overwrite_flag = 1

        self.fit()

    def back(self):
        global values, number

        try:
            if number:
                number.pop()
                self.lineEdit.setText(''.join(values+number))
            else:
                values.pop()
                self.lineEdit.setText(''.join(values+number))
        except:
            values = ["0"]
            self.lineEdit.setText(''.join(values+number))

        self.fit()


    def sqroot(self):
        global values, number, overwrite_flag
        
        result = Math(self.lineEdit.text()).root()
        self.lineEdit.setText(str(result))
        number = []
        values = [str(result)]
        overwrite_flag = 1

        self.fit()

    def root(self):
        global values, number, overwrite_flag, root_flag

        overwrite_flag = 0
        root_flag = 1
        values = self.lineEdit.text()
        self.lineEdit.setText("√"+str(values))
        number = []

        self.fit()

    def ln(self):
        global values, number, overwrite_flag

        result = Math(self.lineEdit.text()).ln()
        self.lineEdit.setText(str(result))
        number = []
        values = [str(result)]
        overwrite_flag = 1

        self.fit()

    def log(self):
        global values, number, overwrite_flag, log_flag

        overwrite_flag = 0
        log_flag = 1
        values = self.lineEdit.text()
        self.lineEdit.setText("log(x, "+str(values)+")")
        number = []

        self.fit()

    def factorial(self):
        global values, number, overwrite_flag
        
        result = Math(self.lineEdit.text()).factorial()
        self.lineEdit.setText(str(result))
        number = []
        values = [str(result)]
        overwrite_flag = 1

        self.fit()

    def numbers(self, x):
        global values, number, overwrite_flag, log_flag, root_flag
        
        if overwrite_flag is 1:
            values = []
            overwrite_flag = 0
        
        if log_flag == 1 or root_flag == 1:

            if x != "(" and x != ")":

                if log_flag is 1:
                    number.append(x)
                    num = ''.join(number)
                    self.lineEdit.setText("log("+str(num)+", "+str(values)+")")

                if root_flag is 1:
                    number.append(x)
                    num = ''.join(number)
                    self.lineEdit.setText(str(num)+"√"+str(values))
            
        else: # len 1 bodka
            if x == "." and "." in number:
                pass
            elif x == "." and not number:
                number.append("0"+x)
            else:
                number.append(x)

            try:
                if number[0] == "0" and number[1] != ".":
                    number.pop(0)
            except:
                pass

            num = ''.join(number)
            
            if len(num) > 40: 
                number.pop()
                num = ''.join(number)

            self.lineEdit.setText(''.join(values)+num)

        self.fit()
    
    def operand(self, x):
        global values, number, overwrite_flag, log_flag, root_flag

        overwrite_flag = 0

        if log_flag == 1 or root_flag == 1:
            if x == "-":
                number.append(x)
                if log_flag == 1:
                    self.lineEdit.setText("log("+str(''.join(number))+", "+str(values)+")")
                else:
                    self.lineEdit.setText(''.join(number)+self.lineEdit.text())

        else:
            if number:
                values.append(''.join(number))
                number = []

            if not values:
                values.append("0")

            if x == "^" or x == "^2":
                values.insert(0,"(")
                values.append(")")

            if values[-1] == "*" or values[-1] == "/":
                values.pop()
            
            values.append(x)

            self.lineEdit.setText(''.join(values))
        
        self.fit()

    def evaluate(self):
        global values, number, overwrite_flag, log_flag, root_flag
        
        if log_flag == 1:
            try:
                result = Math(int(values)).log(int(''.join(number)))
                self.lineEdit.setText(str(result))
                values = [str(result)]
            except:
                self.lineEdit.setText("Syntax Error")
            
            number = []
            log_flag = 0
            overwrite_flag = 1

        elif root_flag == 1:
            try:
                result = Math(int(values)).root(int(''.join(number)))
                self.lineEdit.setText(str(result))
                values = [str(result)]
            except:
                self.lineEdit.setText("Syntax Error")
            
            number = []
            root_flag = 0
            overwrite_flag = 1

        else:
            print(values, number)

            expr = ''.join(values+number)
            print(expr)

            result = Math(expr)
            self.lineEdit.setText(str(result))
            print(result)

            overwrite_flag = 1
            values = [str(result)]
            number = []

        self.fit()


    def clear(self):
        global values, number, overwrite_flag, log_flag, root_flag
        
        values = ["0"]
        number = []
        self.lineEdit.setText(values[0])

        log_flag = 0
        root_flag = 0
        overwrite_flag = 1

        self.fit()

    def fit(self):

        self.lineEdit.setCursorPosition(0)

        size = 38
        font = QtGui.QFont()
        font.setPointSize(size)

        if len(self.lineEdit.text()) > 20:
            i = len(self.lineEdit.text()) - 20
            j = 22

            while i > 0 :
                
                if i > 2:
                    
                    if size < 23:                        
                        
                        if j % 4 == 0 :
                            size += -1
                        j += -1
                    
                    else:
                        size += -1
                        
                else:
                    size += -2

                i += -1

            font.setPointSize(size)

        self.lineEdit.setFont(font)
        self.lineEdit.show()

######################################################################

class MainWindowBasic(QMainWindow, Ui_Basic):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def keyPressEvent(self, e):

        if   e.key() == Qt.Key_0:
            self.numbers("0")
        elif e.key() == Qt.Key_1:
            self.numbers("1")
        elif e.key() == Qt.Key_2:
            self.numbers("2")
        elif e.key() == Qt.Key_3:
            self.numbers("3")
        elif e.key() == Qt.Key_4:
            self.numbers("4")
        elif e.key() == Qt.Key_5:
            self.numbers("5")
        elif e.key() == Qt.Key_6:
            self.numbers("6")
        elif e.key() == Qt.Key_7:
            self.numbers("7")
        elif e.key() == Qt.Key_8:
            self.numbers("8")
        elif e.key() == Qt.Key_9:
            self.numbers("9")
        elif e.key() == Qt.Key_Period:
            self.numbers(".")

        elif e.key() == Qt.Key_Plus:
            self.operand("+")
        elif e.key() == Qt.Key_Minus:
            self.operand("-")
        elif e.key() == Qt.Key_Asterisk:
            self.operand("*")
        elif e.key() == Qt.Key_Slash:
            self.operand("/")

        elif e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return:
            self.evaluate()
        elif e.key() == Qt.Key_Delete:
            self.clear()
        elif e.key() == Qt.Key_Backspace:
            self.back()

    def change_ui(self):
        w = MainWindowAdvanced()
        w.show()
        self.close()    

class MainWindowAdvanced(QMainWindow, Ui_Advanced):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def keyPressEvent(self, e):

        if (e.modifiers() & Qt.ShiftModifier):
            val = e.key()

            if QtGui.QKeySequence(val).toString() == "(":
                self.numbers("(")

            if QtGui.QKeySequence(val).toString() == ")":
                self.numbers(")")
            
            if QtGui.QKeySequence(val).toString() == "!":
                self.factorial()

        if   e.key() == Qt.Key_0:
            self.numbers("0")
        elif e.key() == Qt.Key_1:
            self.numbers("1")
        elif e.key() == Qt.Key_2:
            self.numbers("2")
        elif e.key() == Qt.Key_3:
            self.numbers("3")
        elif e.key() == Qt.Key_4:
            self.numbers("4")
        elif e.key() == Qt.Key_5:
            self.numbers("5")
        elif e.key() == Qt.Key_6:
            self.numbers("6")
        elif e.key() == Qt.Key_7:
            self.numbers("7")
        elif e.key() == Qt.Key_8:
            self.numbers("8")
        elif e.key() == Qt.Key_9:
            self.numbers("9")
        elif e.key() == Qt.Key_Period:
            self.numbers(".")

        elif e.key() == Qt.Key_Plus:
            self.operand("+")
        elif e.key() == Qt.Key_Minus:
            self.operand("-")
        elif e.key() == Qt.Key_Asterisk:
            self.operand("*")
        elif e.key() == Qt.Key_Slash:
            self.operand("/")

        elif e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return:
            self.evaluate()
        elif e.key() == Qt.Key_Delete:
            self.clear()
        elif e.key() == Qt.Key_Backspace:
            self.back()

    def change_ui(self):
        w = MainWindowBasic()
        w.show()
        self.close()

