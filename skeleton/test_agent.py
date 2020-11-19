'''
Created on 2020/11/10

@author: ukai
'''
import unittest

from skeleton.abstract_agent import AbstractAgent
from skeleton.abstract_agent_factory import AbstractAgentFactory
from skeleton.abstract_batch_data_agent import AbstractBatchDataAgent
from skeleton.abstract_batch_data_agent_factory import AbstractBatchDataAgentFactory
from skeleton.abstract_batch_data_environment_factory import AbstractBatchDataEnvironmentFactory
from skeleton.abstract_batch_data_feature import AbstractBatchDataFeature
from skeleton.abstract_batch_data_reward_factory import AbstractBatchDataRewardFactory
from skeleton.abstract_batch_data_value import AbstractBatchDataValue
from skeleton.abstract_context_factory import AbstractContextFactory


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.contextFactory = AbstractContextFactory()
        self.agentFactory = AbstractAgentFactory()
        self.batchDataEnvironmentFactory = AbstractBatchDataEnvironmentFactory()
        self.batchDataAgentFactory = AbstractBatchDataAgentFactory()
        self.rewardFactory = AbstractBatchDataRewardFactory()


    def test001(self):
        
        context = self.contextFactory.create() 
        
        agent = self.agentFactory.create(context)
        
        assert isinstance(agent, AbstractAgent)
        
        batchDataFeature = agent.getFeature(self.batchDataEnvironmentFactory.create(context))
        
        assert isinstance(batchDataFeature, AbstractBatchDataFeature)
        
        batchDataAgent = agent.getAction(self.batchDataEnvironmentFactory.create(context))
        
        assert isinstance(batchDataAgent, AbstractBatchDataAgent)

        batchDataActionValue = agent.getActionValue(self.batchDataEnvironmentFactory.create(context)
                                        , batchDataAgent)
        
        assert isinstance(batchDataActionValue, AbstractBatchDataValue)
        
        batchDataStateValue = agent.getActionValue(self.batchDataEnvironmentFactory.create(context)
                                        , batchDataAgent)
        
        assert isinstance(batchDataStateValue, AbstractBatchDataValue)
        
        
    def test002(self):

        context = self.contextFactory.create() 
        
        agent = self.agentFactory.create(context)
        
        assert isinstance(agent, AbstractAgent)        
        
        agent.updatePolicy(batchDataEnvironment = self.batchDataEnvironmentFactory.create(context))

        agent.updateStateValueFunction(batchDataEnvironment = self.batchDataEnvironmentFactory.create(context))
        
        agent.updateActionValueFunction(batchDataEnvironment = self.batchDataEnvironmentFactory.create(context)
                                , batchDataAgent = self.batchDataAgentFactory.create(context)
                                , batchDataReward = self.rewardFactory.create(context)
                                , batchDataEnvironmentNextStep = self.batchDataEnvironmentFactory.create(context))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()