import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import os
import picamera
from filemanager import FileManager
########


class Camera(object):
    """docstring for Camera."""

    def __init__(self, Logging=True, SWITCHpin=None, LEDpin=None):
        # super(picamera, self).__init__()
        self.ResolutionTuple = (128, 128)
        self.SWITCHpin = SWITCHpin
        self.LEDpin = LEDpin
        self.Logging = Logging


    def setLogging(self, printLogs):
        if printLogs == True:
            self.Logging = True
        elif printLogs == False:
            self.Logging = False
        else:
            print("Error: argument must be True or False")


    def Verbose(self):
        print("\n___CAMERA___")
        print("[Logging: {}]".format(self.Logging))
        print("SWITCHpin: {}".format(self.SWITCHpin))
        print("LEDpin: {}".format(self.LEDpin))
        print("Resolution: {}".format(self.ResolutionTuple))
        print("_____________\n")


    def readCameraSwitch(self):
        # Switch is between SWITCHpin & GND
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)
        GPIO.setup(self.SWITCHpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        if self.Logging == True: print("Checking Pin #{}".format(self.SWITCHpin))
        try:
            if GPIO.input(self.SWITCHpin) == 1:
                if self.Logging == True: print("\tSwitch is OFF")
                return False
            elif GPIO.input(self.SWITCHpin) == 0:
                if self.Logging == True: print("\tSwitch is ON")
                return True
        except:
            if self.Logging == True: print("\t\tEnding read process")
        finally:
            GPIO.cleanup()
            if self.Logging == True: print("\t\t\tPins are cleaned up")


    def CaptureAndSave(self, FM):
        with picamera.PiCamera() as camera:
            camera.resolution = self.ResolutionTuple
            camera.capture(FM.GenerateTimestampFilename()[1])
            print("Picture Taken 📸")


    def CameraLEDon(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.LEDpin, GPIO.OUT)
        if GPIO.input(self.LEDpin) == True:
            pass
        else:
            GPIO.setup(self.LEDpin, GPIO.OUT, initial=1)


    def CameraLEDoff(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)
        GPIO.setup(self.LEDpin, GPIO.OUT, initial=0)
