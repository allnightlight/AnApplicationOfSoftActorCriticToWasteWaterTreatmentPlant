'''
Created on 2020/11/14

@author: ukai
'''
import unittest
from skeleton.abstract_plant import AbstractPlant
from skeleton.abstract_environment import AbstractEnvironment
from skeleton.factory_for_test import FactoryForTest


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = FactoryForTest()

    def test001(self):
        
        plant = self.factory.createPlant()
        
        assert isinstance(plant, AbstractPlant)
        
        plant.reset()
        _ = plant.update(u = None)
        _ = plant.getPv()
        
        
    def test002(self):
        
        environment = self.factory.createEnvironment()
        
        assert isinstance(environment, AbstractEnvironment)
        
        environment.reset()
        environment.observe()
        environment.update(self.factory.createBatchDataAgent())
        
        
    def test003(self):
        
        environment = self.factory.createEnvironment()
        
        assert isinstance(environment, AbstractEnvironment)

        assert isinstance(environment.getNmv(), int)
        assert isinstance(environment.getNpv(), int)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()