'''
Created on 2020/11/17

@author: ukai
'''
import unittest

from concrete.factory_for_test import FactoryForTest
from concrete.concrete_feature_extractor import ConcreteFeatureExtractor


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = FactoryForTest()
        
        assert isinstance(self.factory, FactoryForTest)

    def test001(self):
        
        featureExtractor = self.factory.createFeatureExtractor()
        
        assert isinstance(featureExtractor, ConcreteFeatureExtractor)
        
        featureExtractor.call(batchDataEnvironment = self.factory.createBatchDataEnvironment())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()