'''
Created on 2020/07/09

@author: ukai
'''
from framework.util import Utils


class Agent(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        self.agentKey = Utils.generateRandomString(16)
    
    def createMemento(self):
        agentMemento = Utils.generateRandomString(16)        
        return agentMemento
    
    def loadMemento(self, agentMemento, agentKey):
        self.agentKey = agentKey
        pass
        
    def getAgentKey(self):
        return self.agentKey