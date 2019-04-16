#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mathematica import Math

values = []
number = []

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 653)
        MainWindow.setMinimumSize(QtCore.QSize(512, 652))
        MainWindow.setMaximumSize(QtCore.QSize(512, 653))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(38)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_07 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_07.setGeometry(QtCore.QRect(110, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_07.setFont(font)
        self.pushButton_07.setObjectName("pushButton_07")
        self.pushButton_08 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_08.setGeometry(QtCore.QRect(210, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_08.setFont(font)
        self.pushButton_08.setObjectName("pushButton_08")
        self.pushButton_09 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_09.setGeometry(QtCore.QRect(310, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_09.setFont(font)
        self.pushButton_09.setObjectName("pushButton_09")
        self.pushButton_06 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_06.setGeometry(QtCore.QRect(310, 330, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_06.setFont(font)
        self.pushButton_06.setObjectName("pushButton_06")
        self.pushButton_05 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_05.setGeometry(QtCore.QRect(210, 330, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_05.setFont(font)
        self.pushButton_05.setObjectName("pushButton_05")
        self.pushButton_04 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_04.setGeometry(QtCore.QRect(110, 330, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_04.setFont(font)
        self.pushButton_04.setObjectName("pushButton_04")
        self.pushButton_01 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_01.setGeometry(QtCore.QRect(110, 430, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_01.setFont(font)
        self.pushButton_01.setObjectName("pushButton_01")
        self.pushButton_02 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_02.setGeometry(QtCore.QRect(210, 430, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_02.setFont(font)
        self.pushButton_02.setObjectName("pushButton_02")
        self.pushButton_03 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_03.setGeometry(QtCore.QRect(310, 430, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_03.setFont(font)
        self.pushButton_03.setObjectName("pushButton_03")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(110, 530, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(410, 430, 91, 191))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(310, 530, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(410, 230, 91, 191))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(410, 130, 91, 91))
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
        self.pushButton_17.setGeometry(QtCore.QRect(110, 130, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 491, 111))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
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
        self.pushButton_18.setGeometry(QtCore.QRect(10, 130, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(10, 230, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 21))
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
        self.menuMode.addAction(self.actionBasic)
        self.menuHelp.addAction(self.actionUser_Manual)
        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

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
        
        self.pushButton_12.clicked.connect(self.evaluate)
        self.pushButton_17.clicked.connect(self.clear)

        self.pushButton_13.clicked.connect(lambda: self.operand("+"))
        self.pushButton_14.clicked.connect(lambda: self.operand("-"))
        self.pushButton_15.clicked.connect(lambda: self.operand("*"))
        self.pushButton_16.clicked.connect(lambda: self.operand("/"))
        self.pushButton_20.clicked.connect(lambda: self.operand("^"))
        self.pushButton_21.clicked.connect(lambda: self.operand("^2"))

        self.pushButton_18.clicked.connect(self.ln)
#        self.pushButton_19.clicked.connect(lambda: self.log)

    def ln(self):
        global values, number
        result = Math(self.lineEdit.text()).ln()
        self.lineEdit.setText(str(result))
        number = []
        values = [str(result)]

#    def log(self):
#        global values, number
#        #result = Math(self.lineEdit.text()).log(base)
#        
#        #number = []
#        values = [self.lineEdit.text()]


    def numbers(self, x):
        global values, number
        number.append(x)
        
        try:
            if number[0] == "0" and number[1] != ".":
                number.pop(0)
        except:
            pass

        num = ''.join(number)
        self.lineEdit.setText(''.join(values)+num)
    
    def operand(self, x):
        global values, number

        if number:
            values.append(''.join(number))
            number = []
        
        try:
            if values[0] :
                values.append(x)
                self.lineEdit.setText(''.join(values))
        except:
            pass

    def evaluate(self):
        global values, number
        
        print(values, number)
        #expr = ''.join(values) + ''.join(number)
        expr = self.lineEdit.text()
        print(expr)
        result = Math(expr)
        self.lineEdit.setText(str(result))
        print(result)
        values = [str(result)]
        number = []

    def clear(self):
        global values, number
        values = []
        number = []
        self.lineEdit.setText('')


#    def number(self, x):
#        global values
#        values.append(x)
#        num = ''.join(values)
#        self.lineEdit.setText(num)
#        values = [num]
#    
#    def operand(self, opr):
#        global values
#        if values[0]:
#            values.append(opr)
#            num = ''.join(values)
#            self.lineEdit.setText(num)
#            values[0] = '(' + values[0] + ')'
#
#    def evaluate(self):
#        global values
#        result = Math(str(values[0]))
#        self.lineEdit.setText(str(result))
#        print(result)
#        values = []
#

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KalC00Lačka"))
        
        self.pushButton_01.setText(_translate("MainWindow", "1"))
        self.pushButton_02.setText(_translate("MainWindow", "2"))
        self.pushButton_03.setText(_translate("MainWindow", "3"))
        self.pushButton_04.setText(_translate("MainWindow", "4"))
        self.pushButton_05.setText(_translate("MainWindow", "5"))
        self.pushButton_06.setText(_translate("MainWindow", "6"))
        self.pushButton_07.setText(_translate("MainWindow", "7"))
        self.pushButton_08.setText(_translate("MainWindow", "8"))
        self.pushButton_09.setText(_translate("MainWindow", "9"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_11.setText(_translate("MainWindow", "."))
        self.pushButton_12.setText(_translate("MainWindow", "="))
        self.pushButton_13.setText(_translate("MainWindow", "+"))
        self.pushButton_14.setText(_translate("MainWindow", "-"))
        self.pushButton_15.setText(_translate("MainWindow", "*"))
        self.pushButton_16.setText(_translate("MainWindow", "/"))
        self.pushButton_17.setText(_translate("MainWindow", "C"))
        self.pushButton_18.setText(_translate("MainWindow", "ln(x)"))
        self.pushButton_19.setText(_translate("MainWindow", "logₙ(x)"))
        self.pushButton_20.setText(_translate("MainWindow", "xⁿ"))
        self.pushButton_21.setText(_translate("MainWindow", "x²"))
        self.pushButton_22.setText(_translate("MainWindow", "x!"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionBasic.setText(_translate("MainWindow", "Basic"))
        self.actionUser_Manual.setText(_translate("MainWindow", "User Manual"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
