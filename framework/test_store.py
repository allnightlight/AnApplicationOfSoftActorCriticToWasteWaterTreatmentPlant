'''
Created on 2020/07/10

@author: ukai
'''
import os
import unittest

from framework.agent import Agent
from framework.build_parameter import BuildParameter
from framework.build_parameter_factory import BuildParameterFactory
from framework.store import Store
from framework.store_field import StoreField


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
        if os.path.exists(cls.dbPath):
            os.remove(cls.dbPath)

    
    def setUp(self):
        unittest.TestCase.setUp(self)
        

    def test001(self):
        
        buildParameter = BuildParameter()
        buildParameterMemento = buildParameter.createMemento()
        
        buildParameterFactory = BuildParameterFactory()
        buildParameterAnother = buildParameterFactory.create()
        
        assert buildParameter.__dict__ != buildParameterAnother.__dict__
        
        buildParameterAnother.loadMemento(buildParameterMemento)
        
        assert buildParameter.__dict__ == buildParameterAnother.__dict__
        
    def test002(self):
        
        store = Store(self.dbPath)
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

        store.update_db()
        
        for storeField in store.restore("test%", epoch = epoch):
            assert isinstance(storeField, StoreField)

        for storeField in store.restore("test%", agentKey=agentKey):
            assert isinstance(storeField, StoreField)

        for storeField in store.restore():
            assert isinstance(storeField, StoreField)

        for storeField in store.restore(buildParameterKey=buildParameterKey):
            assert isinstance(storeField, StoreField)

    def test003(self):
        
        store = Store(self.dbPath)

        store.removeHistory()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()