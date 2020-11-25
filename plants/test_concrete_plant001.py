'''
Created on 2020/11/23

@author: ukai
'''
import unittest
from plants.factory_for_test import FactoryForTest
from sac.sac_environment import SacEnvironment
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from sac.sac_batch_data_reward import SacBatchDataReward

import numpy as np

class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.factory = FactoryForTest()

    def test001(self):
        
        plant = self.factory.createPlant001()
        
        plant.reset()
        
        reward = plant.update(u = np.ones((1,1)))
        assert reward is not None

        pv = plant.getPv()
        assert pv is not None
        
        assert plant.getPv() == 1
        assert plant.getNmv() == 1
        
    def test002(self):
        
        environment = self.factory.createEnvironmentPoweredByPlant001()

        assert isinstance(environment, SacEnvironment)
        
        environment.reset()

        batchDataEnvironment = environment.observe()
        
        assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
        assert batchDataEnvironment.bufferPv[-1] is not None
        
        for batchDataAgent in self.factory.generateBatchDataAgentForPlant001():
            
            assert isinstance(batchDataAgent, ConcreteBatchDataAgent)
            
            batchDataEnvironment = environment.observe()
            assert batchDataEnvironment.bufferPv[-1] is not None
        
            batchDataReward = environment.update(batchDataAgent)
            
            assert isinstance(batchDataReward, SacBatchDataReward)
        
        assert environment.getNmv() == 1
        assert environment.getNpv() == 1

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()