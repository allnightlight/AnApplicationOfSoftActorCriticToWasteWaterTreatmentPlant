'''
Created on 2020/12/02

@author: ukai
'''
import unittest
from concrete.concrete_factory_for_test import ConcreteFactoryForTest
from concrete.concrete_evaluator_suite import ConcreteEvaluatorSuite
from sac.sac_evaluator import SacEvaluator


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = ConcreteFactoryForTest(nMv=1, nPv=1)


    def test001(self):
        
        evaluatorSuite = self.factory.createConcreteEvaluatorSuite()
        
        assert isinstance(evaluatorSuite, ConcreteEvaluatorSuite)
        
        for evaluator, stats in evaluatorSuite.evaluate(agent = self.factory.createAgent()
                                , environment = self.factory.createEnvironmentPoweredByPlant001()
                                , nSimulationStep = 2**7):

            assert isinstance(stats, dict)
            assert isinstance(evaluator, SacEvaluator)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()