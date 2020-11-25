'''
Created on 2020/11/19

@author: ukai
'''
from sac.sac_batch_data_reward import SacBatchDataReward

class ConcreteBatchDataReward(SacBatchDataReward):
    '''
    classdocs
    '''


    def __init__(self, reward):
        '''
        Constructor
        '''        
        self.reward = reward
        
    def getValue(self):
        return self.reward