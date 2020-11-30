'''
Created on 2020/11/23

@author: ukai
'''
import numpy as np
from sac.sac_plant import SacPlant
from concrete.concrete_batch_data_reward import ConcreteBatchDataReward

class ConcretePlant001(SacPlant):
    '''
    classdocs
    '''
    
    def __init__(self, threshold = 2.):
        super(ConcretePlant001, self).__init__()
        
        self.sv = None
        self.x = None
        self.threshold = threshold

    def getPv(self):
        return np.array(self.x).reshape(1,-1).astype(np.float32)
    
    def reset(self):
        self.sv = 1.
        self.x = 0.
        
    def update(self, u):
        
        u = u.copy()
        
        u[u > self.threshold ] = self.threshold
        u[u < -self.threshold] = -self.threshold
        
        self.x = u 
        reward = -(self.sv - self.x).__abs__()
        
        return ConcreteBatchDataReward(reward = np.array(reward).reshape(1,-1).astype(np.float32))
    
    def getNmv(self):
        return 1
    
    def getNpv(self):
        return 1