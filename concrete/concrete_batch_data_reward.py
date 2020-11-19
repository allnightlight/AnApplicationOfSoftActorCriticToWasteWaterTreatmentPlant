'''
Created on 2020/11/19

@author: ukai
'''
from skeleton.abstract_batch_data_reward import AbstractBatchDataReward

class ConcreteBatchDataReward(AbstractBatchDataReward):
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