'''
Created on 2020/11/23

@author: ukai
'''
import numpy as np
from sac.sac_plant import SacPlant

class ConcretePlant002(SacPlant):
    '''
    classdocs
    '''
    
    def __init__(self, threshold = 2., tau = 10.):
        super(ConcretePlant002, self).__init__()
        
        self.sv = None
        self.x = None
        self.threshold = threshold
        self.tau = tau

    def getPv(self):
        return np.array(self.x).reshape(1,-1).astype(np.float32)
    
    def reset(self):
        self.sv = 1.
        self.x = 0.
        
    def update(self, u):
        
        u = u.copy()
        
        u[u > self.threshold ] = self.threshold
        u[u < -self.threshold] = -self.threshold
        
        self.x = (1-1/self.tau) * self.x + 1/self.tau * u
        reward = -(self.sv - self.x).__abs__()
        
        return reward
    
    def getNmv(self):
        return 1
    
    def getNpv(self):
        return 1