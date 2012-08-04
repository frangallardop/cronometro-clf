# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cronometro.ui'
#
# Created: Sat Aug 04 00:09:08 2012
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
        watch.resize(400, 227)
        self.horizontalLayoutWidget = QtGui.QWidget(watch)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 371, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_start = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.horizontalLayout.addWidget(self.btn_start)
        self.btn_stop = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_stop.setObjectName(_fromUtf8("btn_stop"))
        self.horizontalLayout.addWidget(self.btn_stop)
        self.btn_reset = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_reset.setObjectName(_fromUtf8("btn_reset"))
        self.horizontalLayout.addWidget(self.btn_reset)
        self.btn_exit = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.horizontalLayout.addWidget(self.btn_exit)
        self.lb_watch = QtGui.QLabel(watch)
        self.lb_watch.setGeometry(QtCore.QRect(30, 80, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lb_watch.setFont(font)
        self.lb_watch.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_watch.setObjectName(_fromUtf8("lb_watch"))
        self.labelEstado = QtGui.QLabel(watch)
        self.labelEstado.setGeometry(QtCore.QRect(90, 175, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelEstado.setFont(font)
        self.labelEstado.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEstado.setObjectName(_fromUtf8("labelEstado"))

        self.retranslateUi(watch)
        QtCore.QObject.connect(self.btn_exit, QtCore.SIGNAL(_fromUtf8("clicked()")), watch.close)
        QtCore.QMetaObject.connectSlotsByName(watch)

    def retranslateUi(self, watch):
        watch.setWindowTitle(QtGui.QApplication.translate("watch", "Clock Watch", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_start.setText(QtGui.QApplication.translate("watch", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_stop.setText(QtGui.QApplication.translate("watch", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_reset.setText(QtGui.QApplication.translate("watch", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_exit.setText(QtGui.QApplication.translate("watch", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_watch.setText(QtGui.QApplication.translate("watch", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelEstado.setText(QtGui.QApplication.translate("watch", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

