'''
Created on 2020/11/15

@author: ukai
'''
import tensorflow

from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from skeleton.abstract_policy import AbstractPolicy


class ConcretePolicy(AbstractPolicy, tensorflow.keras.Model):
    '''
    classdocs
    '''


    def __init__(self, nMv):
        super().__init__()
        
        AbstractPolicy.__init__(self)
        
        self.nMv = nMv
        self.dense = tensorflow.keras.layers.Dense(nMv)
        
        
    def call(self, batchDataFeature):
        
        _Feature = batchDataFeature.getValue() # (..., nFeature)
        _Mv = self.dense(_Feature) # (..., nMv)
        
        return ConcreteBatchDataAgent(_Mv)
    