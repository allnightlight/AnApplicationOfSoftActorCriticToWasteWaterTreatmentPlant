'''
Created on 2020/11/29

@author: ukai
'''
import unittest
from sac.sac_factory_for_test import SacFactoryForTest
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from sac.sac_batch_data_agent import SacBatchDataAgent
from sac.sac_batch_data_reward import SacBatchDataReward
from sac.sac_simulator_abstract import SacSimulatorAbstract
from sac.sac_simulator_factory import SacSimulatorFactory


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = SacFactoryForTest()


    def test001(self):
        for simulator in self.factory.generateSimulator():
            
            assert isinstance(simulator, SacSimulatorAbstract)
        
            simulator.reset()
            
            for batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep in simulator.generateSeries():
                
                assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
                assert isinstance(batchDataAgent, SacBatchDataAgent)
                assert isinstance(batchDataReward, SacBatchDataReward)
                assert isinstance(batchDataEnvironmentNextStep, SacBatchDataEnvironment)
                                            
    def test002(self):
        
        simulatorFactory = self.factory.createSimulatorFactory()
        simulator = simulatorFactory.create(agent = self.factory.createAgent()
                                , environment = self.factory.createEnvironment())
        assert isinstance(simulator, SacSimulatorAbstract)
        
        simulator.reset()
        batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep = simulator.generateSeries().__next__()

        assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
        assert isinstance(batchDataAgent, SacBatchDataAgent)
        assert isinstance(batchDataReward, SacBatchDataReward)
        assert isinstance(batchDataEnvironmentNextStep, SacBatchDataEnvironment)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()