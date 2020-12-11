'''
Created on 2020/11/15

@author: ukai
'''

import tensorflow

from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_policy import ConcretePolicy


class ConcretePolicy001(ConcretePolicy):
    '''
    classdocs
    '''


    def __init__(self, nMv):
        ConcretePolicy.__init__(self, nMv)
        
        self.feature2mean = tensorflow.keras.layers.Dense(units = nMv)
        self.feature2logSd = tensorflow.keras.layers.Dense(units = nMv)
                        
    def call(self, batchDataFeature):
        
        _Feature = batchDataFeature.getFeature() # (..., nFeature)
        
        return ConcreteBatchDataAgent(
            _Mean = self.feature2mean(_Feature)
            , _LogSd = self.feature2logSd(_Feature))