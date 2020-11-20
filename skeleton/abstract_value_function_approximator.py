'''
Created on 2020/11/10

@author: ukai
'''
from skeleton.abstract_batch_data_feature import AbstractBatchDataFeature
from skeleton.abstract_batch_data_value import AbstractBatchDataValue
from skeleton.abstract_batch_data_agent import AbstractBatchDataAgent


class AbstractValueFunctionApproximator(object):
    '''
    classdocs
    '''

        
    def call(self, batchDataFeature, batchDataAgent):
        
        assert isinstance(batchDataFeature, AbstractBatchDataFeature)
        assert batchDataAgent is None or isinstance(batchDataAgent, AbstractBatchDataAgent)
        
        return AbstractBatchDataValue()
    
    # <<abstract>>
    def getActionValue(self, batchDataEnvironment, batchDataAgent):
        return AbstractBatchDataValue()

    # <<abstract>>
    def getStateValue(self, batchDataEnvironment):
        return AbstractBatchDataValue()
    
    # <<abstract>>
    def getAveragedActionValue(self, batchDataEnvironment, batchDataAgent):
        return AbstractBatchDataValue()
