'''
Created on 2020/11/29

@author: ukai
'''
import unittest
from sac.sac_factory_for_test import SacFactoryForTest
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from sac.sac_batch_data_agent import SacBatchDataAgent
from sac.sac_batch_data_reward import SacBatchDataReward


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = SacFactoryForTest()


    def test001(self):
        simulator = self.factory.createSimulator()
        
        simulator.reset()
        
        for _ in range(10):
            batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep = simulator.step()
            
            assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
            assert isinstance(batchDataAgent, SacBatchDataAgent)
            assert isinstance(batchDataReward, SacBatchDataReward)
            assert isinstance(batchDataEnvironmentNextStep, SacBatchDataEnvironment)

    def test002(self):
        simulator = self.factory.createSimulator()
        
        simulator.reset()

        for batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep in simulator.getSimulationResultGenerator(10):

            assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
            assert isinstance(batchDataAgent, SacBatchDataAgent)
            assert isinstance(batchDataReward, SacBatchDataReward)
            assert isinstance(batchDataEnvironmentNextStep, SacBatchDataEnvironment)
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()