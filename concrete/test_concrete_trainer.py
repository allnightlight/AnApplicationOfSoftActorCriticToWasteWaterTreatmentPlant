'''
Created on 2020/11/23

@author: ukai
'''
import unittest
from concrete.factory_for_test import FactoryForTest
from sac.sac_trainer import SacTrainer
import numpy


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = FactoryForTest()


    def test001(self):
        
        trainer = self.factory.createTrainer()
        
        assert isinstance(trainer, SacTrainer)
        
        trainer.reset()
                
        trainer.stepEnvironment()
        
        trainer.stepGradient()
        
        trainer.train(nIteration = 10)
        
    def test002(self):
        
        trainer = self.factory.createTrainer()
        
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


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()