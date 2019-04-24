import RPi.GPIO as GPIO
from time import sleep
from LEDlogic import LEDlogic
from math import ceil

LEDs = LEDlogic(Bit0Pin=14, Bit1Pin=15, Bit2Pin=18)
LEDs.Verbose()

# helper func to produce ground_truth values
def BinaryList(Integer):
    return [int(d) for d in bin(Integer)[2:].zfill(3)]

def testByInteger(sleepTime=0.01,Integer=0):
    try:
        print("Testing case < {} >".format(Integer))
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)
        GPIO.setup(LEDs.Bit0Pin, GPIO.OUT, initial=0)
        GPIO.setup(LEDs.Bit1Pin, GPIO.OUT, initial=0)
        GPIO.setup(LEDs.Bit2Pin, GPIO.OUT, initial=0)
        toActivate = []
        for pin, val in zip(LEDs.LEDpins,BinaryList(Integer)):
            if pin and val:
                toActivate.append(pin)
        for pin in toActivate:
            print("\tActivating Pin: {}".format(pin))
            GPIO.output(pin, True)
        sleep(sleepTime)
    except:
        pass
    finally:
        GPIO.cleanup()

def runTestByInteger(sleepTime):
    print("Testing COUNT function   [CTRL + C] to END")
    try:
        for x in range(8):
            testByInteger(sleepTime=sleepTime,Integer=x)
    except KeyboardInterrupt:
        pass
    finally:
        pass
    print("\n\n|runTestByInteger COMPLETE|\n\n")

def bounceLights(steps=30,sleepTime=0.2):
    if steps is None: steps = ceil(10 / sleepTime)
    hiLimit = 7
    loLimit = 1
    direction = 1
    number = 0
    lives = 0
    try:
        while lives < steps:
            if direction is 1:
                if number < hiLimit:
                    number += 1
                    print("\t\t\tLoop Number: {}".format(number))
                else:
                    number -= 1
                    direction = 0
                    print("\t\t\tLoop Number: {}".format(number))
            elif direction is 0:
                if number > loLimit:
                    number -= 1
                    print("\t\t\tLoop Number: {}".format(number))
                else:
                    number += 1
                    direction = 1
                    print("\t\t\tLoop Number: {}".format(number))
            lives += 1
            testByInteger(sleepTime=sleepTime,Integer=number)
    except:
        print("\nSAFELY QUIT")
    finally:
        print("\n\n|bounceLights COMPLETE|\n\n")
        

if __name__ == '__main__':
    runTestByInteger(sleepTime=0.5)
    bounceLights(steps=30,sleepTime=0.1)
    print("\n\nEOF")
