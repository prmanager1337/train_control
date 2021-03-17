# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-03-17
# =============================================================================
""""""
# =============================================================================
# Imports
from LedIndicatorWidget import *
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
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

        self.label = QLabel(self)
        pixmap = QPixmap('traingui1.png')
        self.label.setPixmap(pixmap)

        self.MapLayout = QHBoxLayout()
        self.TopLayout = QVBoxLayout()
        self.VerticalButtonLayout = QVBoxLayout()

        self.button_1 = TrainSwitch(self)
        self.button_1.button.setText("Växel 1")
        self.VerticalButtonLayout.addLayout(self.button_1.layout)
        self.button_1.button.clicked.connect(train_switch_1)

        self.button_2 = TrainSwitch(self)
        self.button_2.button.setText("Växel 2")
        self.VerticalButtonLayout.addLayout(self.button_2.layout)
        self.button_2.button.clicked.connect(train_switch_2)

        self.button_3 = TrainSwitch(self)
        self.button_3.button.setText("Växel 3")
        self.VerticalButtonLayout.addLayout(self.button_3.layout)
        self.button_3.button.clicked.connect(train_switch_3)

        self.button_4 = TrainSwitch(self)
        self.button_4.button.setText("Växel 4")
        self.VerticalButtonLayout.addLayout(self.button_4.layout)
        self.button_4.button.clicked.connect(train_switch_4)

        self.button_5 = TrainSwitch(self)
        self.button_5.button.setText("Växel 5")
        self.VerticalButtonLayout.addLayout(self.button_5.layout)
        self.button_5.button.clicked.connect(train_switch_5)

        self.button_6 = TrainSwitch(self)
        self.button_6.button.setText("Växel 6")
        self.VerticalButtonLayout.addLayout(self.button_6.layout)
        self.button_6.button.clicked.connect(train_switch_6)

        self.button_7 = TrainSwitch(self)
        self.button_7.button.setText("Växel 7")
        self.VerticalButtonLayout.addLayout(self.button_7.layout)
        self.button_7.button.clicked.connect(train_switch_7)

        self.button_8 = TrainSwitch(self)
        self.button_8.button.setText("Växel 8")
        self.VerticalButtonLayout.addLayout(self.button_8.layout)
        self.button_8.button.clicked.connect(train_switch_8)

        self.button_9 = TrainSwitch(self)
        self.button_9.button.setText("Växel 9")
        self.VerticalButtonLayout.addLayout(self.button_9.layout)
        self.button_9.button.clicked.connect(train_switch_9)

        self.button_10 = TrainSwitch(self)
        self.button_10.button.setText("Växel 10")
        self.VerticalButtonLayout.addLayout(self.button_10.layout)
        self.button_10.button.clicked.connect(train_switch_10)

        self.button_11 = TrainSwitch(self)
        self.button_11.button.setText("Växel 11")
        self.VerticalButtonLayout.addLayout(self.button_11.layout)
        self.button_11.button.clicked.connect(train_switch_11)

        self.button_12 = TrainSwitch(self)
        self.button_12.button.setText("Växel 12")
        self.VerticalButtonLayout.addLayout(self.button_12.layout)
        self.button_12.button.clicked.connect(train_switch_12)

        self.button_13 = TrainSwitch(self)
        self.button_13.button.setText("Växel 13")
        self.VerticalButtonLayout.addLayout(self.button_13.layout)
        self.button_13.button.clicked.connect(train_switch_13)

        self.button_14 = TrainSwitch(self)
        self.button_14.button.setText("Växel 14")
        self.VerticalButtonLayout.addLayout(self.button_14.layout)
        self.button_14.button.clicked.connect(train_switch_14)

        self.button_15 = TrainSwitch(self)
        self.button_15.button.setText("Växel 15")
        self.VerticalButtonLayout.addLayout(self.button_15.layout)
        self.button_15.button.clicked.connect(train_switch_15)

        self.button_16 = TrainSwitch(self)
        self.button_16.button.setText("Växel 16")
        self.VerticalButtonLayout.addLayout(self.button_16.layout)
        self.button_16.button.clicked.connect(train_switch_16)

        self.button_17 = TrainSwitch(self)
        self.button_17.button.setText("Växel 17")
        self.VerticalButtonLayout.addLayout(self.button_17.layout)
        self.button_17.button.clicked.connect(train_switch_17)

        self.button_18 = TrainSwitch(self)
        self.button_18.button.setText("Växel 18")
        self.VerticalButtonLayout.addLayout(self.button_18.layout)
        self.button_18.button.clicked.connect(train_switch_18)

        self.button_19 = TrainSwitch(self)
        self.button_19.button.setText("Växel 19")
        self.VerticalButtonLayout.addLayout(self.button_19.layout)
        self.button_19.button.clicked.connect(train_switch_19)

        self.MapLayout.addLayout(self.VerticalButtonLayout)
        self.MapLayout.addWidget(self.label)
        self.setLayout(self.MapLayout)        
