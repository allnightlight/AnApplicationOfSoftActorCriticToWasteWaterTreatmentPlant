'''
Created on 2020/11/16

@author: ukai
'''
import unittest

from concrete.factory_for_test import FactoryForTest
from concrete.concrete_batch_data_feature import ConcreteBatchDataFeature
from builtins import isinstance
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
import tensorflow


class Test(unittest.TestCase):
    
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = FactoryForTest()

    def test001(self):
        
        batchDataFeature = self.factory.createBatchDataFeature()
        
        assert isinstance(batchDataFeature, ConcreteBatchDataFeature)
                
        
    def test002(self):
        
        batchDataAgent = self.factory.createBatchDataAgent()
        
        assert isinstance(batchDataAgent, ConcreteBatchDataAgent)
        
        _SampledAction = batchDataAgent.getSampledAction() # (nBatch, nMv)
        
        assert isinstance(_SampledAction, tensorflow.Tensor)
        assert _SampledAction.shape == (self.factory.nBatch, self.factory.nMv)
        
        _Entropy = batchDataAgent.getEntropy() # (..., 1)
        
        assert isinstance(_Entropy, tensorflow.Tensor)
        assert _Entropy.shape == (self.factory.nBatch, 1)
        
        for _SampledAction in batchDataAgent.generateSamples(10):
            assert isinstance(_SampledAction, tensorflow.Tensor)
            assert _SampledAction.shape == (self.factory.nBatch, self.factory.nMv)
            
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()