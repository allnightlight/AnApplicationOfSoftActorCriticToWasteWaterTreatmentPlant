'''
Created on 2020/11/16

@author: ukai
'''
import unittest
from concrete.concrete_factory_for_test import ConcreteFactoryForTest
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = ConcreteFactoryForTest()


    def test001(self):
        
        policy = self.factory.createPolicy()
        
        batchDataAgent = policy.call(self.factory.createBatchDataFeature())
        
        assert isinstance(batchDataAgent, ConcreteBatchDataAgent)
        
        assert batchDataAgent.getSampledAction().shape == (self.factory.nBatch, self.factory.nMv)
        assert batchDataAgent.getEntropy().shape == (self.factory.nBatch, 1)
        assert batchDataAgent.generateSamples(1).__next__().shape == (self.factory.nBatch, self.factory.nMv)
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()