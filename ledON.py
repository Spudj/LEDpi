import RPi.GPIO as GPIO

pin = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, True)
