#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
from ui_clockwatch import Ui_watch
from PyQt4 import QtGui
from PyQt4.QtGui import QSound
from PyQt4.QtCore import SIGNAL, pyqtSignature, QBasicTimer, QObject

class EstadoTimer(QObject):
    def __init__(self, minutos=3, segundos=0, label=None, window=None):
        super(EstadoTimer, self).__init__()
        self.segundos = segundos + 60*minutos
        self.segundos_iniciales = self.segundos
        self.label = label
        self.timer = QBasicTimer()
        self.window = window
        QObject.connect(self, SIGNAL("ESTADO_TIMER_FINALIZADO"), self.window.estado_timer_finalizado)
        self.set_text(self.segundos/60, self.segundos%60, (self.segundos%1)*100)
        
    
    def start(self):
        self.start_time = time.time()
        return self.timer.start(10, self)
    
    def pause(self):
        elapsed_time = time.time() - self.start_time
        self.segundos -= elapsed_time
        return self.timer.stop()
    
    def reset(self):
        if self.timer.isActive():
            self.timer.stop()
        self.segundos = self.segundos_iniciales
        self.set_text(self.segundos/60, self.segundos%60, (self.segundos%1)*100)
    
    def is_active(self):
        return self.timer.isActive()
    
    def timerEvent(self, event):
        elapsed_time = time.time() - self.start_time
        segundos = self.segundos - elapsed_time
        if segundos < 0:
            segundos = 0
        self.set_text(segundos/60, segundos%60, (segundos%1)*100)
        
        if segundos == 0:
            self.emit(SIGNAL("ESTADO_TIMER_FINALIZADO"))
            self.timer.stop()
            #QObject.disconnect(self, SIGNAL("ESTADO_TIMER_FINALIZADO"), self.window.estado_timer_finalizado)
        
    def set_text(self, minutos, segundos, centesimas):
        self.label.setText('%02d:%02d:%02d' % (minutos, segundos, centesimas))
    
class Round(EstadoTimer):
    gong = QSound('sounds/gong.wav')
    beep = QSound('sounds/beep-7.wav')
    next_beep = 10
	
    def __init__(self, numero=1, minutos=0, segundos=20, label=None, window=None):
        self.numero = numero
        super(Round, self).__init__(minutos=minutos, segundos=segundos, label=label, window=window)
        
    def __str__(self):
        return "Round "+str(self.numero)
    
    def timerEvent(self, event):
        elapsed_time = time.time() - self.start_time
        segundos = self.segundos - elapsed_time
        
        if segundos <= self.next_beep and self.next_beep > 0:
            self.next_beep -= 1
            self.beep.play()
        
        if segundos < 0:
            segundos = 0
        self.set_text(segundos/60, segundos%60, (segundos%1)*100)
        
        if segundos == 0:
            self.gong.play()
            self.emit(SIGNAL("ESTADO_TIMER_FINALIZADO"))
            self.timer.stop()


class Descanso(EstadoTimer):
    def __init__(self, minutos=0, segundos=10, label=None, window=None):
        super(Descanso, self).__init__(minutos=minutos, segundos=segundos, label=label, window=window)
        
    def __str__(self):
        return "Descanso"
    
class VentanaTimer(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_watch()
        self.ui.setupUi(self)
        
        self.rounds = 3
        self.round_actual = 1
        self.estado = Round(numero=self.round_actual, label=self.ui.lb_watch, window=self)
        self.ui.labelEstado.setText(str(self.estado))
        
    @pyqtSignature("")
    def on_btn_start_clicked(self):        
        if not self.estado.is_active():
            self.estado.start()
            self.ui.btn_start.setText("Detener")
        else:
            self.estado.pause()
            self.ui.btn_start.setText("Continuar")
            
    @pyqtSignature("")
    def on_btn_reset_clicked(self):                                   
        """ Reinicio mi cronometro. """
        self.estado.reset()
        self.estado.start()
        self.ui.btn_start.setText("Detener")

    @pyqtSignature("")
    def on_btn_stop_clicked(self):
        """ Reinicio el cronometro pero lo dejo pausado """
        self.estado.reset()
        self.ui.btn_start.setText("Start")
    
    @pyqtSignature("")
    def on_btn_back_clicked(self):
        """ Vuelvo al Round 1 para cronometrar un nuevo combate """
        self.round_actual = 1
        self.estado = Round(numero=self.round_actual, label=self.ui.lb_watch, window=self)
        self.ui.btn_start.setText("Start")
        self.ui.labelEstado.setText(str(self.estado))
        self.ui.btn_start.setEnabled(True)
        self.ui.btn_stop.setEnabled(True)
        self.ui.btn_reset.setEnabled(True)
    
    def estado_timer_finalizado(self):
        if isinstance(self.estado, Round):
            if self.round_actual < self.rounds:
                self.estado = Descanso(label=self.ui.lb_watch, window=self)
                self.round_actual += 1
                self.ui.btn_start.setText("Start")
            else:
                self.ui.btn_start.setText("Finalizado")
                self.ui.btn_start.setDisabled(True)
                self.ui.btn_stop.setDisabled(True)
                self.ui.btn_reset.setDisabled(True)
        elif isinstance(self.estado, Descanso):
            self.estado = Round(numero=self.round_actual, label=self.ui.lb_watch, window=self)
            self.ui.btn_start.setText("Start")
        self.ui.labelEstado.setText(str(self.estado))
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = VentanaTimer()
    myapp.show()
    sys.exit(app.exec_())
