import urllib3.request as url
import urllib3

class CreateURL(object):
    """docstring for CreateURL."""

    def __init__(self, url_root, token, machine, Logging=True):
        self.url_root = url_root
        self.token = token
        self.machine = machine
        self.assn = '='
        self.delim = '-'
        self.Logging = Logging


    def setLogging(self, printLogs):
        if printLogs == True:
            self.Logging = True
        elif printLogs == False:
            self.Logging = False
        else:
            print("Error: argument must be True or False")


    def Verbose(self):
        print("\n___CreateURL___")
        print("[Logging: {}]".format(self.Logging))
        print("Token: {}".format(self.token))
        print("Machine: {}".format(self.machine))
        print("Assign: {}".format(self.assn))
        print("Delim: {}".format(self.delim))
        print("_____________\n")


    def process_url(self, filename, modelresult, confidence=0, computetime=0):
        action = 'process'
        if modelresult == "NOID": modelresult = 0
        params = {
        "token": str(self.token),
        "machine": str(self.machine),
        "action": str(action),
        "filename": str(filename),
        "modelresult": str(modelresult),
        "confidence": str(confidence),
        "computetime": str(computetime)
        }
        param_key = list(params.keys())
        param_values = list(params.values())
        url_list = []
        # if self.Logging == True: print(params)
        for i in range(len(param_key)):
            for j in range(0, 4):
                switch = j % 4
                if switch == 0:
                    url_list.append(param_key[i])
                elif switch == 1:
                    url_list.append(self.assn)
                elif switch == 2:
                    url_list.append(param_values[i])
                elif switch == 3:
                    url_list.append(self.delim)
                else:
                    print("Unable to create PROCESS url")
        url_string = ''.join(url_list)[0:-1]
        destination = self.url_root + url_string
        # if self.Logging == True: print("URL: {}".format(destination))
        return destination


    def state_url(self, t1lv, t1tl, t2lv, t2tl, t3lv, t3tl, t4lv, t4tl, t5lv, t5tl, t6lv, t6tl):
        action = 'state'
        params = {
        "token": str(self.token),
        "machine": str(self.machine),
        "action": str(action),
        "tote1level": str(t1lv),
        "tote1tally": str(t1tl),
        "tote2level": str(t2lv),
        "tote2tally": str(t2tl),
        "tote3level": str(t3lv),
        "tote3tally": str(t3tl),
        "tote4level": str(t4lv),
        "tote4tally": str(t4tl),
        "tote5level": str(t5lv),
        "tote5tally": str(t5tl),
        "tote6level": str(t6lv),
        "tote6tally": str(t6tl)
        }
        param_key = list(params.keys())
        param_values = list(params.values())
        url_list = []
        if self.Logging == True: print(params)
        for i in range(len(param_key)):
            for j in range(0, 4):
                switch = j % 4
                if switch == 0:
                    url_list.append(param_key[i])
                elif switch == 1:
                    url_list.append(self.assn)
                elif switch == 2:
                    url_list.append(param_values[i])
                elif switch == 3:
                    url_list.append(self.delim)
                else:
                    print("Unable to create STATE url")
        url_string = ''.join(url_list)[0:-1]
        destination = self.url_root + url_string
        # if self.Logging == True: print("URL: {}".format(destination))
        return destination


    def VisitURL(self, URLaddress):
        http = urllib3.PoolManager()
        try:
            r = http.urlopen('GET', URLaddress)
            return r.status
        except:
            return 404
