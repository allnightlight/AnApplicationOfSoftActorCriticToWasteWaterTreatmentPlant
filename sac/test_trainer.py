'''
Created on 2020/11/10

@author: ukai
'''
import unittest
from sac.sac_trainer import SacTrainer
from sac.sac_replay_buffer import SacReplayBuffer
from sac.factory_for_test import FactoryForTest


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = FactoryForTest()


    def test001(self):
        
        trainer = self.factory.createTrainer()
        
        assert isinstance(trainer, SacTrainer) 

        trainer.reset()
        trainer.train(1)
        
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
            
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()