'''
Created on 2020/11/29

@author: ukai
'''
import unittest
from concrete.concrete_factory_for_test import ConcreteFactoryForTest
from concrete.concrete_application import ConcreteApplication


class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        
        cls.factory = ConcreteFactoryForTest()
        cls.app, cls.store, cls.evaluationDb = cls.factory.createApplication(console_print=False)
        
    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        
        cls.store.removeHistory()
        cls.evaluationDb.removeRemainedFiles()

    def test001(self):
        
        assert isinstance(self.app, ConcreteApplication)
        
        for buildParameter in self.factory.generateBuildParameter():
            self.app.runBuild(buildParameter)
            
        assert self.app.runEvaluationWithSimulation(nSimulationStep = 10) > 0
        
        assert self.app.runEvaluationWithSimulation(nSimulationStep = 10) == 0

        assert len(self.app.exportEvaluationTable()) > 0


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()