#!/usr/bin/env python

import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(14, RPi.GPIO.OUT)

for i in range(0, 10):
    RPi.GPIO.output(14, True)
    print "high"
    time.sleep(1.5)
    RPi.GPIO.output(14, False)
    print "low"
    time.sleep(0.5)

RPi.GPIO.cleanup()
