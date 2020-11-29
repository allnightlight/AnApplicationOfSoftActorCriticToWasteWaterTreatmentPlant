'''
Created on 2020/11/29

@author: ukai
'''
import unittest
from sanitycheck.work004_utility import Work004Utility
from concrete.concrete_build_parameter import ConcreteBuildParameter


class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        
        cls.app, cls.store = Work004Utility.create()
        
    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        
        cls.store.removeHistory()

    def test001(self):
        
        nEpoch = 2**2
        buildParameter = ConcreteBuildParameter(nIntervalSave = nEpoch//2
                                                , nEpoch = nEpoch
                                                , label = "test"
                                                , plantClass = "ConcretePlant001"
                                                , discountFactor = 0.
                                                , alphaTemp = 1.
                                                , saveFolderPathAgent = "checkpoint"
                                                , nFeature = 1
                                                , nSampleOfActionsInValueFunctionApproximator = 2**3
                                                , nHiddenValueFunctionApproximator = 2**5
                                                , nStepEnvironment = 1
                                                , nStepGradient = 2**5
                                                , nIntervalUpdateStateValueFunction = 1
                                                , nIterationPerEpoch = 1
                                                , bufferSizeReplayBuffer = 2**10
                                                , featureExtractorClass = "ConcreteFeatureExtractor002")
        
        for _ in range(3):
            self.app.build(buildParameter)        
        
        self.app.evaluate()
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()