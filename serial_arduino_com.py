#import serial 
#import time

#arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

def write_serial_arduino(x): 
    #while True:
        #arduino.write(bytes(command, 'utf-8'))
        #time.sleep(0.05)
        #data = arduino.readline()
        #if data == b'1':
           # break
    print(x)


def train_switch_1():
    write_serial_arduino("1")

def train_switch_2():
    write_serial_arduino("2")

def train_switch_3():
    write_serial_arduino("3")

def train_switch_4():
    write_serial_arduino("4")

def train_switch_5():
    write_serial_arduino("5")

def train_switch_6():
    write_serial_arduino("6")

def train_switch_7():
    write_serial_arduino("7")

def train_switch_8():
    write_serial_arduino("8")

def train_switch_9():
    write_serial_arduino("9")

def train_switch_10():
    write_serial_arduino("10")

def train_switch_11():
    write_serial_arduino("11")

def train_switch_12():
    write_serial_arduino("12")

def train_switch_13():
    write_serial_arduino("13")

def train_switch_14():
    write_serial_arduino("14")

def train_switch_15():
    write_serial_arduino("15")

def train_switch_16():
    write_serial_arduino("16")

def train_switch_17():
    write_serial_arduino("17")

def train_switch_18():
    write_serial_arduino("18")

def train_switch_19():
    write_serial_arduino("19")