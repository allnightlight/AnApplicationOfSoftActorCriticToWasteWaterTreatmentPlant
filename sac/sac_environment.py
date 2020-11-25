'''
Created on 2020/11/11

@author: ukai
'''
from sac.sac_batch_data_reward import SacBatchDataReward
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from sac.sac_plant import SacPlant

class SacEnvironment(object):
    '''
    classdocs
    '''
    
    
    def __init__(self, plant):
        
        assert isinstance(plant, SacPlant)
        self.plant = plant
        self.bufferPv = None
        self.bufferMv = None


    def reset(self):

        self.plant.reset()
        
        self.bufferPv = [self.plant.getPv(),]
        self.bufferMv = []        

    def update(self, batchDataAgent):
        
        mv = batchDataAgent.getSampledActionOnEnvironment()
        r = self.plant.update(mv)
        pvNext = self.plant.getPv()
        self.bufferMv.append(mv)
        self.bufferPv.append(pvNext) 
        return SacBatchDataReward(r) # as BatchDataReward
    
    def observe(self):
        return SacBatchDataEnvironment(self.bufferPv, self.bufferMv) # as BatchDataEnvironment
    
    # <<public, final>>
    def getNmv(self):
        return self.plant.getNmv()
    
    # <<public, final>>
    def getNpv(self):
        return self.plant.getNpv()