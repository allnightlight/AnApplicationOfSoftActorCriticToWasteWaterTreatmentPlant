'''
Created on 2020/11/28

@author: ukai
'''
import unittest
from concrete.concrete_builder import ConcreteBuilder
from framework.store import Store
from concrete.concrete_factory_for_test import ConcreteFactoryForTest
from framework.mylogger import MyLogger


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        
        cls.store = Store(dbPath = "testDb.sqlite", trainLogFolderPath = "testTrainLog")

    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        
        cls.store.removeHistory()
                
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = ConcreteFactoryForTest()

    def test001(self):
        
        builder = ConcreteBuilder(store = self.store, logger = MyLogger(console_print = True))
        
        assert isinstance(builder, ConcreteBuilder)
        
        for buildParameter in self.factory.generateBuildParameter():
            builder.build(buildParameter) 
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()