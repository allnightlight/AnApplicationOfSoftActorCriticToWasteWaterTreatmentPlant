'''
Created on 2020/07/09

@author: ukai
'''

class StoreField(object):
    '''
    classdocs
    '''

    def __init__(self, agentMemento, epoch, buildParameterMemento, buildParameterKey, buildParameterLabel, agentKey):
        
        self.agentMemento = agentMemento
        self.epoch = epoch
        self.buildParameterMemento = buildParameterMemento
        self.buildParameterLabel = buildParameterLabel
        self.buildParameterKey = buildParameterKey
        self.agentKey = agentKey
