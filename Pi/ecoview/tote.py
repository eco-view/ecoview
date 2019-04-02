import time
from time import sleep
import RPi.GPIO as GPIO
import timeout_decorator


class Tote(object):
    """
    Tote class with assigned pins for operations
    All pin numbers referenced will be BCM
    By default, Logging is TRUE
    Call __obj__.setLogging(False) to disable.
    """
    def __init__(self, Number=None, SWITCHpin=None, BEAMpin=None, TRIGpin=None, ECHOpin=None):
        self.Number = Number
        self.Logging = True
        self.LEDcall = bin(Number)
        self.LEDlist = [int(d) for d in bin(Number)[2:].zfill(3)]
        self.SWITCHpin = SWITCHpin
        self.BEAMpin = BEAMpin
        self.TRIGpin = TRIGpin
        self.ECHOpin = ECHOpin


    def Verbose(self):
        print("\n___Tote #{}___".format(self.Number))
        print("[Logging: {}]".format(self.Logging))
        print("LED call: {}".format(self.LEDcall))
        print("LED list: {}".format(self.LEDlist))
        print("SWITCH pin: {}".format(self.SWITCHpin))
        print("BEAM pin: {}".format(self.BEAMpin))
        print("TRIG pin: {}".format(self.TRIGpin))
        print("ECHO pin: {}".format(self.ECHOpin))
        print("______________\n")


    def setLogging(self, printLogs):
        if printLogs == True:
            self.Logging = True
        elif printLogs == False:
            self.Logging = False
        else:
            print("Error: argument must be True or False")


    def senseDistance(self, maxPossible=2000):
        if self.Logging == True: print("Measuring Tote #{}".format(self.Number))
        try:
            TRIG = self.TRIGpin
            ECHO = self.ECHOpin
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(TRIG, GPIO.OUT)
            GPIO.setup(ECHO, GPIO.IN)
            GPIO.output(TRIG, False)
            time.sleep(0.01)
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
            distance = round(sig_time / 0.000058, 1)  # centimeters
            if distance > maxPossible:
                distance = maxPossible
            if self.Logging == True: print("Distance: {} cm".format(distance))
        except:
            distance = None
            if self.Logging == True: print("Unable to measure distance")
        finally:
            GPIO.cleanup()
            if self.Logging == True: print("Pins are cleaned up")
        return distance


    def convertToCapacity(self, measuredDistance=100, toteHeight=100):
        if self.Logging == True: print("Converting distance to percentage...")
        # in centimeters
        if measuredDistance > toteHeight:
            calculatedHeight = 0
        else:
            calculatedHeight = toteHeight - measuredDistance
        asAPercent = round(calculatedHeight / toteHeight * 100)
        if self.Logging == True: print("Current Capacity: {} % filled".format(asAPercent))
        return asAPercent


    def readBreakBeam(self):
        if self.Logging == True: print("Checking BEAM #{}  (Pin {})".format(self.Number, self.BEAMpin))
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        try:
            LEDpin = self.BEAMpin
            GPIO.setup(LEDpin, GPIO.IN)
            if GPIO.input(LEDpin) == True:
                response = False
                if self.Logging == True: print("Beam is NOT broken")
            else:
                response = True
                if self.Logging == True: print("Beam IS broken")
        except:
            response = None
            if self.Logging == True: print("Error reading beam")
        finally:
            GPIO.cleanup()
            if self.Logging == True: print("Pins are cleaned up")
            # sleep(0.01)
            return response


    def readSwitch(self):
        if self.Logging == True: print("Reading SWITCH #{}".format(self.Number))
        buttonPin = self.SWITCHpin
        GPIO.setwarnings(False)
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
            if GPIO.input(buttonPin) == False:
                if self.Logging == True: print("Button PUSHED")
                return True
            elif GPIO.input(buttonPin) == True:
                if self.Logging == True: print("Button NOT pushed")
                return False
        except:
            if self.Logging == True: print("Unable to read switch")
            return None
        finally:
            GPIO.cleanup()
            if self.Logging == True: print("Pins are cleaned up")


""" xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx """


# tote1 = Tote(Number=1, SWITCHpin=5, BEAMpin=26, TRIGpin=4, ECHOpin=18)
# tote1.setLogging(False)
# tote1.Verbose()
#
# # tote1.senseDistance()
# while True:
#     if tote1.readBreakBeam(): print("BEAM #1: TRUE")

# tote1.convertToCapacity()
# tote1.readSwitch()
# print(tote1.LEDlist[-1]) # LSB
# print(tote1.LEDlist)
