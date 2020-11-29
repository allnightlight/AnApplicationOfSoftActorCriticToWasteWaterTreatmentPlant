'''
Created on 2020/11/29

@author: ukai
'''
import unittest
from concrete.concrete_factory_for_test import ConcreteFactoryForTest
from concrete.concrete_application import ConcreteApplication
from sac.sac_evaluator import SacEvaluator


class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        
        cls.factory = ConcreteFactoryForTest()
        cls.app, cls.store = cls.factory.createApplication(console_print=True)
        
    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        
        cls.store.removeHistory()

    def test001(self):
        
        assert isinstance(self.app, ConcreteApplication)
        
        for buildParameter in self.factory.generateBuildParameter():
            self.app.runBuild(buildParameter)
        
        for row, agent, buildParameter, epoch, environment, trainer in self.app.runEvaluationWithSimulation(evaluators = [SacEvaluator(),], nSimulationStep = 10):
            assert isinstance(row, dict)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()