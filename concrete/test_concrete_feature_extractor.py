'''
Created on 2020/11/17

@author: ukai
'''
import unittest

from concrete.concrete_batch_data_feature import ConcreteBatchDataFeature
from concrete.concrete_feature_extractor import ConcreteFeatureExtractor
from concrete.factory_for_test import FactoryForTest
import tensorflow


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = FactoryForTest()
        
        assert isinstance(self.factory, FactoryForTest)

    def test001(self):
        
        featureExtractor = self.factory.createFeatureExtractor()
        
        assert isinstance(featureExtractor, ConcreteFeatureExtractor)
        
        batchDataFeature = featureExtractor.call(batchDataEnvironment = self.factory.createBatchDataEnvironment())
        
        assert isinstance(batchDataFeature, ConcreteBatchDataFeature)
        
        _Feature = batchDataFeature.getFeature()
        
        assert isinstance(_Feature, tensorflow.Tensor)
        assert _Feature.shape == (self.factory.nBatch, self.factory.nFeature)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()