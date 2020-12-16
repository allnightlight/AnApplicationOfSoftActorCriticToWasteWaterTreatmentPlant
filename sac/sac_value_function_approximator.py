'''
Created on 2020/11/10

@author: ukai
'''
from sac.sac_batch_data_feature import SacBatchDataFeature
from sac.sac_batch_data_value import SacBatchDataValue
from sac.sac_batch_data_agent import SacBatchDataAgent


class SacValueFunctionApproximator(object):
    '''
    classdocs
    '''

        
    def call(self, batchDataFeature, batchDataAgent):
        
        assert isinstance(batchDataFeature, SacBatchDataFeature)
        assert batchDataAgent is None or isinstance(batchDataAgent, SacBatchDataAgent)
        
        return SacBatchDataValue()
    
    # <<abstract>>
    def getActionValue(self, batchDataFeature, batchDataAgent):
        return SacBatchDataValue()

    # <<abstract>>
    def getStateValue(self, batchDataFeature):
        return SacBatchDataValue()
    
    # <<abstract>>
    def getAveragedActionValue(self, batchDataFeature, batchDataAgent):
        return SacBatchDataValue()

    # <<abstract>>
    def getTrainableVariablesOfStateValueFunction(self):
        return None
    
    # <<abstract>>
    def getTrainableVariablesOfActionValueFunction(self):
        return None