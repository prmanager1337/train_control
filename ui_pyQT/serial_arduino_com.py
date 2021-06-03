import serial 
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout = .1)
#arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout = None)

def write_serial_arduino(command):
    arduino.write(bytes(command, 'utf-8'))
    #data = arduino.read(2)
    #print(data)

    #data = b'1'
    #while True:
        #arduino.write(bytes(command, 'utf-8'))
        #data = arduino.read()
        #if data == b'0':
            #break
    #print(command)s