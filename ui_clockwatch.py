# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cronometro.ui'
#
# Created: Sat Aug 04 02:19:15 2012
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
        watch.resize(730, 494)
        watch.setMinimumSize(QtCore.QSize(730, 494))
        watch.setWhatsThis(_fromUtf8(""))
        watch.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.gridLayout = QtGui.QGridLayout(watch)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(80, -1, 80, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btn_start = QtGui.QPushButton(watch)
        self.btn_start.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet(_fromUtf8("border-color: rgb(149, 149, 149);"))
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.horizontalLayout_4.addWidget(self.btn_start)
        self.btn_stop = QtGui.QPushButton(watch)
        self.btn_stop.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_stop.setFont(font)
        self.btn_stop.setObjectName(_fromUtf8("btn_stop"))
        self.horizontalLayout_4.addWidget(self.btn_stop)
        self.btn_reset = QtGui.QPushButton(watch)
        self.btn_reset.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_reset.setFont(font)
        self.btn_reset.setObjectName(_fromUtf8("btn_reset"))
        self.horizontalLayout_4.addWidget(self.btn_reset)
        self.btn_exit = QtGui.QPushButton(watch)
        self.btn_exit.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet(_fromUtf8("border-color: rgb(149, 149, 149);"))
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.horizontalLayout_4.addWidget(self.btn_exit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.lb_watch = QtGui.QLabel(watch)
        self.lb_watch.setMinimumSize(QtCore.QSize(0, 250))
        font = QtGui.QFont()
        font.setPointSize(120)
        self.lb_watch.setFont(font)
        self.lb_watch.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_watch.setObjectName(_fromUtf8("lb_watch"))
        self.gridLayout.addWidget(self.lb_watch, 2, 1, 1, 1)
        self.labelEstado = QtGui.QLabel(watch)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.labelEstado.setFont(font)
        self.labelEstado.setStyleSheet(_fromUtf8("color: rgb(103, 103, 103);"))
        self.labelEstado.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEstado.setObjectName(_fromUtf8("labelEstado"))
        self.gridLayout.addWidget(self.labelEstado, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 1)

        self.retranslateUi(watch)
        QtCore.QObject.connect(self.btn_exit, QtCore.SIGNAL(_fromUtf8("clicked()")), watch.close)
        QtCore.QMetaObject.connectSlotsByName(watch)

    def retranslateUi(self, watch):
        watch.setWindowTitle(QtGui.QApplication.translate("watch", "Temporizador", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_start.setText(QtGui.QApplication.translate("watch", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_stop.setText(QtGui.QApplication.translate("watch", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_reset.setText(QtGui.QApplication.translate("watch", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_exit.setText(QtGui.QApplication.translate("watch", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_watch.setText(QtGui.QApplication.translate("watch", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelEstado.setText(QtGui.QApplication.translate("watch", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

