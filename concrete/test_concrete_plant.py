'''
Created on 2020/11/26

@author: ukai
'''
import unittest

from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_batch_data_reward import ConcreteBatchDataReward
from concrete.concrete_factory_for_test import ConcreteFactoryForTest
import numpy as np
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from sac.sac_environment import SacEnvironment


class Test(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)

        self.factory = ConcreteFactoryForTest()

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
             
            assert isinstance(batchDataReward, ConcreteBatchDataReward)
         
        assert environment.getNmv() == 1
        assert environment.getNpv() == 1
 
    def test003(self):
         
        plant = self.factory.createPlant002()
         
        plant.reset()
         
        reward = plant.update(u = np.ones((1,1)))
        assert reward is not None
 
        pv = plant.getPv()
        assert pv is not None
                 
    def test004(self):
         
        environment = self.factory.createEnvironmentPoweredByPlant002()
 
        assert isinstance(environment, SacEnvironment)
         
        environment.reset()
 
        batchDataEnvironment = environment.observe()
         
        assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
        assert batchDataEnvironment.bufferPv[-1] is not None
         
        for batchDataAgent in self.factory.generateBatchDataAgentForPlant002():
             
            assert isinstance(batchDataAgent, ConcreteBatchDataAgent)
             
            batchDataEnvironment = environment.observe()
            assert batchDataEnvironment.bufferPv[-1] is not None
         
            batchDataReward = environment.update(batchDataAgent)
             
            assert isinstance(batchDataReward, ConcreteBatchDataReward)
         
        assert environment.getNmv() == 1
        assert environment.getNpv() == 1

    def test005(self):
         
        plant = self.factory.createPlant003()
         
        plant.reset()
         
        reward = plant.update(u = np.ones((1,plant.getNmv())))
        assert reward is not None
 
        pv = plant.getPv()
        assert pv is not None
                 
    def test006(self):
         
        environment = self.factory.createEnvironmentPoweredByPlant003()
 
        assert isinstance(environment, SacEnvironment)
         
        environment.reset()
 
        batchDataEnvironment = environment.observe()
         
        assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
        assert batchDataEnvironment.bufferPv[-1] is not None
         
        for batchDataAgent in self.factory.generateBatchDataAgentForPlant003():
             
            assert isinstance(batchDataAgent, ConcreteBatchDataAgent)
             
            batchDataEnvironment = environment.observe()
            assert batchDataEnvironment.bufferPv[-1] is not None
         
            batchDataReward = environment.update(batchDataAgent)
             
            assert isinstance(batchDataReward, ConcreteBatchDataReward)
         

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()