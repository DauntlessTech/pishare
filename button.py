import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.IN)
GPIO.setup(27,GPIO.OUT)

while True:
	if GPIO.input(17) == False:
		GPIO.output(27,GPIO.HIGH)
		time.sleep(1)
		print("The sytem will restart in 5 seconds, PRESS CTRL + C TO QUIT NOW...")
		time.sleep(5)
		os.system("shutdown now -r")
	elif GPIO.input(17) == True:
		GPIO.output(27,GPIO.LOW)
