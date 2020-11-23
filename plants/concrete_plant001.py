'''
Created on 2020/11/23

@author: ukai
'''
from skeleton.abstract_plant import AbstractPlant

class ConcretePlant001(AbstractPlant):
    '''
    classdocs
    '''
    
    def __init__(self):
        super(ConcretePlant001, self).__init__()
        
        self.sv = None
        self.x = None

    def getPv(self):
        return self.x
    
    def reset(self):
        self.sv = 1.
        self.x = 0.
        
    def update(self, u):
        
        self.x = u 
        reward = -(self.sv - self.x).__abs__()
        
        return reward