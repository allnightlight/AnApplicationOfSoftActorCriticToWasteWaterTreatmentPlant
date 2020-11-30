'''
Created on 2020/11/14

@author: ukai
'''
from sac.sac_batch_data_reward import SacBatchDataReward

class SacPlant(object):
    '''
    classdocs
    '''

    # <<abstract>>
    def getPv(self):
        return None # as pv
    
    # <<abstract>>
    def update(self, u):
        return SacBatchDataReward(reward = 1.0) # reward
    
    # <<abstract>>
    def reset(self):
        pass
    
    # <<abstract>>
    def getNmv(self):
        return -1
    
        # <<abstract>>
    def getNpv(self):
        return -1