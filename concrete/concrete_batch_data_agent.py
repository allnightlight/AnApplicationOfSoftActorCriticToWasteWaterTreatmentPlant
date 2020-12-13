'''
Created on 2020/11/15

@author: ukai
'''
from sac.sac_batch_data_agent import SacBatchDataAgent
import tensorflow

class ConcreteBatchDataAgent(SacBatchDataAgent):
    '''
    classdocs
    '''


    def __init__(self, _Mean, _LogSd, sampledAction = None):
        SacBatchDataAgent.__init__(self)
        self._Mean = _Mean # (..., nMv)
        self._LogSd = _LogSd # (..., nMv)
        
        if sampledAction is None:
            self.sampledAction = self.getSample() # (..., nMv)
        else:
            self.sampledAction = sampledAction # (..., nMv)
        
    def getSampledActionOnEnvironment(self):
        """
        Output is returned as <<numpy.ndarray>> 
        since it's used for updating plant objects, which is out of tensorflow's graphs.
        """        
        
        return self.sampledAction.numpy() # (..., nMv)

    def getSampledAction(self):
        """
        This function returns sampled action as an instance of <<tensorflow.Tensor>>
        since it can be used in a tensorflow's graph.
        """
        
        return self.sampledAction  # (..., nMv)

    def getSample(self):
        return self._Mean + tensorflow.random.normal(shape=self._LogSd.shape) * tensorflow.exp(self._LogSd) # (..., nMv)
        
    def getEntropy(self):
        return tensorflow.reduce_sum(self._LogSd, axis=-1, keepdims=True) # (..., 1) 
    
    def generateSamples(self, nSample):
        for _ in range(nSample):
            yield self.getSample() # (..., nMv)
            
    def getDeterministicAction(self):
        return self._Mean.numpy() # (..., nMv)