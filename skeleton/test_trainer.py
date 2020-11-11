'''
Created on 2020/11/10

@author: ukai
'''
import unittest
from skeleton.abstract_trainer_factory import AbstractTrainerFactory
from skeleton.abstract_context_factory import AbstractContextFactory
from skeleton.abstract_agent_factory import AbstractAgentFactory
from skeleton.abstract_trainer import AbstractTrainer
from skeleton.abstract_batch_data_environment_factory import AbstractBatchDataEnvironmentFactory
from skeleton.abstract_batch_data_reward_factory import AbstractBatchDataRewardFactory
from skeleton.abstract_batch_data_agent_factory import AbstractBatchDataAgentFactory
from skeleton.abstract_environment_factory import AbstractEnvironmentFactory


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.agentFactory = AbstractAgentFactory()
        self.environmentFactory = AbstractEnvironmentFactory()
        self.contextFactory = AbstractContextFactory()
        self.trainerFactory = AbstractTrainerFactory()
        self.batchDataEnvironmentFactory = AbstractBatchDataEnvironmentFactory()
        self.batchDataAgentFactory = AbstractBatchDataAgentFactory()
        self.rewardFactory = AbstractBatchDataRewardFactory()


    def test001(self):
        
        context = self.contextFactory.create()
        agent = self.agentFactory.create(context)
        environment = self.environmentFactory.create(context)
        trainer = self.trainerFactory.create(context, agent, environment)
        
        assert isinstance(trainer, AbstractTrainer) 

        trainer.train()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()