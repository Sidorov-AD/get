import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        dac_val = dec2bin(i)
        GPIO.output(dac, dac_val)
        sleep(0.001)
        cmp = GPIO.input(comp)
        if cmp:
            return i
    return 256

try:
    while True:
        adc_val = adc()
        voltage = adc_val / 256.0 * 3.3
        print("Adc value: {:3d}, Voltage: {:.2f}".format(adc_val, voltage))


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()