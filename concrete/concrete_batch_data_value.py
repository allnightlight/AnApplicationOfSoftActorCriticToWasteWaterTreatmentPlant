'''
Created on 2020/11/16

@author: ukai
'''
from sac.sac_batch_data_value import SacBatchDataValue
import tensorflow

class ConcreteBatchDataValue(SacBatchDataValue):
    '''
    classdocs
    '''


    def __init__(self, _Value):
        self._Value = _Value # (..., nRedundancy)
        
    def getValue(self):
        return tensorflow.reduce_min(self._Value, axis=-1, keepdims=True) # (..., 1)
    
    def getValueWithRedundancy(self):
        return self._Value # (..., nRedundancy)        