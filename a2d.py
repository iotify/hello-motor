import time
# using the ADS1x15 module from Adafruit.
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115(busnum=1)
GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
while True:
    values = [0]*4
    for i in range(4):
        values[i] = adc.read_adc(i, gain=GAIN) * 0.1875
    # Print the ADC values.
    print('| {0:>6} mV | {1:>6} mV | {2:>6} mV | {3:>6} mV|'.format(*values))
    time.sleep(1)
