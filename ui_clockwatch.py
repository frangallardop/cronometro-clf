# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clock_watch.ui'
#
# Created: Sat Jan 30 15:05:10 2010
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_watch(object):
    def setupUi(self, watch):
        watch.setObjectName("watch")
        watch.resize(400, 166)
        self.horizontalLayoutWidget = QtGui.QWidget(watch)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 371, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_start = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout.addWidget(self.btn_start)
        self.btn_reset = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout.addWidget(self.btn_reset)
        self.btn_exit = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)
        self.lb_watch = QtGui.QLabel(watch)
        self.lb_watch.setGeometry(QtCore.QRect(30, 80, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lb_watch.setFont(font)
        self.lb_watch.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_watch.setObjectName("lb_watch")

        self.retranslateUi(watch)
        QtCore.QObject.connect(self.btn_exit, QtCore.SIGNAL("clicked()"), watch.close)
        QtCore.QMetaObject.connectSlotsByName(watch)

    def retranslateUi(self, watch):
        watch.setWindowTitle(QtGui.QApplication.translate("watch", "Clock Watch", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_start.setText(QtGui.QApplication.translate("watch", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_reset.setText(QtGui.QApplication.translate("watch", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_exit.setText(QtGui.QApplication.translate("watch", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_watch.setText(QtGui.QApplication.translate("watch", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    watch = QtGui.QWidget()
    ui = Ui_watch()
    ui.setupUi(watch)
    watch.show()
    sys.exit(app.exec_())

