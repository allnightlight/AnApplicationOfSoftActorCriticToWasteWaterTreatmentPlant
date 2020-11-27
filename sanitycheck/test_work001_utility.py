'''
Created on 2020/11/21

@author: ukai
'''
import unittest
from sanitycheck.work001_utility import Work001Utility
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_batch_data_environment import ConcreteBatchDataEnvironment
from concrete.concrete_batch_data_reward import ConcreteBatchDataReward


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.utility = Work001Utility.create(nIter = 10, alphaTemp = 0.5)


    def test001(self):
        
        for batchDataAgent, batchDataEnvironment, batchDataReward, batchDataEnvironmentNext in self.utility.generateData():
            
            assert isinstance(batchDataAgent, ConcreteBatchDataAgent)
            assert isinstance(batchDataEnvironment, ConcreteBatchDataEnvironment)
            assert isinstance(batchDataReward, ConcreteBatchDataReward) 
            assert isinstance(batchDataEnvironmentNext, ConcreteBatchDataEnvironment)

    def test002(self):
        
        self.utility.trainQ()
        
    def test003(self):
        
        self.utility.plotTrainedQ()
        
    def test004(self):
        
        self.utility.trainQandV()
        
    def test005(self):
        
        self.utility.trainQandVandPi()

    def test006(self):
        
        self.utility.plotTrainedPi()

    @unittest.skip("check the performance of update policy")
    def test007(self):
        
        def getLogSd():    
            batchDataAgent = self.utility.agent.getAction(batchDataEnvironment = self.utility.getFixedBatchDataEnvironment())
            assert isinstance(batchDataAgent, ConcreteBatchDataAgent)        
            return batchDataAgent._LogSd.numpy().squeeze()
        
        print(getLogSd())
        for _ in range(10):
            self.utility.trainOnlyPi()
            print(getLogSd())
    
    @unittest.skip("check the performance of update policy")
    def test008(self):
        
        def getLogSd():    
            batchDataAgent = self.utility.agent.getAction(batchDataEnvironment = self.utility.getFixedBatchDataEnvironment())
            assert isinstance(batchDataAgent, ConcreteBatchDataAgent)        
            return batchDataAgent._Mean.numpy().squeeze(), batchDataAgent._LogSd.numpy().squeeze()
        
        print(getLogSd())
        for _ in range(100):
            self.utility.trainQandVandPi()
            print(getLogSd())

            self.utility.plotTrainedQ()
            
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()