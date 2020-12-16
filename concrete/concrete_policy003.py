'''
Created on 2020/11/15

@author: ukai
'''

import tensorflow

from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_policy import ConcretePolicy

        
class ConcretePolicy003(ConcretePolicy):
    '''
    classdocs
    '''


    def __init__(self, nMv, threshold = 1.5):
        ConcretePolicy.__init__(self, nMv)
        
        self.threshold = threshold
        self.feature2mean = tensorflow.zeros(shape = (1, nMv))
        self.feature2sd = tensorflow.ones(shape = (1, nMv)) * threshold
                        
    def call(self, batchDataFeature):
        
        _Feature = batchDataFeature.getFeature() # (..., nFeature)
        
        return ConcreteBatchDataAgent(
            _Mean = self.feature2mean * tensorflow.ones(shape=(*_Feature.shape[:-1], 1)) 
            , _LogSd = tensorflow.math.log(self.feature2sd)* tensorflow.ones(shape=(*_Feature.shape[:-1], 1))) 