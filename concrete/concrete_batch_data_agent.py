'''
Created on 2020/11/15

@author: ukai
'''
from skeleton.abstract_batch_data_agent import AbstractBatchDataAgent
import tensorflow

class ConcreteBatchDataAgent(AbstractBatchDataAgent):
    '''
    classdocs
    '''


    def __init__(self, _Mean, _LogSd):
        AbstractBatchDataAgent.__init__(self)
        self._Mean = _Mean # (..., nMv)
        self._LogSd = _LogSd # (..., nMv)
        
        self.sampledAction = self.getSample() # (..., nMv)

    def getSample(self):
        return self._Mean + tensorflow.random.normal(shape=self._LogSd.shape) * tensorflow.exp(self._LogSd) # (..., nMv)
        
    def getEntropy(self):
        return tensorflow.reduce_sum(self._LogSd, axis=-1, keepdims=True) # (..., 1) 
    
    def generateSamples(self, nSample):
        for _ in range(nSample):
            yield self.getSample() # (..., nMv)