'''
Created on 2020/11/16

@author: ukai
'''
import unittest

from concrete.factory_for_test import FactoryForTest
from concrete.concrete_batch_data_feature import ConcreteBatchDataFeature
from builtins import isinstance
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent


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
        
        _Mv = batchDataAgent.getValue()
        
        
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()