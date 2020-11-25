'''
Created on 2020/11/15

@author: ukai
'''
from sac.sac_batch_data_feature import SacBatchDataFeature

class ConcreteBatchDataFeature(SacBatchDataFeature):
    '''
    classdocs
    '''


    def __init__(self, _Feature):
        SacBatchDataFeature.__init__(self)        
        self._Feature = _Feature
        
        
    def getFeature(self):
        return self._Feature