import serial 
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout = None)
#arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout = None)

def write_serial_arduino(command): 
    while True:
        arduino.write(bytes(command, 'utf-8'))
        data = arduino.read()
        if data == b'0':
            break
    print(command)