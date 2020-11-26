'''
Created on 2020/11/26

@author: ukai
'''
import unittest
from sanitycheck.work003_utilitiy import Work003Utility


class Test(unittest.TestCase):


    def test001(self):
        
        Work003Utility.create().runSimulationCase001()
        
    def test002(self):
        
        Work003Utility.create().runSimulationCase002()

    def test003(self):
        
        Work003Utility.create().runSimulationCase003()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()