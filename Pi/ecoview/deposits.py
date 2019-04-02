import os
import ast
from datetime import datetime


class TallyWizard(object):
    """object-based handling of running tallies"""

    def __init__(self, Logging=True):
        self.Logging = Logging
        storedTallies, absolute_path = self.getTalliesFromFile()
        self.currentTallyDict = storedTallies
        self.absolute_path = absolute_path
        self.refreshFields()
        if self.Logging == True: self.Verbose()


    def refreshFields(self):
        self.Tote0 = self.currentTallyDict['Tote0']
        self.Tote1 = self.currentTallyDict['Tote1']
        self.Tote2 = self.currentTallyDict['Tote2']
        self.Tote3 = self.currentTallyDict['Tote3']
        self.Tote4 = self.currentTallyDict['Tote4']
        self.Tote5 = self.currentTallyDict['Tote5']
        self.Tote6 = self.currentTallyDict['Tote6']


    def Verbose(self):
        print("\n___Tally___")
        print("[Logging: {}]".format(self.Logging))
        print("Tote0: {}".format(self.Tote0))
        print("Tote1: {}".format(self.Tote1))
        print("Tote2: {}".format(self.Tote2))
        print("Tote3: {}".format(self.Tote3))
        print("Tote4: {}".format(self.Tote4))
        print("Tote5: {}".format(self.Tote5))
        print("Tote6: {}".format(self.Tote6))
        print("__________\n")


    def setLogging(self, printLogs):
        if printLogs == True:
            self.Logging = True
        elif printLogs == False:
            self.Logging = False
        else:
            print("Error: argument must be True or False")


    def addByNumber(self, toteNumber=None):
        if toteNumber is not None and toteNumber in range(0, 7):
            if self.Logging == True: print("Recording tally in Tote #{}".format(toteNumber))
            if toteNumber == 0:
                self.currentTallyDict['Tote0'] += 1
            elif toteNumber == 1:
                self.currentTallyDict['Tote1'] += 1
            elif toteNumber == 2:
                self.currentTallyDict['Tote2'] += 1
            elif toteNumber == 3:
                self.currentTallyDict['Tote3'] += 1
            elif toteNumber == 4:
                self.currentTallyDict['Tote4'] += 1
            elif toteNumber == 5:
                self.currentTallyDict['Tote5'] += 1
            elif toteNumber == 6:
                self.currentTallyDict['Tote6'] += 1
            else:
                if self.Logging == True: print("Rare Error")
                pass
            self.refreshFields()
            self.saveTalliesToFile()
            if self.Logging == True: print("\t[Tally recorded]")
        else:
            if self.Logging == True: print("\tInvalid argument")


    def getTalliesFromFile(self):
        if self.Logging == True: print("\nGetting tallies...")
        current_folder = os.path.dirname(os.path.abspath(__file__))
        absolute_path = os.path.join(current_folder,'RunningTally.txt')
        exists = os.path.isfile(absolute_path)
        if self.Logging == True: print("\tCurrentFolder: {}".format(current_folder))
        if self.Logging == True: print("\tAbsolutePath: {}".format(absolute_path))
        storedTalliesINIT = {"Tote0": 0, "Tote1": 0, "Tote2": 0, "Tote3": 0,\
            "Tote4": 0, "Tote5": 0, "Tote6": 0}
        tallyKeyList = storedTalliesINIT.keys()
        if exists:
            if self.Logging == True: print("\t\t[File exists]")
            try:
                with open(absolute_path, 'rt') as storedTallies:
                    storedTallies = storedTallies.read() # Read the text file
                # if self.Logging == True: print("Text data: {}".format(storedTallies))
                if self.Logging == True: print("Checking format...")
                try:
                    fileDict = ast.literal_eval(storedTallies)
                    # if self.Logging == True: print("File Keys: {}".format(fileDict.keys()))
                    # if self.Logging == True: print("Good Keys: {}".format(tallyKeyList))
                    if fileDict.keys() == tallyKeyList:
                        if self.Logging == True: print("\t[File keys are valid]")
                        pass
                except:
                    if self.Logging == True: print("Invalid keys")
                    if self.Logging == True: print("Writing clean file...")
                    myfile = open(absolute_path, 'w')
                    myfile.write(str(storedTalliesINIT))
                    myfile.close()
                    if self.Logging == True: print("File written")
            except:
                if self.Logging == True: print("Oops! The file is unreadable")
                if self.Logging == True: stringTag = datetime.date(datetime.now())
                if self.Logging == True: print("ERROR: {}".format(stringTag))
                if self.Logging == True: print("Writing clean file...")
                myfile = open(absolute_path, 'w')
                myfile.write(str(storedTalliesINIT))
                myfile.close()
                if self.Logging == True: print("File written")
        else:
            if self.Logging == True: print("We have to create a new file")
            with open(absolute_path, 'wt') as storedTallies:
                storedTallies.write(str(storedTalliesINIT)) # Write the text file
            if self.Logging == True: print("File created!")
        try:
            myfile = open(absolute_path, 'r')
            storedTallies = myfile.read()
            myfile.close()
            storedTallies = ast.literal_eval(storedTallies)
        except:
            if self.Logging == True: print("Rare error: re-run program")
            pass
        if self.Logging == True: print("\t\t[Loaded Current Tallies]")
        return storedTallies, absolute_path


    def saveTalliesToFile(self):
        with open(self.absolute_path, 'wt') as storedTallies:
            storedTallies.write(str(self.currentTallyDict)) # Write the text file


    def ResetReset(self):
        with open(self.absolute_path, 'wt') as storedTallies:
            storedTallies.write('') # Write empty file
        self.__init__()  # Reset class fields




#########################
# print("Hello")
# Tally = TallyWizard(Logging=False)
# # Tally.setLogging(False)
# Tally.addByNumber(4)
# Tally.Verbose()
# print("world!")
# Tally.ResetReset()
# Tally.Verbose()


"""
break beam monitored
    if broken, return ToteNumber
    record tally result

if object is detected in camera
    capture image
    model image
    return Result
    timeout(*)
    light best guess, wait for button press
        if timeout(*wait) expires, kill, return to monitor mode
        if UserButton==BestGuess
            kill timer, timeout(*ring), glow ring






"""













#
