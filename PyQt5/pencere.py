#!/usr/bin/python

import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("Deneme Penceresi")
    pencere.show()
    
    sys.exit(app.exec_())

Pencere()
