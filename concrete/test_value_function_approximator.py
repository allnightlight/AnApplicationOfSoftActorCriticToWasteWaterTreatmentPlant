'''
Created on 2020/11/17

@author: ukai
'''
import unittest

from concrete.concrete_factory_for_test import ConcreteFactoryForTest
from concrete.concrete_value_function_approximator import ConcreteValueFunctionApproximator
from concrete.concrete_batch_data_value import ConcreteBatchDataValue


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = ConcreteFactoryForTest()
        
        assert isinstance(self.factory, ConcreteFactoryForTest)

    def test001(self):
        
        valueFunctionApproximator = self.factory.createValueFunctionApproximator()
        
        assert isinstance(valueFunctionApproximator, ConcreteValueFunctionApproximator)
        
        batchDataValue = valueFunctionApproximator.getActionValue(batchDataFeature = self.factory.createBatchDataFeature()
                                       , batchDataAgent = self.factory.createBatchDataAgent())
        
        assert isinstance(batchDataValue, ConcreteBatchDataValue)
        assert batchDataValue.getValue().shape == (self.factory.nBatch, 1)

        batchDataValue = valueFunctionApproximator.getStateValue(batchDataFeature = self.factory.createBatchDataFeature())
        
        assert isinstance(batchDataValue, ConcreteBatchDataValue)
        assert batchDataValue.getValue().shape == (self.factory.nBatch, 1)

        batchDataValue = valueFunctionApproximator.getAveragedActionValue(batchDataFeature = self.factory.createBatchDataFeature()
                                       , batchDataAgent = self.factory.createBatchDataAgent())
        
        assert isinstance(batchDataValue, ConcreteBatchDataValue)
        assert batchDataValue.getValue().shape == (self.factory.nBatch, 1)

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()