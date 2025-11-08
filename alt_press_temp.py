#!/usr/bin/env python

import time
from subprocess import PIPE, Popen

from smbus2 import SMBus

from bmp280 import BMP280

print("""compensated-temperature.py - Use the CPU temperature to compensate temperature
readings from the BMP280 sensor. Method adapted from Initial State's Enviro pHAT
review: https://medium.com/@InitialState/tutorial-review-enviro-phat-for-raspberry-pi-4cd6d8c63441

Press Ctrl+C to exit!

""")

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)


# Gets the CPU temperature in degrees C
from subprocess import Popen, PIPE

def get_cpu_temperature():
    process = Popen(["vcgencmd", "measure_temp"], stdout=PIPE)
    output, _error = process.communicate() # returns bytes
    # Decode bytes to string
    output = output.decode("utf-8")
   
    temp_str = output[output.index("=") + 1 : output.rindex("'")]
    return float(temp_str)

# Example usage
print(get_cpu_temperature())



factor = 1.2  # Smaller numbers adjust temp down, vice versa
smooth_size = 10  # Dampens jitter due to rapid CPU temp changes

cpu_temps = []

# Relative altitude calculation.
baseline_values = []
baseline_size = 50

print(f"Collecting baseline values for {baseline_size:d} seconds. Do not move the sensor!\n")

for i in range(baseline_size):
    pressure = bmp280.get_pressure()
    baseline_values.append(pressure)
    time.sleep(1)

baseline = sum(baseline_values[:-25]) / len(baseline_values[:-25])


while True:
    # Compenstated temperature
    cpu_temp = get_cpu_temperature()
    cpu_temps.append(cpu_temp)

    if len(cpu_temps) > smooth_size:
        cpu_temps = cpu_temps[1:]

    smoothed_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
    raw_temp = bmp280.get_temperature()
    comp_temp = raw_temp - ((smoothed_cpu_temp - raw_temp) / factor)

    print(f"Compensated temperature: {comp_temp:05.2f} *C")

    #temp print out
    temperature = bmp280.get_temperature()
    pressure = bmp280.get_pressure()
    print(f"{temperature:05.2f}*C {pressure:05.2f}hPa")

    # Altitude printout
    altitude = bmp280.get_altitude(qnh=baseline)
    print(f"Relative altitude: {altitude:05.2f} metres")

    time.sleep(1.0)
