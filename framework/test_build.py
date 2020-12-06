'''
Created on 2020/07/09

@author: ukai
'''
from builtins import isinstance
import os
import unittest

from framework.agent import Agent
from framework.agent_factory import AgentFactory
from framework.build_parameter import BuildParameter
from framework.build_parameter_factory import BuildParameterFactory
from framework.builder import Builder
from framework.environment_factory import EnvironmentFactory
from framework.loader import Loader
from framework.mylogger import MyLogger
from framework.store import Store
from framework.trainer_factory import TrainerFactory


class Test(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        
        cls.dbPath = "testDb.sqlite"
        if os.path.exists(cls.dbPath):
            os.remove(cls.dbPath)
            
    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
#         if os.path.exists(cls.dbPath):
#             os.remove(cls.dbPath)
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        agentFactory = AgentFactory()
        environmentFactory = EnvironmentFactory()
        trainerFactory = TrainerFactory()        
        buildParameterFactory = BuildParameterFactory()
        store = Store(self.dbPath)
        logger = MyLogger(console_print=False)
        
        self.builder = Builder(trainerFactory, agentFactory, environmentFactory, store, logger)
        
        self.buildParameters = []
        for k1 in range(3):
            nIntervalSave = 10
            nEpoch = 100
            self.buildParameters.append(BuildParameter(int(nIntervalSave), int(nEpoch), label="test" + str(k1)))
        
        self.loader = Loader(agentFactory, buildParameterFactory, environmentFactory, trainerFactory, store)
        

    def test001(self):
        for buildParameter in self.buildParameters:
            assert isinstance(buildParameter, BuildParameter)
            self.builder.build(buildParameter)
            self.builder.build(buildParameter)
            
        assert isinstance(self.loader, Loader)
        cnt = 0   
        for agent, buildParameter, epoch, environment, trainer in self.loader.load("test%", None):
            assert isinstance(agent, Agent)
            assert isinstance(buildParameter, BuildParameter)
            cnt += 1
        assert cnt > 0
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()