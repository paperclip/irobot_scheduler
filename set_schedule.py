#!/bin/env python

import os
import serial
import sys
import time

if len(sys.argv) > 1:
    PORT = sys.argv[1]
else:
    PORT=os.environ.get("PORT", "COM1") # /dev/ttyUSB0

import irobot.openinterface.commands 
from irobot.openinterface import commands
from irobot.openinterface.commands import set_mode_full, request_sensor_data # or other commands
from irobot.openinterface.constants import RESPONSE_SIZES, DAYS
from irobot.openinterface.response_parsers import unsigned_byte_response
# open a serial connection
BAUD_RATE=115200
ser = serial.Serial(PORT, baudrate=BAUD_RATE, timeout=0.5)

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

hour = 9
minute = 30

sun_hour = hour
sun_min = minute

mon_hour = hour
mon_min = minute

tues_hour = hour
tues_min = minute

wed_hour = hour
wed_min = minute

thurs_hour = hour
thurs_min = minute

fri_hour = hour
fri_min = minute

sat_hour = hour
sat_min = minute

ser.write(commands.set_schedule(
    sun_hour, sun_min,
    mon_hour, mon_min, 
    tues_hour, tues_min, 
    wed_hour, wed_min, 
    thurs_hour, thurs_min,
    fri_hour, fri_min, 
    sat_hour, sat_min
)
)

ser.write(commands.set_mode_passive())

# read oi mode
ser.write(request_sensor_data(35))
response = ser.read(RESPONSE_SIZES[35])
print(repr(response))
ret = unsigned_byte_response(response)
print("OI mode:",ret)
