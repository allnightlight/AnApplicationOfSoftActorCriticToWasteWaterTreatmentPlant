'''
Created on 2020/11/17

@author: ukai
'''
import unittest
from concrete.factory_for_test import FactoryForTest
from concrete.concrete_agent import ConcreteAgent


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = FactoryForTest()


    def test001(self):
        
        agent = self.factory.createAgent()
        
        assert isinstance(agent, ConcreteAgent)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()