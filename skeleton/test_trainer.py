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
from skeleton.abstract_replay_buffer import AbstractReplayBuffer


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

        trainer.reset()
        trainer.train(1)
        
    def test002(self):
        
        bufferSize = 10
        buffer = AbstractReplayBuffer(bufferSize)
        buffer.reset()
        for k1 in range(bufferSize * 2 + 1):
            assert len(buffer.buffer) <= bufferSize
            assert len(buffer.buffer) == min(k1, bufferSize)
            
            buffer.append(None, None, None, None)
            
    def test003(self):
        
        context = self.contextFactory.create()
        agent = self.agentFactory.create(context)
        environment = self.environmentFactory.create(context)
        trainer = self.trainerFactory.create(context, agent, environment)
        
        assert isinstance(trainer, AbstractTrainer) 

        trainer.reset()
        try:
            trainer.stepGradient()
            assert False
        except:
            pass
            
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()