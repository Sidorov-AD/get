import RPi.GPIO as GPIO

pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 1000)
pwm.start(0)

try:
    while True:

        val = input("Enter duty from 0.0 to 100.0: ")

        try:
            val = float(val)
            if 0 <= val <= 100:
                pwm.ChangeDutyCycle(val)
                print("Voltage: {:.4f}".format(val * 3.3/100))
            else:
                print("Duty must be in range [0.0, 100.0]!")

        except Exception:
            print("You have to type a number, not string! Try again...")
            

finally:
    pwm.stop()
    GPIO.output(pin, 0)
    GPIO.cleanup()