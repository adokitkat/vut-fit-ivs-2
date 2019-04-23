#!/usr/bin/env python3
import sys
from mathematica import Math
import gui as gui

def init():
    app = gui.QtWidgets.QApplication(sys.argv)
    w = gui.MainWindowBasic()
    w.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    init()