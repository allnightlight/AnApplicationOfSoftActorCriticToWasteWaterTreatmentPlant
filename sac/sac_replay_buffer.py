'''
Created on 2020/11/16

@author: ukai
'''

import numpy as np

class SacReplayBuffer(object):
    '''
    classdocs
    '''


    def __init__(self, bufferSize):
        '''
        Constructor
        '''
        
        self.buffer = None
        self.bufferSize = bufferSize
        
    def reset(self):
        
        self.buffer = []
        
        
    def append(self, batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep):
        self.buffer.append((batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep))
        if len(self.buffer) > self.bufferSize:
            del self.buffer[0]
            
    def getStateActionRewardAndNextState(self):
        
        i = int(np.random.randint(len(self.buffer)))
        
        return self.buffer[i]