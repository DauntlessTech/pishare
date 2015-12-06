import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.IN)
GPIO.setup(27,GPIO.OUT)

pinNum = input(" LED POSITIVE PIN NUMBER : ")

while True:
	if GPIO.input(pinNum) == True:
		GPIO.output(27,GPIO.HIGH)
	elif GPIO.input(pinNum) == False:
		GPIO.output(27,GPIO.LOW)
