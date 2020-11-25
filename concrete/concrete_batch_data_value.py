'''
Created on 2020/11/16

@author: ukai
'''
from sac.sac_batch_data_value import SacBatchDataValue

class ConcreteBatchDataValue(SacBatchDataValue):
    '''
    classdocs
    '''


    def __init__(self, _Value):
        self._Value = _Value # (..., 1)
        
    def getValue(self):
        return self._Value # (..., 1)