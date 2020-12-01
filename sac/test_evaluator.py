'''
Created on 2020/11/29

@author: ukai
'''
import unittest

from sac.sac_factory_for_test import SacFactoryForTest


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = SacFactoryForTest()

    def test001(self):
        
        evaluator = self.factory.createEvaluator()
        simulator = self.factory.createSimulator()
        
        n = 10
        
        simulator.reset()
        
        g = iter([simulator.stepWithDeterministicAction() for _ in range(n) ])
        
        res = evaluator.evaluate(g)
        
        assert isinstance(res, dict)
        assert res["count"] == n
        
        simulator.reset()
        
        g = iter([simulator.stepWithStochasticAction() for _ in range(n) ])
        
        res = evaluator.evaluate(g)
        
        assert isinstance(res, dict)
        assert res["count"] == n
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()