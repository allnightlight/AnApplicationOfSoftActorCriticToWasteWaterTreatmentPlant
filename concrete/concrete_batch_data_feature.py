'''
Created on 2020/11/15

@author: ukai
'''
from skeleton.abstract_batch_data_feature import AbstractBatchDataFeature

class ConcreteBatchDataFeature(AbstractBatchDataFeature):
    '''
    classdocs
    '''


    def __init__(self, _Feature):
        AbstractBatchDataFeature.__init__(self)        
        self._Feature = _Feature
        
        
    def getValue(self):
        return self._Feature