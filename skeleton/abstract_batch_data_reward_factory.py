'''
Created on 2020/11/10

@author: ukai
'''
from skeleton.abstract_batch_data_reward import AbstractBatchDataReward

class AbstractBatchDataRewardFactory(object):
    '''
    classdocs
    '''


    def create(self, context):
        
        return AbstractBatchDataReward()