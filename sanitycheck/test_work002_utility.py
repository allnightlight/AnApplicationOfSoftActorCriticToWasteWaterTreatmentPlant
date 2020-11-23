'''
Created on 2020/11/23

@author: ukai
'''
import unittest
from sanitycheck.work002_utility import Work002Utility


class Test(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.utility = Work002Utility.create(alphaTemp = 1.0, discountFactor = 0.01, nIteration=2**0) 

    def test001(self):
        
        self.utility.runTraining()
        
    def test002(self):
        
        self.utility.runTraining()
        
        self.utility.plotTrainedPi()
        
        self.utility.plotTrainedQ()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()