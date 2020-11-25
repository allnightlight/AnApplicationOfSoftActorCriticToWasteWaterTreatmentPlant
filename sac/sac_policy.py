'''
Created on 2020/11/10

@author: ukai
'''
from skeleton.abstract_batch_data_feature import AbstractBatchDataFeature
from skeleton.abstract_batch_data_agent import AbstractBatchDataAgent

class AbstractPolicy(object):
    '''
    classdocs
    '''

        
    def call(self, batchDataFeature):
        
        assert isinstance(batchDataFeature, AbstractBatchDataFeature)
        
        return AbstractBatchDataAgent()