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
from serial_arduino_com import *
# =============================================================================

class TrainSwitch(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.button = QPushButton()
        self.led1 = LedIndicator()
        self.led2 = LedIndicator()
        self.led2.setChecked(True)

        self.led1.setDisabled(True)  # Make the led non clickable
        self.led2.setDisabled(True)  # Make the led non clickable

        self.led2.on_color_1 = QColor(255, 0, 0)
        self.led2.on_color_2 = QColor(176, 0, 0)
        self.led2.off_color_1 = QColor(28, 0, 0)
        self.led2.off_color_2 = QColor(156, 0, 0)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.led1)
        self.layout.addWidget(self.led2)

        self.button.clicked.connect(lambda: self.button_clicked())

    def button_clicked(self):
        self.led1.setChecked(not self.led1.isChecked())
        self.led2.setChecked(not self.led2.isChecked())

class windowLayout(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.MapLayout = QHBoxLayout()
        self.ButtonLayout = QGridLayout()
        self.ButtonLayout.setAlignment(Qt.AlignLeft)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ButtonLayout.addItem(self.verticalSpacer,1 ,0)

        self.button_1 = TrainSwitch(self)
        self.button_1.button.setText("Växel 1")
        self.ButtonLayout.addLayout(self.button_1.layout, 0, 0)

        self.button_2 = TrainSwitch(self)
        self.button_2.button.setText("Växel 2")
        self.ButtonLayout.addLayout(self.button_2.layout, 0, 1)

        self.button_3 = TrainSwitch(self)
        self.button_3.button.setText("Växel 3")
        self.ButtonLayout.addLayout(self.button_3.layout, 0, 2)

        self.MapLayout.addLayout(self.ButtonLayout)
        self.setLayout(self.MapLayout)        
