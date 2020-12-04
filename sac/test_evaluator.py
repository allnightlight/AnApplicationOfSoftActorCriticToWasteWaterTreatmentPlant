'''
Created on 2020/11/29

@author: ukai
'''
import unittest

from sac.sac_factory_for_test import SacFactoryForTest
from sac.sac_evaluator import SacEvaluatorDummy
from sac.sac_evaluate_method import SacEvaluateMethod


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = SacFactoryForTest()

    def test001(self):
        
        evaluator = self.factory.createEvaluator()
        
        assert isinstance(evaluator, SacEvaluatorDummy)
        
        for evaluateMethod, stats in evaluator.evaluate(agent = self.factory.createAgent()
                           , environment = self.factory.createEnvironment()
                           , evaluateMethods = self.factory.createEvaluateMethods()):
            
            assert isinstance(evaluateMethod, SacEvaluateMethod)
            
            assert isinstance(stats, dict)
            assert stats["count"] == self.factory.nSimulationStep
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()