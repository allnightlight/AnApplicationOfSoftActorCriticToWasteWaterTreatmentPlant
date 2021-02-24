'''
Created on 2020/11/15

@author: ukai
'''

import tensorflow

from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_policy import ConcretePolicy

        
class ConcretePolicy002(ConcretePolicy):
    '''
    classdocs
    '''


    def __init__(self, nMv, threshold = 1.5):
        ConcretePolicy.__init__(self, nMv)
        
        self.threshold = threshold
        self.feature2mean = tensorflow.keras.layers.Dense(units = nMv)
        self.feature2sd = tensorflow.keras.layers.Dense(units = nMv)
                        
    def call(self, batchDataFeature):
        
        _Feature = batchDataFeature.getFeature() # (..., nFeature)
        
        return ConcreteBatchDataAgent(
            _Mean = self.threshold * tensorflow.tanh(self.feature2mean(_Feature)) 
            , _LogSd = tensorflow.math.log(self.threshold) + tensorflow.math.log_sigmoid(self.feature2sd(_Feature))) 