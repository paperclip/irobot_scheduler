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
from irobot.openinterface.response_parsers import unsigned_byte_response
# open a serial connection
# assumed to be serial here
# change mode
ser.write(commands.start())
ser.write(commands.set_mode_passive())

ser.write(commands.seek_dock())

ser.write(commands.set_mode_passive())
