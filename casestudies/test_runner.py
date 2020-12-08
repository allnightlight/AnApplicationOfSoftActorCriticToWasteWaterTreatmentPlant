'''
Created on 2020/12/07

@author: ukai
'''
import unittest
from casestudies.runner import Runner
from casestudies.work_factory import WorkFactory
from datetime import timedelta


class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        
        cls.runners = []

        work = WorkFactory().create(workName = "work001"
                                    , nSimulationStep = 2**3
                                    , nEpoch = 2**1
                                    , nAgent = 3
                                    , saveFolderPathAgent = "checkpoint"
                                    , updateEvaluationInterval = timedelta(seconds = 1)
                                    , nUpdateEvaluation = 2
                                    , showProgress = False)

        cls.runners.append(Runner(work))

        work = WorkFactory().create(workName = "work002"
                                    , nSimulationStep = 2**3
                                    , nEpoch = 2**3
                                    , nAgent = 1
                                    , saveFolderPathAgent = "checkpoint"
                                    , updateEvaluationInterval = timedelta(seconds = 1)
                                    , nUpdateEvaluation = 1
                                    , nSampleOverLearningCurve = 2
                                    , showProgress = False)

        cls.runners.append(Runner(work))
        
        
    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        
        for runner in cls.runners:
            runner.command(99)
            
    def test001(self):

        for runner in self.runners:        
            runner.command(0)

    def test002(self):

        for runner in self.runners:        
            runner.command(1)
        
    def test003(self):
        
        for runner in self.runners:
            runner.command(2, None, None)
    
    def test004(self):
        
        for runner in self.runners:
            runner.command(3, None, None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()