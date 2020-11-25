'''
Created on 2020/11/10

@author: ukai
'''
import unittest

from sac.sac_agent import SacAgent
from sac.sac_batch_data_agent import SacBatchDataAgent
from sac.factory_for_test import FactoryForTest


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = FactoryForTest()


    def test001(self):
        
        agent = self.factory.createAgent()
        
        assert isinstance(agent, SacAgent)
                
        batchDataAgent = agent.getAction(self.factory.createBatchDataEnvironment())
        
        assert isinstance(batchDataAgent, SacBatchDataAgent)
        
        
    def test002(self):

        agent = self.factory.createAgent()
        
        assert isinstance(agent, SacAgent)        
        
        agent.updatePolicy(batchDataEnvironment = self.factory.createBatchDataEnvironment())

        agent.updateStateValueFunction(batchDataEnvironment = self.factory.createBatchDataEnvironment())
        
        agent.updateActionValueFunction(batchDataEnvironment = self.factory.createBatchDataEnvironment()
                                , batchDataAgent = self.factory.createBatchDataAgent()
                                , batchDataReward = self.factory.createBatchDataReward()
                                , batchDataEnvironmentNextStep = self.factory.createBatchDataEnvironment())
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()