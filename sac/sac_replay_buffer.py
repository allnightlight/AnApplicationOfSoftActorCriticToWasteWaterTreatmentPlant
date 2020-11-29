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
            
    def generateStateActionRewardAndNextState(self, nStepGradient):
        
        if len(self.buffer) > 0:                    
            for i in np.random.permutation(len(self.buffer))[:min(len(self.buffer), nStepGradient, self.bufferSize)]:            
                yield self.buffer[i]