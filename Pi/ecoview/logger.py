from datetime import datetime
import os
from time import time
import sys
##########


class Logger(object):
    """docstring for Logger."""

    def __init__(self, GlobalLogging=False):
        self.GlobalLogging = GlobalLogging
        self.current_folder = os.path.dirname(os.path.abspath(__file__))
        self.log_folder_path = os.path.join(self.current_folder, 'logs')
        self.InitializeDirectory()
        self.Extension = '.txt'
        self.Current_Log = 'LOG_' + datetime.now().strftime("%Y.%m.%d_%H%M%S") + self.Extension
        self.AbsolutePath = ''
        if GlobalLogging == True:
            self.LogToLog()
        else:
            self.LogToConsole()


    def LogToLog(self):
        self.AbsolutePath = os.path.join(self.log_folder_path, self.Current_Log)
        print("LOG: {}".format(self.AbsolutePath))
        logfile = open(self.AbsolutePath, 'w')
        sys.stdout = logfile


    def LogToConsole(self):
        sys.stdout = sys.__stdout__


    def InitializeDirectory(self):
        print("Initializing directories...")
        if os.path.isdir(self.log_folder_path) == False:
            print("Need to create Log folder")
            try:
                os.mkdir(self.log_folder_path)
            except OSError:
                print("\tUnable to create LOGS folder")
            else:
                print("\tSuccessfully created LOGS folder")
        else:
            print("\tLOGS folder already exists")
        print("\t\tLog Initialization complete\n")
