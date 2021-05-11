# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-05-11
# =============================================================================
"""Sends a command to an arduino with the command to change the state of a
output pin. The command is sent over I2C frokm the master device of the 
Raspberry PI to a ATMEGA328-PU"""
# =============================================================================
# Imports
from smbus import SMBus
# =============================================================================

def write_i2c_arduino(command): 
    address = round(command / 100) + 1 
    command_send = command % 100

    bus = SMBus(1) #indicates /dev/ic2-1
    bus.write_byte(address, 0x2)

    print(command)