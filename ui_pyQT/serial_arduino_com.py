import serial 
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

def write_serial_arduino(command): 
    while True:
        arduino.write(bytes(command, 'utf-8'))
        time.sleep(0.05)
        data = arduino.readline()
        if data == b'0':
            break
    print(command)