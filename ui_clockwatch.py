# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cronometro.ui'
#
# Created: Sat Oct 06 13:15:38 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_watch(object):
    def setupUi(self, watch):
        watch.setObjectName(_fromUtf8("watch"))
        watch.setEnabled(True)
        watch.resize(1218, 592)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(watch.sizePolicy().hasHeightForWidth())
        watch.setSizePolicy(sizePolicy)
        watch.setMinimumSize(QtCore.QSize(700, 500))
        watch.setWhatsThis(_fromUtf8(""))
        watch.setStyleSheet(_fromUtf8("/*background-color: rgb(0,0,0);*/\n"
"/*background-color: rgb(0, 0, 50);*/\n"
"background-color: rgb(0, 40, 30);"))
        self.gridLayout = QtGui.QGridLayout(watch)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lb_watch = QtGui.QLabel(watch)
        self.lb_watch.setMinimumSize(QtCore.QSize(0, 250))
        font = QtGui.QFont()
        font.setPointSize(150)
        self.lb_watch.setFont(font)
        self.lb_watch.setStyleSheet(_fromUtf8("color: rgb(255, 255, 0);"))
        self.lb_watch.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_watch.setObjectName(_fromUtf8("lb_watch"))
        self.gridLayout.addWidget(self.lb_watch, 4, 1, 1, 1)
        self.labelEstado = QtGui.QLabel(watch)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.labelEstado.setFont(font)
        self.labelEstado.setStyleSheet(_fromUtf8("color: rgb(255,255,255);"))
        self.labelEstado.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEstado.setObjectName(_fromUtf8("labelEstado"))
        self.gridLayout.addWidget(self.labelEstado, 5, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)

        self.retranslateUi(watch)
        QtCore.QMetaObject.connectSlotsByName(watch)

    def retranslateUi(self, watch):
        watch.setWindowTitle(QtGui.QApplication.translate("watch", "Temporizador Categoria FULL (Version de prueba)", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_watch.setText(QtGui.QApplication.translate("watch", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelEstado.setText(QtGui.QApplication.translate("watch", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

