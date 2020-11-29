'''
Created on 2020/07/10

@author: ukai
'''
from builtins import isinstance
import os
import unittest

from framework.agent import Agent
from framework.agent_factory import AgentFactory
from framework.build_parameter import BuildParameter
from framework.build_parameter_factory import BuildParameterFactory
from framework.environment import Environment
from framework.environment_factory import EnvironmentFactory
from framework.loader import Loader
from framework.store import Store
from framework.store_field import StoreField
from framework.trainer import Trainer
from framework.trainer_factory import TrainerFactory
import pandas as pd


class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        
        dbPath = "testDb.sqlite"
        if os.path.exists(dbPath):
            os.remove(dbPath)
        
        store = Store(dbPath)
        assert isinstance(store, Store)
        
        for k1 in range(2**3):
            buildParameter = BuildParameter(label = "test" + str(k1))
            agent = Agent()

            for epoch in range(2**4):        
        
                agentMemento = agent.createMemento()
                buildParameterMemento = buildParameter.createMemento()
                buildParameterKey = buildParameter.key
                buildParameterLabel = buildParameter.label
                agentKey = agent.getAgentKey()
        
                storeField = StoreField(agentMemento, epoch, buildParameterMemento, buildParameterKey, buildParameterLabel, agentKey)
                assert isinstance(storeField, StoreField)
                
                store.append(storeField)
                
        cls.dbPath = dbPath
        

    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        if os.path.exists(cls.dbPath):
            os.remove(cls.dbPath)


    def test0001(self):
        
        store = Store(self.dbPath)
        agentFactory = AgentFactory()
        environmentFactory = EnvironmentFactory()
        buildParameterFactory = BuildParameterFactory()
        trainerFactory = TrainerFactory()
        
        loader = Loader(agentFactory, buildParameterFactory, environmentFactory, trainerFactory, store)
        assert isinstance(loader, Loader)
        
        for agent, buildParameter, epoch, environment, trainer in loader.load("test%", None):
            assert isinstance(agent, Agent)
            assert isinstance(buildParameter, BuildParameter)
            assert isinstance(environment, Environment)
            assert isinstance(trainer, Trainer)

        epochGiven = 1
        for agent, buildParameter, epoch, environment, trainer in loader.load("test%", epoch=epochGiven):
            assert isinstance(agent, Agent)
            assert isinstance(buildParameter, BuildParameter)
            assert epoch == epochGiven
            assert isinstance(environment, Environment)
            assert isinstance(trainer, Trainer)


        buildParameterKeyGiven = buildParameter.key
        for agent, buildParameter, epoch, environment, trainer in loader.load("test%", buildParameterKey=buildParameterKeyGiven):
            assert isinstance(agent, Agent)
            assert isinstance(buildParameter, BuildParameter)
            assert buildParameter.key == buildParameterKeyGiven
            assert isinstance(environment, Environment)
            assert isinstance(trainer, Trainer)


        for agent, buildParameter, epoch, environment, trainer in loader.load("test%", buildParameterKey=buildParameterKeyGiven, epoch = epochGiven):
            assert isinstance(agent, Agent)
            assert isinstance(buildParameter, BuildParameter)
            assert buildParameter.key == buildParameterKeyGiven
            assert epoch == epochGiven
            assert isinstance(environment, Environment)
            assert isinstance(trainer, Trainer)

        agentKey = None
        for agent, buildParameter, epoch, environment, trainer in loader.load():
            agentKey = agent.getAgentKey()
            break

        assert agentKey is not None
        for agent, buildParameter, epoch, environment, trainer in loader.load(agentKey=agentKey):
            assert agent.getAgentKey() == agentKey            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test0001']
    unittest.main()