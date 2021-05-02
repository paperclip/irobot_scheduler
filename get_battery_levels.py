#!/bin/env python

import serial
import sys
import time

if len(sys.argv) > 1:
    PORT = sys.argv[1]
else:
    PORT="/dev/ttyUSB0"

BAUD_RATE=115200
ser = serial.Serial(PORT, baudrate=BAUD_RATE, timeout=0.5)

import irobot.openinterface.commands 
from irobot.openinterface import commands
from irobot.openinterface.constants import RESPONSE_SIZES
from irobot.openinterface.response_parsers import SensorGroup3
# open a serial connection
# assumed to be serial here
# change mode
ser.write(commands.start())
ser.write(commands.set_mode_passive())

# read battery info
def request_data(field):
    ser.write(commands.request_sensor_data(field))
    return ser.read(RESPONSE_SIZES[field])

data = request_data(3)
assert data is not None
print(repr(data))
print([ "%x"%c for c in data ])
battery_status = SensorGroup3(data)
print("charging_state:", battery_status.charging_state)
print("voltage:", battery_status.voltage)
print("current:", battery_status.current)
print("temperature:", battery_status.temperature)
print("battery_charge:", battery_status.battery_charge)
print("battery_capacity:", battery_status.battery_capacity)

ser.write(commands.set_mode_passive())
