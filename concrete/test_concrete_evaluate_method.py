'''
Created on 2020/12/05

@author: ukai
'''
import unittest
from concrete.concrete_factory_for_test import ConcreteFactoryForTest
from sac.sac_evaluate_method import SacEvaluateMethod


class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        
        cls.factory = ConcreteFactoryForTest(nBatch=1)
        
    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        
        cls.factory.clean()


    def test001(self):
        
        assert isinstance(self.factory, ConcreteFactoryForTest)
        
        g = [(self.factory.createBatchDataEnvironment()
            , self.factory.createBatchDataAgent()
            , self.factory.createBatchDataReward()
            , self.factory.createBatchDataEnvironment())            
              for _ in range(2**7)]
        
        for evaluateMethod in self.factory.createEvaluateMethods():
            assert isinstance(evaluateMethod, SacEvaluateMethod)
            
            evaluateMethod.evaluate(g)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()