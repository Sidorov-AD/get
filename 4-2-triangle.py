import RPi.GPIO as GPIO
from time import sleep

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


try:
    val = input("Enter period in sec: ")
    try:
        while True:
            val = float(val)

            for i in range(256):
                GPIO.output(dac, dec2bin(i))
                sleep(val/2/256)
            for i in range(254, 0, -1):
                GPIO.output(dac, dec2bin(i))
                sleep(val/2/254)
            
    except Exception:
        print("You have to type a number, not string! Try again...")


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()