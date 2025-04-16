import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def GetVoltage(value):
    d = 3.3 * 1/2
    voltage = 0
    for i in value:
        voltage += i * d
        d /= 2
    return voltage


try:
    while True:
        val = input("Write num from 0 to 255: ")

        try:
            val = int(val)
            if val in range(0,256):
                val_bin = decimal2binary(val)
                GPIO.output(dac, val_bin)
                print(f"Voltage is about {GetVoltage(val_bin):.4} volt")
            else:
                print("Number must be in range [0,255]!")

        except Exception:
            if val == "q": 
                break
            else:
                print("You have to type a number, not string! Try again...")


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()