'''
Created on 2020/11/10

@author: ukai
'''
import unittest
from sac.sac_trainer import SacTrainer
from sac.sac_replay_buffer import SacReplayBuffer
from sac.sac_factory_for_test import SacFactoryForTest
from sac.sac_batch_data_environment import SacBatchDataEnvironment


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = SacFactoryForTest()


    def test001(self):
        
        trainer = self.factory.createTrainer()
        
        assert isinstance(trainer, SacTrainer) 

        trainer.reset()
        trainer.train()
        
    def test002(self):
        
        bufferSize = 10
        buffer = SacReplayBuffer(bufferSize)
        buffer.reset()
        for k1 in range(bufferSize * 2 + 1):
            assert len(buffer.buffer) <= bufferSize
            assert len(buffer.buffer) == min(k1, bufferSize)
            
            buffer.append(None, None, None, None)
            
    def test003(self):

        trainer = self.factory.createTrainer()        
        
        assert isinstance(trainer, SacTrainer) 

        trainer.reset()
        try:
            trainer.stepGradient()
            assert False
        except:
            pass
            
    def test004(self):
        
        nIteration = 2**3
        trainer = self.factory.createTrainer()
        
        assert isinstance(trainer, SacTrainer) 

        replayBuffer = trainer.replayBuffer
        assert isinstance(replayBuffer, SacReplayBuffer)

        trainer.reset()
        trainer.train()
        
        for k1 in range(nIteration):
            batchDataEnvironment = replayBuffer.buffer[k1][0]
            
            assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
            
            assert len(batchDataEnvironment.bufferMv) == k1, "%d" % len(batchDataEnvironment.bufferMv)
            assert len(batchDataEnvironment.bufferPv) == k1+1, "%d" % len(batchDataEnvironment.bufferPv) 
    
    def test005(self):        
        
        bufferSize = 2**7
        nStepGradient = 2**3
        buffer = SacReplayBuffer(bufferSize)
        buffer.reset()
        for k1 in range(bufferSize * 2 + 1):
            
            assert len([*buffer.generateStateActionRewardAndNextState(nStepGradient)]) == min(k1, nStepGradient)
            
            buffer.append(None, None, None, None)
            
    def test006(self):
        
        trainer = self.factory.createTrainer()
        trainer.nStepEnvironment = 2**5
        trainer.nStepGradient = 1
        trainer.nIterationPerEpoch = 1
        
        nEpoch = 2**7 
        
        assert isinstance(trainer, SacTrainer) 
        
        trainer.reset()
        for _ in range(nEpoch):
            trainer.train()
        assert trainer.cntStepEnvironment == nEpoch        
        assert trainer.cntStepGradient == (nEpoch//trainer.nStepEnvironment)
        
        
#         assert trainer.cntStepGradient == trainer.nIterationPerEpoch//trainer.nStepEnvironment*trainer.nStepGradient

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()