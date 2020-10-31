#test.py
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setwarnings(False)

GPIO.output(2, 0)
GPIO.output(3, 0)
GPIO.output(4, 0)

try:
	while(True):
		request = input("RGB-->")
		if(len(request) == 3):
			GPIO.output(2, int(request[0]))
			GPIO.output(3, int(request[1]))
			GPIO.output(4, int(request[2]))
		elif(request == "EXIT"):
			GPIO.output(2, 0)
			GPIO.output(3, 0)
			GPIO.output(4, 0)
			break
except KeyboardInterrupt:
	GPIO.cleanup()





