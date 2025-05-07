import RPi.GPIO as GPIO
from time import sleep, time
import matplotlib.pyplot as plt

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

pow_two = [128, 64, 32, 16, 8, 4, 2, 1]
def adc():
    adc_val = 0
    GPIO.output(dac, 0)
    for i in range(8):
        GPIO.output(dac[i], 1)
        sleep(0.0012)
        if GPIO.input(comp) == 0:
            adc_val += pow_two[i]
        else:
            GPIO.output(dac[i], 0)
    return adc_val

lst = []
val = 0
koef = 3.3/256

try:
    GPIO.output(troyka, 1)
    time_start = time()

    while val < 206:
        val = adc()
        vlt = val * koef
        # print(f"Val: {val:3d}, Voltage: {vlt:.2f}, Stat: 1")
        lst.append(vlt)

    GPIO.output(troyka, 0)
        
    while val > 192:
        val = adc()
        vlt = val * koef
        # print(f"Val: {val:3d}, Voltage: {vlt:.2f}, Stat: 0")
        lst.append(vlt)
        
    time_stop = time()

    all_time = time_stop - time_start

    with open("data.txt", "w") as f:
        data = ""
        for i in lst:
            data += str(i) + '\n'
        f.write(data)

    with open("settings.txt", "w") as f:
        f.write(f"Частота дискретизации: {len(lst)/all_time} Гц\nШаг квантования:{3.3/256:.3f} V")
    
    print(f"Время: {all_time} с")
    print(f"Период: {all_time/len(lst)} с")
    print(f"Частота дискретизации: {len(lst)/all_time} Гц")
    print(f"Шаг квантования:{3.3/256:.3f} V")

    plt.plot(lst)
    plt.show()

finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup() 