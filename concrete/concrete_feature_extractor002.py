'''
Created on 2020/11/27

@author: ukai
'''
import tensorflow

from concrete.concrete_batch_data_feature import ConcreteBatchDataFeature
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from sac.sac_feature_extractor import SacFeatureExtractor


class ConcreteFeatureExtractor002(SacFeatureExtractor, tensorflow.keras.Model):
    '''
    classdocs
    '''
    
    def __init__(self, nFeature):
        super().__init__()
        
        self.nFeature = nFeature
        
    def call(self, batchDataEnvironment):
        
        assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
        assert batchDataEnvironment.bufferPv[-1].shape[-1] == self.nFeature
        
        return ConcreteBatchDataFeature(_Feature = tensorflow.constant(batchDataEnvironment.bufferPv[-1])) # (..., nPv) 
        