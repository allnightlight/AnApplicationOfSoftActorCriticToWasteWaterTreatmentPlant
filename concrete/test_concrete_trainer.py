'''
Created on 2020/11/23

@author: ukai
'''
import unittest
from concrete.concrete_factory_for_test import ConcreteFactoryForTest
from sac.sac_trainer import SacTrainer
import numpy
from sac.sac_replay_buffer import SacReplayBuffer


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = ConcreteFactoryForTest()


    def test001(self):
        
        for trainer in self.factory.generateTrainer():
        
            assert isinstance(trainer, SacTrainer)
            
            trainer.reset()
                    
            trainer.stepEnvironment()
            
            trainer.stepGradient()
            
            trainer.train()
        
    def test002(self):
        
        for trainer in self.factory.generateTrainer():
        
            assert isinstance(trainer, SacTrainer)
            
            trainer.reset()
            
            assert len(trainer.environment.bufferMv) == 0
            assert len(trainer.environment.bufferPv) == 1
                    
            trainer.stepEnvironment()
            
            assert len(trainer.environment.bufferMv) == 1
            assert len(trainer.environment.bufferPv) == 2
                    
            trainer.stepEnvironment()
            
            assert len(trainer.environment.bufferMv) == 2
            assert len(trainer.environment.bufferPv) == 3
            
            for X in trainer.environment.bufferMv:
                assert isinstance(X, numpy.ndarray) and X is not None
    
            for X in trainer.environment.bufferPv:
                assert isinstance(X, numpy.ndarray) and X is not None

    def test003(self):

        nStepGradient = 2**3
                
        for replayBuffer in self.factory.generateReplayBuffer():
            assert isinstance(replayBuffer, SacReplayBuffer)
            
            replayBuffer.reset()
            
            for _ in range(self.factory.nBatch * nStepGradient):
                replayBuffer.append(self.factory.createBatchDataEnvironment()
                    , self.factory.createBatchDataAgent()
                    , self.factory.createBatchDataReward()
                    , self.factory.createBatchDataEnvironment())

            res = [arg for arg in replayBuffer.generateStateActionRewardAndNextState(nStepGradient)]
            assert len(res) == nStepGradient, len(res)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()