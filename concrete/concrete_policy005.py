'''
Created on 2020/11/15

@author: ukai
'''

import tensorflow

from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_policy import ConcretePolicy


class ConcretePolicy005(ConcretePolicy):
    '''
    classdocs
    '''


    def __init__(self, nFeature, nMv, nHidden):
        ConcretePolicy.__init__(self, nMv)
        
        self.feature2mean = tensorflow.keras.Sequential((
            tensorflow.keras.Input(shape = (nFeature,))
            , tensorflow.keras.layers.Dense(nHidden, activation="relu")
            , tensorflow.keras.layers.Dense(nMv)))
 
        self.feature2logSd = tensorflow.keras.Sequential((
            tensorflow.keras.Input(shape = (nFeature,))
            , tensorflow.keras.layers.Dense(nHidden, activation="relu")
            , tensorflow.keras.layers.Dense(nMv)))
                        
    def call(self, batchDataFeature):
        
        _Feature = batchDataFeature.getFeature() # (..., nFeature)
        
        return ConcreteBatchDataAgent(
            _Mean = self.feature2mean(_Feature)
            , _LogSd = self.feature2logSd(_Feature))