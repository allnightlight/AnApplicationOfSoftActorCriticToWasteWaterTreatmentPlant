'''
Created on 2020/11/10

@author: ukai
'''

class AbstractBatchDataAgent(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        self.sampledAction = None

    # <<abstract>>
    def getSampledAction(self):
        return self.sampledAction
    
    # <<abstract>>
    def getEntropy(self):
        return 1.