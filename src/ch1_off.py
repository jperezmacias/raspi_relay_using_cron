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


gpio.output(relay_channel_1, gpio.HIGH) 
gpio.output(relay_channel_2, gpio.HIGH) 
gpio.output(relay_channel_3, gpio.HIGH) 

