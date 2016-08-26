import RPi.GPIO as GPIO
import numpy as np
import time
GPIO.setmode(GPIO.BCM)

STEP_BENBL = 7
DIR_BPHASE = 8
M1 = 9
M0_APHASE = 10
NSLEEP = 11
NFAULT = 14
NENBL_AENBL = 15
CONFIG = 17

steps = -10

print "Motor rotation by %g steps" % (steps)

GPIO.setup(STEP_BENBL, GPIO.OUT)
GPIO.setup(DIR_BPHASE, GPIO.OUT)
GPIO.setup(NSLEEP, GPIO.OUT)
GPIO.setup(NFAULT, GPIO.IN)
GPIO.setup(NENBL_AENBL, GPIO.OUT)
GPIO.setup(CONFIG, GPIO.OUT)

indexer_mode = True

GPIO.output(NSLEEP, False)
GPIO.output(CONFIG, indexer_mode)
GPIO.output(NSLEEP, True)
time.sleep(0.001)
while GPIO.input(NFAULT)==0:
	time.sleep(0.001)

if indexer_mode:

	GPIO.output(NENBL_AENBL, False)
	if steps < 0:
		GPIO.output(DIR_BPHASE, False)
		steps = -steps
	else:
		GPIO.output(DIR_BPHASE, True)
	step_unit = 1.0/4
	if step_unit == 1:
	        GPIO.setup(M1, GPIO.OUT)
	        GPIO.output(M1, False)
	        GPIO.setup(M0_APHASE, GPIO.OUT)
	        GPIO.output(M0_APHASE, False)
	elif step_unit == 1.0/2:
	        GPIO.setup(M1, GPIO.OUT)
	        GPIO.output(M1, False)
	        GPIO.setup(M0_APHASE, GPIO.OUT)
	        GPIO.output(M0_APHASE, True)
	elif step_unit == 1.0/4:
	        GPIO.setup(M1, GPIO.OUT)
	        GPIO.output(M1, False)
	        GPIO.setup(M0_APHASE, GPIO.IN)
	elif step_unit == 1.0/8:
	        GPIO.setup(M1, GPIO.OUT)
	        GPIO.output(M1, True)
	        GPIO.setup(M0_APHASE, GPIO.OUT)
	        GPIO.output(M0_APHASE, False)
	elif step_unit == 1.0/16:
	        GPIO.setup(M1, GPIO.OUT)
	        GPIO.output(M1, True)
	        GPIO.setup(M0_APHASE, GPIO.OUT)
	        GPIO.output(M0_APHASE, True)
	elif step_unit == 1.0/32:
	        GPIO.setup(M1, GPIO.OUT)
	        GPIO.output(M1, True)
	        GPIO.setup(M0_APHASE, GPIO.IN)
	for count in np.arange(0, steps, step_unit):
		time.sleep(0.05)
		GPIO.output(STEP_BENBL, True)
		time.sleep(0.05)
		GPIO.output(STEP_BENBL, False)

else:
	# phase/enable mode
	GPIO.setup(M0_APHASE, GPIO.OUT)
	electr_angle = 45
        GPIO.output(M0_APHASE, True)
        GPIO.output(NENBL_AENBL, True)
        GPIO.output(DIR_BPHASE, True)
        GPIO.output(STEP_BENBL, True)
	if steps > 0:
		step_unit = 0.5
	else:
		step_unit = -0.5
	for count in np.arange(0, steps, step_unit):
		if steps > 0:
			electr_angle += 45
			if electr_angle > 180:
				electr_angle -= 360
		else:
			electr_angle -= 45
			if electr_angle < -180:
                                electr_angle += 360
		if (electr_angle == 0) or (electr_angle == 180) or (electr_angle == -180):
			GPIO.output(STEP_BENBL, False)
                elif (electr_angle == 90) or (electr_angle == -90):
                        GPIO.output(NENBL_AENBL, False)
		elif electr_angle == 45:
			GPIO.output(M0_APHASE, True)
                        GPIO.output(NENBL_AENBL, True)
			GPIO.output(DIR_BPHASE, True)
			GPIO.output(STEP_BENBL, True)
                elif electr_angle == 135:
                        GPIO.output(M0_APHASE, False)
                        GPIO.output(NENBL_AENBL, True)
                        GPIO.output(DIR_BPHASE, True)
                        GPIO.output(STEP_BENBL, True)
                elif electr_angle == -135:
                        GPIO.output(M0_APHASE, False)                           
                        GPIO.output(NENBL_AENBL, True)
                        GPIO.output(DIR_BPHASE, False)
                        GPIO.output(STEP_BENBL, True)
                elif electr_angle == -45:
                        GPIO.output(M0_APHASE, True)
                        GPIO.output(NENBL_AENBL, True)
                        GPIO.output(DIR_BPHASE, False)
                        GPIO.output(STEP_BENBL, True)

GPIO.cleanup()
