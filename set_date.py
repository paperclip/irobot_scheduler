#!/bin/env python

import serial
import time

PORT="/dev/ttyUSB3"
BAUD_RATE=115200
ser = serial.Serial(PORT, baudrate=BAUD_RATE, timeout=0.5)

import irobot.openinterface.commands 
from irobot.openinterface import commands
from irobot.openinterface.commands import set_mode_full, request_sensor_data # or other commands
from irobot.openinterface.constants import RESPONSE_SIZES, DAYS
from irobot.openinterface.response_parsers import unsigned_byte_response
# open a serial connection
# assumed to be serial here
# change mode
ser.write(commands.start())
ser.write(commands.set_mode_passive())

now = time.localtime()

DAY_MAP = {
    0 : DAYS.MONDAY,
    1 : DAYS.TUESDAY,
    2 : DAYS.WEDNESDAY,
    3 : DAYS.THURSDAY,
    4 : DAYS.FRIDAY,
    5 : DAYS.SATURDAY,
    6 : DAYS.SUNDAY,
}

day = DAY_MAP[now.tm_wday]
hour = now.tm_hour
minute = now.tm_min

ser.write(commands.set_day_time(day, hour, minute))
ser.write(commands.set_mode_passive())
