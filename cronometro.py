#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
from ui_clockwatch import Ui_watch
from PyQt4 import QtGui
from PyQt4.QtGui import QSound
from PyQt4.QtCore import *
# from PyQt4.QtCore import SIGNAL, pyqtSignature, QBasicTimer, QObject

class EstadoTimer(QObject):
    def __init__(self, minutos=2, segundos=0, label=None, window=None):
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
	
    def __init__(self, numero=1, minutos=1, segundos=30, label=None, window=None):
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
    beep_descanso = QSound('sounds/beep-9.wav')
    rest_beep = 10
    play_beep = True
	
    def __init__(self, minutos=1, segundos=0, label=None, window=None):
        super(Descanso, self).__init__(minutos=minutos, segundos=segundos, label=label, window=window)
        
    def __str__(self):
        return "Descanso"
		
    def timerEvent(self, event):
        elapsed_time = time.time() - self.start_time
        segundos = self.segundos - elapsed_time

        if segundos <= self.rest_beep and self.play_beep == True:
            self.play_beep = False
            self.beep_descanso.play()
        
        if segundos < 0:
            segundos = 0
        self.set_text(segundos/60, segundos%60, (segundos%1)*100)
        
        if segundos == 0:
            self.emit(SIGNAL("ESTADO_TIMER_FINALIZADO"))
            self.timer.stop()
    
class VentanaTimer(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_watch()
        self.ui.setupUi(self)
        self.maximized = True
        
        self.rounds = 1
        self.round_actual = 1
        self.estado = Round(numero=self.round_actual, label=self.ui.lb_watch, window=self)
        self.ui.labelEstado.setText(str(self.estado))
        
    @pyqtSignature("")
    def keyPressEvent(self, event):
        key = event.key()
        # Start / Stop
        if key == Qt.Key_S : 
            if not self.estado.is_active():
                self.estado.start()

            else:
                self.estado.pause()

        # Vuelvo al Round 1 para cronometrar un nuevo combate
        if key == Qt.Key_R or key == Qt.Key_1 :
            self.round_actual = 1
            self.estado = Round(numero=self.round_actual, label=self.ui.lb_watch, window=self)
            self.ui.labelEstado.setText(str(self.estado))

		# Reiniciar en round 2 o 3 (categoria full)
        if self.rounds >= 2 and key == Qt.Key_2 :
            self.round_actual = 2
            self.estado = Round(numero=self.round_actual, label=self.ui.lb_watch, window=self)
            self.ui.labelEstado.setText(str(self.estado))

        if self.rounds >= 3 and key == Qt.Key_3 :
            self.round_actual = 3
            self.estado = Round(numero=self.round_actual, label=self.ui.lb_watch, window=self)
            self.ui.labelEstado.setText(str(self.estado))
        
        # Maximizar ventana cronometro
        if key == Qt.Key_M :
            if self.maximized == False :
                self.showMaximized()
                self.maximized = True
            else:
                self.showNormal()
                self.maximized = False
			
        # Exit cronometro
        if key == Qt.Key_Escape :
            self.close()
            sys.exit(0)
    
    def estado_timer_finalizado(self):
        if isinstance(self.estado, Round):
            if self.round_actual < self.rounds:
                self.estado = Descanso(label=self.ui.lb_watch, window=self)
                self.round_actual += 1
                self.estado.start()
        elif isinstance(self.estado, Descanso):
            self.estado = Round(numero=self.round_actual, label=self.ui.lb_watch, window=self)
            #self.estado.start()
        self.ui.labelEstado.setText(str(self.estado))
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = VentanaTimer()
    # myapp.setWindowFlags(myapp.windowFlags() | Qt.SplashScreen);
    myapp.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowSystemMenuHint);
    myapp.showMaximized()
    #myapp.show()
    sys.exit(app.exec_())
