'''
Created on 2020/11/16

@author: ukai
'''
import unittest
from concrete.factory_for_test import FactoryForTest
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = FactoryForTest()


    def test001(self):
        
        policy = self.factory.createPolicy()
        
        batchDataAgent = policy.call(self.factory.createBatchDataFeature())
        
        assert isinstance(batchDataAgent, ConcreteBatchDataAgent)
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()