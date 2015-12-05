import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)

timeScaler = .1
interval = 10

while interval > 0:
	GPIO.output(17,GPIO.HIGH)
	time.sleep(timeScaler)
	GPIO.output(17,GPIO.LOW)
	time.sleep(timeScaler)
	interval = interval - 1
