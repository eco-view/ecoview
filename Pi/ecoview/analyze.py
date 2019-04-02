from random import randint
from time import sleep, time

"""
generate random result between 0 and 1
return result
allow user to correct
    as "confidence"
change TargetDirectory to UserEntry
"""

class myModel(object):
    """docstring for Model."""

    def __init__(self, modelfile=None):
        self.modelfile = modelfile
        self.computetime = None

    def TestFunc(self, Integer=None):
        if Integer is None:
            return None
        else:
            return randint(0,Integer)

    def Analyze(self, ImageFile):
        print("IMAGE FOR MODEL: {}".format(ImageFile))
        return self.TestFunc(6)


"""
StartTime = time()


End_Time = time()
Duration = round(End_Time - StartTime, 2)
print("\n\nDuration: {} sec".format(Duration))
"""





















#
