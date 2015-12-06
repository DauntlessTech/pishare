import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# get pin number to light up
pinNum = input(" LED POSITIVE PIN NUMBER : ")

GPIO.setup(pinNum,GPIO.OUT)

timeScaler = input(" BLINK RATE IN SECONDS (.1 == 1/10 of a second): ")
interval = input (" HOW MANY BLINKS : ")

while interval > 0:
	GPIO.output(pinNum,GPIO.HIGH)
	time.sleep(timeScaler)
	GPIO.output(pinNum,GPIO.LOW)
	time.sleep(timeScaler)
	interval = interval - 1
