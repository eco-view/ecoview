import numpy as np
import RPi.GPIO as GPIO
from time import sleep
# real one~~~~
# LEDlogic = {
# "Bit0": 14,
# "Bit1": 15,
# "Bit2": 18,
# }
# GPIO.setmode(GPIO.BCM)
class LEDlogic(object):
    """docstring for LEDlogic.
    Binary format: [Bit2, Bit1, Bit0]
    """

    def __init__(self, Bit2Pin, Bit1Pin, Bit0Pin):
        self.Bit0Pin = Bit0Pin
        self.Bit1Pin = Bit1Pin
        self.Bit2Pin = Bit2Pin
        self.LEDpins = [Bit2Pin, Bit1Pin, Bit0Pin]
        self.LastCall = None
        self.Logging = True


    def setLogging(self, printLogs):
        if printLogs == True:
            self.Logging = True
        elif printLogs == False:
            self.Logging = False
        else:
            print("Error: argument must be True or False")


    def Verbose(self):
        print("\n___LEDs___")
        print("[Logging: {}]".format(self.Logging))
        print("Bit0 Pin: {}".format(self.Bit0Pin))
        print("Bit1 Pin: {}".format(self.Bit1Pin))
        print("Bit2 Pin: {}".format(self.Bit2Pin))
        print("Pin List: {}".format(self.LEDpins))
        print("__________\n")


    def activatePins(self, LEDlist=[0, 0, 0], CycleTime=1):
        if LEDlist == [0, 0, 0]: LEDlist = [1, 1, 1]
        Pin0 = self.Bit0Pin
        Pin1 = self.Bit1Pin
        Pin2 = self.Bit2Pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(Pin0, GPIO.OUT)
        GPIO.setup(Pin1, GPIO.OUT)
        GPIO.setup(Pin2, GPIO.OUT)
        try:
            MyList = np.multiply(LEDlist, self.LEDpins).tolist()
            if self.Logging == True: print("MyList: {}".format(MyList))
            if self.Logging == True: print("LEDpins: {}".format(self.LEDpins))
            for i in range(-1, -4, -1):
                if self.LEDpins[i] & MyList[i]:
                    if self.Logging == True: print("Pin {} turning ON".format(self.LEDpins[i]))
                    GPIO.output(self.LEDpins[i], True)
                else:
                    if self.Logging == True: print("Pin {} should be OFF".format(self.LEDpins[i]))
                    GPIO.output(self.LEDpins[i], False)
            if self.Logging == True: print("Sleeping for {} sec..".format(CycleTime/2))
            sleep(CycleTime/2)
        except:
            if self.Logging == True: print("Unable to activate LED pins")
        finally:
            GPIO.cleanup()
            if self.Logging == True: print("All pins should be OFF")
            if self.Logging == True: print("Sleeping for {} sec..".format(CycleTime/2))
            sleep(CycleTime/2)


    def BinaryList(self, Integer):
        return [int(d) for d in bin(Integer)[2:].zfill(3)]


    def Strobe(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for x in range(len(self.LEDpins)):
            GPIO.setup(self.LEDpins[x], GPIO.OUT, initial=1)
        sleep(0.05)
        # if GPIO.input(self.LEDpin) == True:
        #     pass
        # else:
        #     GPIO.setup(self.LEDpin, GPIO.OUT, initial=1)

# LEDs = LEDlogic(Bit0=14, Bit1=15, Bit2=18)
# LEDlist=[1, 0, 0]
# while True:
#     LEDs.activatePins(LEDlist)
#
# print("EOF")

# LEDs.activatePins(LEDlist=[1, 0, 0])
# LEDs.activatePins(LEDlist=[0, 1, 0])
# LEDs.activatePins(LEDlist=[0, 0, 1])


# print(PINassignments["Tote1"])   # access single dictionary
# print(PINassignments["Tote1"]["ECHOpin"])   # access individual value

# print(PINassignments["Tote1"]["TRIGpin"])
# print(PINassignments["Tote1"]["ECHOpin"])

# for key, value in PINassignments.items():
#     print(key)
#     print(value["TRIGpin"])
#     print(value["ECHOpin"])
