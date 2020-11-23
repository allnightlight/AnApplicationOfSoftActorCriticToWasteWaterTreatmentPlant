'''
Created on 2020/11/14

@author: ukai
'''
import unittest
from skeleton.abstract_environment_factory import AbstractEnvironmentFactory
from skeleton.abstract_context import AbstractContext
from skeleton.abstract_context_factory import AbstractContextFactory
from skeleton.abstract_plant import AbstractPlant
from skeleton.abstract_environment import AbstractEnvironment
from skeleton.abstract_batch_data_agent_factory import AbstractBatchDataAgentFactory


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.contextFactory = AbstractContextFactory()
        self.environmentFactory = AbstractEnvironmentFactory()

    def test001(self):
        
        plant = self.environmentFactory.createPlant(self.contextFactory.create())
        
        assert isinstance(plant, AbstractPlant)
        
        plant.reset()
        _ = plant.update(u = None)
        _ = plant.getPv()
        
        
    def test002(self):
        
        context = self.contextFactory.create()
        environment = self.environmentFactory.create(context)
        
        assert isinstance(environment, AbstractEnvironment)
        
        environment.reset()
        environment.observe()
        environment.update(AbstractBatchDataAgentFactory().create(context))
        
        
    def test003(self):
        
        context = self.contextFactory.create()
        environment = self.environmentFactory.create(context)
        
        assert isinstance(environment, AbstractEnvironment)

        assert isinstance(environment.getNmv(), int)
        assert isinstance(environment.getNpv(), int)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()