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
        
        self.utility = Work001Utility.create(nIter = 10)


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
        
        self.utility.trainV()
        
    def test005(self):
        
        self.utility.trainPi()

    def test006(self):
        
        self.utility.plotTrainedPi()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()