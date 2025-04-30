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
    adc_val = 0
    GPIO.output(dac, 0)
    # for i in range(8):
    #     GPIO.output(dac[i], 1)
    #     sleep(0.001)
    #     cmp_val = GPIO.input(comp)
    #     cmp[i] = (cmp_val == 0)
    #     GPIO.output(dac[i], cmp[i])
    #     adc_val += cmp[i] * 128 // (2**i)
    GPIO.output(dac[0], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[0], 0)
    else:
        adc_val += 128

    GPIO.output(dac[1], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[1], 0)
    else:
        adc_val += 64

    GPIO.output(dac[2], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[2], 0)
    else:
        adc_val += 32

    GPIO.output(dac[3], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[3], 0)
    else:
        adc_val += 16

    GPIO.output(dac[4], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[4], 0)
    else:
        adc_val += 8

    GPIO.output(dac[5], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[5], 0)
    else:
        adc_val += 4

    GPIO.output(dac[6], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[6], 0)
    else:
        adc_val += 2

    GPIO.output(dac[7], 1)
    sleep(0.001)
    if(GPIO.input(comp)):
        GPIO.output(dac[7], 0)
    else:
        adc_val += 1
    
    return adc_val

try:
    while True:
        adc_val = adc()
        voltage = adc_val / 256.0 * 3.3
        print("Adc value: {:3d}, Voltage: {:.2f}".format(adc_val, voltage))


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()