'''
Created on 2020/11/11

@author: ukai
'''
from skeleton.abstract_batch_data_reward import AbstractBatchDataReward
from skeleton.abstract_batch_data_environment import AbstractBatchDataEnvironment

class AbstractEnvironment(object):
    '''
    classdocs
    '''


    def update(self, batchDataAgent):
        return AbstractBatchDataReward() # as BatchDataReward
    
    def observe(self):
        return AbstractBatchDataEnvironment() # as BatchDataEnvironment