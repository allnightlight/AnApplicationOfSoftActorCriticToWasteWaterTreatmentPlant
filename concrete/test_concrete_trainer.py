'''
Created on 2020/11/23

@author: ukai
'''
import unittest
from concrete.factory_for_test import FactoryForTest
from skeleton.abstract_trainer import AbstractTrainer


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = FactoryForTest()


    def test001(self):
        
        trainer = self.factory.createTrainer()
        
        assert isinstance(trainer, AbstractTrainer)
        
        trainer.reset()
                
        trainer.stepEnvironment()
        
        trainer.stepGradient()
        
        trainer.train(nIteration = 10)
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()