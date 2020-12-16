'''
Created on 2020/11/10

@author: ukai
'''
from sac.sac_batch_data_feature import SacBatchDataFeature
from sac.sac_batch_data_agent import SacBatchDataAgent

class SacPolicy(object):
    '''
    classdocs
    '''

        
    def call(self, batchDataFeature):
        
        assert isinstance(batchDataFeature, SacBatchDataFeature)
        
        return SacBatchDataAgent()
    
    # <<protected, abstract>>    
    def getTrainableVariables(self):
        return None