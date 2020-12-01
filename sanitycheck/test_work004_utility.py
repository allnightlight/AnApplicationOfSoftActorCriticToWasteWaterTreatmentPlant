'''
Created on 2020/11/29

@author: ukai
'''
import unittest
from sanitycheck.work004_utility import Work004Utility
from concrete.concrete_build_parameter import ConcreteBuildParameter


class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        
        cls.app, cls.store = Work004Utility.create(nAgent = 3, nEpoch = 2**1)
        
    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        
        cls.store.removeHistory()

    def test001(self):
        
        self.app.build()        
        
    def test002(self):
        self.app.evaluate()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()