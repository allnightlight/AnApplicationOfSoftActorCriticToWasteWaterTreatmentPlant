'''
Created on 2020/07/09

@author: ukai
'''
import json

from framework.util import Utils


class BuildParameter(object):
    '''
    classdocs
    '''

    def __init__(self, nIntervalSave=2**4, nEpoch = 2**8, label = "None"):
        '''
        Constructor
        '''
        
        self.key = Utils.generateRandomString(16)
        self.nIntervalSave = nIntervalSave
        self.nEpoch = nEpoch
        self.label = label
        
    def createMemento(self):
        return json.dumps(self.__dict__)
    
    def loadMemento(self, buildParameterMemento):
        d = json.loads(buildParameterMemento)
        
        for key in self.__dict__:
            if not key in d:
                print("Loaded build parameter does not have \"{key}\", that's why the property is set to the default value \"{value}\"".format(key=key, value=self.__dict__[key]))

        for key in d:
            if not key in self.__dict__:
                print("The current class does not have the property \"{key}\", that's why the value \"{value}\" was dismissed.".format(key=key, value=d[key]))
        
        for key in d:
            self.__dict__[key] = d[key]