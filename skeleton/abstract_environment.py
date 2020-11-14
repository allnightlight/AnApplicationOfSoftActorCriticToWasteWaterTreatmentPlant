'''
Created on 2020/11/11

@author: ukai
'''
from skeleton.abstract_batch_data_reward import AbstractBatchDataReward
from skeleton.abstract_batch_data_environment import AbstractBatchDataEnvironment
from skeleton.abstract_plant import AbstractPlant

class AbstractEnvironment(object):
    '''
    classdocs
    '''
    
    
    def __init__(self, plant):
        
        assert isinstance(plant, AbstractPlant)
        self.plant = plant
        self.bufferPv = None
        self.bufferMv = None


    def reset(self):
        
        self.bufferPv = [self.plant.getPv(),]
        self.bufferMv = []

    def update(self, batchDataAgent):
        
        mv = batchDataAgent.getMv()
        r = self.plant.update(mv)
        pvNext = self.plant.getPv()
        self.bufferMv.append(mv)
        self.bufferPv.append(pvNext) 
        return AbstractBatchDataReward(r) # as BatchDataReward
    
    def observe(self):
        return AbstractBatchDataEnvironment(self.bufferPv, self.bufferMv) # as BatchDataEnvironment