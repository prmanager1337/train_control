import serial 
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

def write_read(x): 
    

    while True:
        arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)
        data = arduino.readline()
        if data == b'1':
            break