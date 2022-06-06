#!/usr/bin/python

import sys
from PyQt5 import QtWidgets,QtGui

def Pencere(baslik,metin):
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle(baslik)
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText(metin)
    etiket1.move(200,30)
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    
    sys.exit(app.exec_())

Pencere("bbbbbbb","112233333")
