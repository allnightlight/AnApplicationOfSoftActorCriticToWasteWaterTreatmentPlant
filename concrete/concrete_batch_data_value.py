'''
Created on 2020/11/16

@author: ukai
'''
from skeleton.abstract_batch_data_value import AbstractBatchDataValue

class ConcreteBatchDataValue(AbstractBatchDataValue):
    '''
    classdocs
    '''


    def __init__(self, _Value):
        self._Value = _Value
        
        
    def getValue(self):
        return self._Value