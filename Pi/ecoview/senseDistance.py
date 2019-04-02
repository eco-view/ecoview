import RPi.GPIO as GPIO
import time
    # TRIG = 4
    # ECHO = 18
def measureHeight(TRIG, ECHO):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    time.sleep(0.1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        # print("startTime")
        startTime = time.time()

    while GPIO.input(ECHO) == 1:
        # print("stopTime")
        stopTime = time.time()

    sig_time = stopTime - startTime
    # centimeters
    distance = sig_time / 0.000058
    print("Distance: {} cm".format(round(distance, 1)))
    GPIO.cleanup()
    return round(distance, 1)

#
