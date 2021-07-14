# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-03-17
# =============================================================================
""""""
# =============================================================================
# Imports
from LedIndicatorWidget import *
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import *
from serial_arduino_com import write_serial_arduino
# =============================================================================

class TrainSwitch(QWidget):
    def __init__(self, parent, train_switch, command_routing):
        super(QWidget, self).__init__(parent)
        self.command_routing = command_routing
        self.train_switch = train_switch
        self.layout = QHBoxLayout()
        self.button = QPushButton()
        self.led = LedIndicator()
        self.button.setCheckable(True)
        self.button.setText("Växel " + train_switch)
        self.button.setStyleSheet(  "background-color: grey;" 
                                    "border-style: outset;"
                                    "border-width: 2px;"
                                    "border-radius: 10px;"
                                    "border-color: beige;"
                                    "font: bold 20px;"
                                    "min-width: 6em;"
                                    "min-height: 2.5em;"
                                    "padding: 2px;")

        self.led.setDisabled(True)  # Make the led non clickable

        self.led.on_color_1 = QColor(255, 0, 0)
        self.led.on_color_2 = QColor(176, 0, 0)
        self.led.off_color_1 = QColor(0, 255, 0)
        self.led.off_color_2 = QColor(0, 192, 0)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.led)

        self.button.clicked.connect(lambda: self.button_clicked())

    def button_clicked(self):
        self.led.setChecked(not self.led.isChecked())

        if self.button.isChecked(): 
            write_serial_arduino(self.command_routing + "1")

        else: 
            write_serial_arduino(self.command_routing + "2")

class quitApp(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.button = QPushButton()
        self.button.setCheckable(True)
        self.button.setText("Exit Application")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(lambda: self.button_clicked())

    def button_clicked(self):
        QCoreApplication.quit()


class windowLayout(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        switch_button = 1
        self.MapLayout = QHBoxLayout()
        self.ButtonLayout = QGridLayout()
        self.ButtonLayout.setAlignment(Qt.AlignLeft)          

        for i in range(0, 8):
            for j in range(0, 5):
                self.switch_button =  TrainSwitch(self, str(switch_button), "11")
                self.ButtonLayout.addLayout(self.switch_button.layout, i, j)
                switch_button += 1

        self.button_quit = quitApp(self)       
        self.ButtonLayout.addLayout(self.button_quit.layout, switch_button / 4, j)

        self.MapLayout.addLayout(self.ButtonLayout)
        self.setLayout(self.MapLayout)  

              
