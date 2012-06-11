#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
from ui_clockwatch import Ui_watch
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import (QMessageBox, QMainWindow, QWidget, QApplication)
from PyQt4.QtCore import (Qt, SIGNAL, pyqtSignature, QBasicTimer)

class VentanaTimer(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
	self.ui = Ui_watch()
	self.ui.setupUi(self)
        
        #Inicializo variables
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self._setTime(self._elapsedtime)
        
        #Creo mi Timer
        self.timer = QtCore.QBasicTimer()
               
    
    @pyqtSignature("")
    def on_btn_start_clicked(self):
        try:
            """ Iniciar cronometro, ignorar si se está ejecutando. """
            if not self._running:            
                self._start = time.time() - self._elapsedtime
                self._running = 1
                self.timer.start(100, self)
                self.ui.btn_start.setText("Detener")
            else:
                self.timer.stop()
                self._elapsedtime = time.time() - self._start    
                self._setTime(self._elapsedtime)
                self.ui.btn_start.setText("Continuar")
                self._running = 0
                
        except:
            QMessageBox.warning(self, "Mensaje",
                            unicode("Error: Controlar el botón de inicio"))
    @pyqtSignature("")
    def on_btn_reset_clicked(self):                                   
        """ Reinicio mi cronometro. """
        self._start = time.time()         
        self._elapsedtime = 0.0    
        self._setTime(self._elapsedtime)
        
    def timerEvent(self, event):
        try:
            """ Actualizo la etiqueta con tiempo remanente. """
            elap = time.time() - self._start
            """ Configuro el string con Minutos, segundo y centesimas de seg. """
            minutes = int(elap/60)
            seconds = int(elap - minutes*60.0)
            hseconds = int((elap - minutes*60.0 - seconds)*100)                
            self.ui.lb_watch.setText('%02d:%02d:%02d' % (minutes, seconds, hseconds))
            
            # Paro mi reloj en 5 segundos
            if seconds==5:
              self.timer.stop()
              # Corrijo los milisegundos
              hseconds=00
              self.ui.lb_watch.setText('%02d:%02d:%02d' % (minutes, seconds, hseconds))

        except:
            QMessageBox.warning(self, "Mensaje",
                            unicode("Error: Controlar timer"))
        
    
    def _setTime(self, elap):
        """ Configuro el string con Minutos, segundo y centesimas de seg. """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.ui.lb_watch.setText('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = VentanaTimer()
    myapp.show()
    sys.exit(app.exec_())
