'''
Created on 2020/11/17

@author: ukai
'''
from skeleton.abstract_feature_extractor import AbstractFeatureExtractor
import tensorflow
from concrete.concrete_batch_data_environment import ConcreteBatchDataEnvironment
from concrete.concrete_batch_data_feature import ConcreteBatchDataFeature

class ConcreteFeatureExtractor(AbstractFeatureExtractor, tensorflow.keras.Model):
    '''
    classdocs
    '''
    
    def __init__(self, nFeature):
        super().__init__()
        
        self.nFeature = nFeature
        self.pv2feature = tensorflow.keras.layers.Dense(nFeature)

    def call(self, batchDataEnvironment):
        
        assert isinstance(batchDataEnvironment, ConcreteBatchDataEnvironment)
        
        return ConcreteBatchDataFeature(_Feature = self.pv2feature(batchDataEnvironment.bufferPv[-1])) # (..., nPv) 
