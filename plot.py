import matplotlib.pyplot as plt
import numpy as np

with open("settings.txt", "r") as settings_file:
    settings_data = [float(num) for num in settings_file.read().split("\n")]

time_step = settings_data[0]
voltage_step = settings_data[1]

data_arr = np.loadtxt("data.txt", dtype=int)

time_arr = np.arange(0, len(data_arr)) * time_step
voltage_arr = data_arr * voltage_step

voltage_max_index = np.argmax(voltage_arr)
voltage_max = np.max(voltage_arr)
time_max = np.max(time_arr)

charge_time = time_arr[voltage_max_index]
discharge_time = time_max - charge_time

figure, ax = plt.subplots(figsize = (16, 10), dpi = 400)

ax.set_xlabel("Время, с", fontsize = 16)
ax.set_ylabel("Напряжение, В", fontsize = 16)
ax.set_title("График зарядки и разрядки RC-цепи", fontsize = 20, loc= 'center', wrap=True)

ax.set_xlim([np.min(time_arr), np.max(time_arr)])
ax.set_ylim([np.min(voltage_arr), np.max(voltage_arr) + 0.2])

ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.125))

ax.grid(which='both', ls='-.', c='gray')

ax.text(time_max*0.7, voltage_max*0.8, f"Время заряда: {charge_time}", fontsize=16, c='black')
ax.text(time_max*0.7, voltage_max*0.7, f"Время разряда: {discharge_time}", fontsize=16, c='black')

ax.plot(time_arr, voltage_arr, color = 'blue', ls='-', lw=3, marker='o', ms=8, mfc='blue', markevery=15, label='V(t)')
ax.legend(fontsize=20)

# plt.show()
plt.savefig("plot.svg")
