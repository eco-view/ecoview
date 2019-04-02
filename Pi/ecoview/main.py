# CLASS
from tote import Tote
from deposits import TallyWizard
from LEDlogic import LEDlogic
from filemanager import FileManager
from camera import Camera
from createurl import CreateURL
from analyze import myModel
from logger import Logger
# UTILS
from time import sleep
import picamera
import timeout_decorator
import sys
#########

print("\nRUNNING main.py [CTRL+C TO EXIT]\n")

Log = Logger(GlobalLogging=False)   # False: LogToConsole   True: LogToLog
MyURL = CreateURL(url_root="http://192.168.1.3:5000/api/", token="abcde", machine=10001, Logging=True)
Tote0 = Tote(Number=0, SWITCHpin=17, BEAMpin=None, TRIGpin=None, ECHOpin=None)
Tote1 = Tote(Number=1, SWITCHpin=27, BEAMpin=None, TRIGpin=19, ECHOpin=None)
Tote2 = Tote(Number=2, SWITCHpin=22, BEAMpin=None, TRIGpin=19, ECHOpin=None)
Tote3 = Tote(Number=3, SWITCHpin=None, BEAMpin=None, TRIGpin=19, ECHOpin=None)
Tote4 = Tote(Number=4, SWITCHpin=None, BEAMpin=None, TRIGpin=19, ECHOpin=None)
Tote5 = Tote(Number=5, SWITCHpin=None, BEAMpin=None, TRIGpin=19, ECHOpin=None)
Tote6 = Tote(Number=6, SWITCHpin=None, BEAMpin=None, TRIGpin=19, ECHOpin=None)
LEDs = LEDlogic(Bit0Pin=14, Bit1Pin=15, Bit2Pin=18)
PiCam = Camera(SWITCHpin=25, LEDpin=22)
FM = FileManager(sub_directories=['0', '1', '2', 'NOID', 'cache'], Logging=False)
Tally = TallyWizard(Logging=False)
Model = myModel()

ToteList = [Tote0, Tote1, Tote2, Tote3, Tote4, Tote5, Tote6]
TimeOutTime = 3     # 6 for deployement

Tote0.setLogging(False)
Tote1.setLogging(False)
Tote2.setLogging(False)
Tote3.setLogging(False)
Tote4.setLogging(False)
Tote5.setLogging(False)
Tote6.setLogging(False)
PiCam.setLogging(False)
LEDs.setLogging(False)


def VerboseVerbose(ToteList):
    print("\n______CLASS DATA______")
    MyURL.Verbose()
    for tote in ToteList:
        tote.Verbose()
    FM.Verbose()
    PiCam.Verbose()
    LEDs.Verbose()
    print("________________________\n")


def Monitor_Beams(ToteList):
    print("\n\tReady\t{}".format(FM.Timestamp()))
    opHandle = True
    while opHandle == True:
        PiCam.CameraLEDon()
        if PiCam.readCameraSwitch() == True:
            opHandle = False
            PiCam.CameraLEDoff()
            PiCam.CaptureAndSave(FM)
            Guess = Model.Analyze(ImageFile=FM.lastFile[0])
            print("\t[$] Model Result: [{}]".format(Guess))
            UserResult = Monitor_Switches(ToteList, Guess)
            print("\t\tUserResult: {}".format(UserResult))
            if UserResult == None: UserResult = 'NOID'
            Modify_Files(UserResult, Guess)
            Monitor_Beams(ToteList)
        for tote in ToteList:
            if tote.readBreakBeam() == True:
                opHandle = False
                PiCam.CameraLEDoff()
                print("Broken Beam: {}".format(tote.Number))
                Tally.addByNumber(tote.Number)
                LEDs.activatePins(tote.LEDlist, CycleTime=1)
                Monitor_Beams(ToteList)
                sleep(0.01)


@timeout_decorator.timeout(TimeOutTime, timeout_exception=StopIteration)
def Monitor_Switches(ToteList, Guess=None):
    print("[STARTING TIMER: {} seconds]".format(TimeOutTime))
    try:
        while True:
            if Guess is not None:
                LEDs.activatePins(LEDs.BinaryList(Guess), CycleTime=0.05)
                # print("Activating #{}".format(Guess))
            for tote in ToteList:
                if Guess is None:
                    # LEDs.activatePins(LEDlist=tote.LEDlist, CycleTime=0.05)
                    LEDs.Strobe()
                    # print("Activating #{}".format(tote.Number))
                if tote.readSwitch() == True:
                    print("\tSWITCH #{} pushed".format(tote.Number))
                    LEDs.activatePins(tote.LEDlist, CycleTime=1)
                    return tote.Number
                    raise ValueError('Pass SWITCH no. to File Manager')
                else:
                    pass
                sleep(0.01)
    except StopIteration:
        print("\t[TIMEOUT]")
    except ValueError:
        pass


def Modify_Files(UserResult, Guess):
    print("Target Directory: {}".format(UserResult))
    print("\tLast File: {}".format(FM.lastFile[1]))
    if UserResult == 'NOID': UserResult = 0
    if Guess is None: Guess = 0
    URLaddress = MyURL.process_url(filename=FM.lastFile[1], modelresult=Guess, confidence=UserResult)
    print("URL: {}".format(URLaddress))
    StatusCode = MyURL.VisitURL(URLaddress)
    if StatusCode == 200: StatusSymbol = "✅"
    elif StatusCode == 400: StatusSymbol = "❌"
    else: StatusSymbol = "❔"
    print("\t\t[STATUS: {}] {}".format(StatusCode, StatusSymbol))
    FM.RelocateImage(UserResult)



""" MAIN FUNCTION """
# # # # # # # # # # # # # # # # # # # #

print("Started: {}".format(FM.Timestamp()))
# VerboseVerbose(ToteList)
try:
    Monitor_Beams(ToteList)
except:
    Tally.Verbose()
    print("\nEnding processes...")
    print("Ended: {}".format(FM.Timestamp()))
    PiCam.CameraLEDoff()
    pass

# # # # # # # # # # # # # # # # # # # #

print("\nEOF")

#
