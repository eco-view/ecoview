import RPi.GPIO as GPIO
from time import sleep, time
from datetime import datetime
import os


class FileManager(object):
    """docstring for FileManager."""

    def __init__(self, sub_directories=['0', '1', '2', 'NOID'], Logging=True):
        self.Logging = Logging
        self.current_folder = os.path.dirname(os.path.abspath(__file__))
        self.image_folder_path = os.path.join(self.current_folder, 'images')
        self.sub_directories = sub_directories
        self.imgExtension = '.jpg'
        self.lastFile = None
        self.InitializeDirectories()


    def Verbose(self):
        print("\n___FILE MANAGER___")
        print("[Logging: {}]".format(self.Logging))
        print("Current Folder: {}".format(self.current_folder))
        print("IMAGE Path: {}".format(self.image_folder_path))
        print("Sub-Directories: {}".format(self.sub_directories))
        print("Extension: {}".format(self.imgExtension))
        print("Last File: {}".format(self.lastFile))
        print("__________________\n")


    def setLogging(self, printLogs):
        if printLogs == True:
            self.Logging = True
        elif printLogs == False:
            self.Logging = False
        else:
            print("Error: argument must be True or False")


    def InitializeDirectories(self):
        if self.Logging == True: print("Initializing directories...")
        if os.path.isdir(self.image_folder_path) == False:
            print("Need to create Image folder")
            try:
                os.mkdir(self.image_folder_path)
            except OSError:
                if self.Logging == True: print("\tUnable to create IMAGES folder")
            else:
                if self.Logging == True: print("\tSuccessfully created IMAGES folder")
        else:
            if self.Logging == True: print("IMAGE folder already exists")
        if os.path.isdir(self.image_folder_path) == True:
            if self.Logging == True: print("IMAGE folder exists, now checking sub-directories")
            for folder in self.sub_directories:
                dir_name = os.path.join(self.image_folder_path, folder)
                if os.path.isdir(dir_name) == True:
                    if self.Logging == True: print("\t{} exists".format(dir_name))
                else:
                    if self.Logging == True: print("\t{} must be created".format(dir_name))
                    try:
                        os.mkdir(dir_name)
                    except OSError:
                        if self.Logging == True: print("\t\tUnable to create {}".format(dir_name))
                    else:
                        if self.Logging == True: print("\t\tSuccessfully created {}".format(dir_name))
        else:
            if self.Logging == True: print("\tUnable to verify IMAGE sub-directories")
        if self.Logging == True: print("\tInitialization complete")


    def GenerateTimestampFilename(self):
        currentTime = datetime.now()
        picTime = currentTime.strftime("%Y.%m.%d_%H%M%S")
        picName = picTime + self.imgExtension
        cachedPicName = self.JoinPaths(TargetDirectory='cache', TimestampFilename=picName)
        self.lastFile = [cachedPicName, picName]
        if self.Logging == True: print("picName: {}".format(picName))
        if self.Logging == True: print("cachedPicName: {}".format(cachedPicName))
        if self.Logging == True: print("Storing lastFile")
        return picName, cachedPicName


    def Timestamp(self):
        # SystemTimeStamp = datetime.now().strftime("%Y.%m.%d-%H%M%S")
        # print(SystemTimeStamp)
        return datetime.utcfromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')


    def JoinPaths(self, TargetDirectory, TimestampFilename):
        if TargetDirectory is None:
            TargetDirectory = 'NOID'
            print("TargetDirectory changed to: {}".format(TargetDirectory))
        if str(TargetDirectory) in self.sub_directories:
            if self.Logging == True: print("Target Directory is valid")
            CompletePath = os.path.join(self.image_folder_path, str(TargetDirectory), TimestampFilename)
            if self.Logging == True: print("Complete Path: {}".format(CompletePath))
            return CompletePath
        else:
            if self.Logging == True: print("Invalid Target Directory: {}".format(TargetDirectory))
            return None


    def RelocateImage(self, Category):
        if self.lastFile is not None:
            try:
                os.rename(self.lastFile[0], self.JoinPaths(TargetDirectory=str(Category), TimestampFilename=self.lastFile[1]))
                if self.Logging == True: print("Successfully relocated file to .../images/{}".format(Category))
                self.lastFile = None
            except:
                if self.Logging == True: print("Unable to relocate file")
        else:
            if self.Logging == True: print("No user data for lastFile")
            try:
                os.rename(self.lastFile[0], self.JoinPaths(TargetDirectory='NOID', TimestampFilename=self.lastFile[1]))
                if self.Logging == True: print("Successfully relocated file to NOID")
                self.lastFile = None
            except:
                if self.Logging == True: print("Unable to relocate file")
        # if self.Logging == True: print("Finished Relocating Image")



# FM = FileManager(sub_directories=['0', '1', '2', 'NOID', 'cache'])
# FM.Verbose()
# picName, cachedPicName = FM.GenerateTimestampFilename()
# # ...once image is captured, the following function will work
# # FM.RelocateImage(0)
