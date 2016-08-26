import time
# using the ADS1x15 module from Adafruit.
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115(busnum=1)
GAIN = 1

print('Reading ADS1x15 Input voltage values in millivolt, press Ctrl-C to quit...')
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
while True:
    values = [0]*4
    for i in range(4):
        # at PGA setting 1, 32767 steps correspond to 4096 millivolt
        values[i] = adc.read_adc(i, gain=GAIN, data_rate=32) * 0.125
    # Print the ADC values.
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} | (millivolt)'.format(*values))
    time.sleep(1)
