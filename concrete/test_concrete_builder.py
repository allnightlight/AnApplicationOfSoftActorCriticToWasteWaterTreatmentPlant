'''
Created on 2020/11/28

@author: ukai
'''
import unittest
from concrete.concrete_builder import ConcreteBuilder
from concrete.concrete_factory_for_test import ConcreteFactoryForTest
from framework.mylogger import MyLogger
from concrete.concrete_loader import ConcreteLoader
from concrete.concrete_build_parameter import ConcreteBuildParameter
from concrete.concrete_agent import ConcreteAgent
from concrete.concrete_environment import ConcreteEnvironment
from concrete.concrete_trainer import ConcreteTrainer


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        
        cls.factory = ConcreteFactoryForTest()
        cls.store = cls.factory.createStore() 

    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        
        cls.store.removeHistory()
                
    def test001(self):
        
        builder = ConcreteBuilder(store = self.store, logger = MyLogger(console_print = True))
        
        assert isinstance(builder, ConcreteBuilder)
        
        for buildParameter in self.factory.generateBuildParameter():
            builder.build(buildParameter)         

    def test002(self):
        
        loader = ConcreteLoader(store = self.store)
        
        assert isinstance(loader, ConcreteLoader)
    
        for agent, buildParameter, epoch, environment, trainer in loader.load("%"):
            
            assert isinstance(agent, ConcreteAgent)
            assert isinstance(buildParameter, ConcreteBuildParameter)
            assert epoch > 0
            assert isinstance(environment, ConcreteEnvironment)
            assert isinstance(trainer, ConcreteTrainer)
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()