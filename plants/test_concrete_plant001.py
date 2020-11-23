'''
Created on 2020/11/23

@author: ukai
'''
import unittest
from plants.factory_for_test import FactoryForTest
from skeleton.abstract_environment import AbstractEnvironment
from skeleton.abstract_batch_data_environment import AbstractBatchDataEnvironment
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from skeleton.abstract_batch_data_reward import AbstractBatchDataReward


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.factory = FactoryForTest()

    def test001(self):
        
        plant = self.factory.createPlant001()
        
        plant.reset()
        
        reward = plant.update(u = 1.0)
        assert reward is not None

        pv = plant.getPv()
        assert pv is not None
        
    def test002(self):
        
        environment = self.factory.createEnvironmentPoweredByPlant001()

        assert isinstance(environment, AbstractEnvironment)
        
        environment.reset()

        batchDataEnvironment = environment.observe()
        
        assert isinstance(batchDataEnvironment, AbstractBatchDataEnvironment)
        
        for batchDataAgent in self.factory.generateBatchDataAgentForPlant001():
            
            assert isinstance(batchDataAgent, ConcreteBatchDataAgent)
        
            batchDataReward = environment.update(batchDataAgent)
            
            assert isinstance(batchDataReward, AbstractBatchDataReward)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()