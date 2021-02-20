#! /usr/bin/env python
# -*- coding:utf-8 -*-
#______________________________________________________________
#
# pin 26 -> relay channel 1
# pin 20 -> relay channel 2
# pin 21 -> relay channel 3
#______________________________________________________________
#
import RPi.GPIO as gpio
import time
import datetime

gpio.cleanup() 
gpio.setwarnings(False)
 
# define BMC based pin counting
 
gpio.setmode(gpio.BCM)
 
relay_channel_1 = 26
relay_channel_2 = 20
relay_channel_3 = 21
 
# setup of gpio pins defined
 
gpio.setup(relay_channel_1, gpio.OUT)
gpio.setup(relay_channel_2, gpio.OUT)
gpio.setup(relay_channel_3, gpio.OUT)

start = datetime.time(6, 0, 0)
end = datetime.time(18, 0, 0)

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

gpio.output(relay_channel_1, gpio.HIGH)
gpio.output(relay_channel_2, gpio.HIGH)
gpio.output(relay_channel_3, gpio.HIGH)

time.sleep(1.0)

print(datetime.datetime.now())
print(datetime.datetime.now().time())
time.sleep(1.0)


print(time_in_range(start, end, datetime.datetime.now().time()))

if (time_in_range(start, end, datetime.datetime.now().time())):
    gpio.output(relay_channel_1, gpio.LOW)
    gpio.output(relay_channel_2, gpio.LOW)
    gpio.output(relay_channel_3, gpio.LOW)

    print('I am here')

