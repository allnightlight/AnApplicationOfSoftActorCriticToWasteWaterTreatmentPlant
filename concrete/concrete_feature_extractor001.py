'''
Created on 2020/11/17

@author: ukai
'''
import tensorflow

from concrete.concrete_batch_data_feature import ConcreteBatchDataFeature
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from sac.sac_feature_extractor import SacFeatureExtractor


class ConcreteFeatureExtractor001(SacFeatureExtractor, tensorflow.keras.Model):
    '''
    classdocs
    '''
    
    def __init__(self, nFeature):
        super().__init__()
        
        self.nFeature = nFeature
        self.pv2feature = tensorflow.keras.layers.Dense(nFeature)

    def call(self, batchDataEnvironment):
        
        assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
        
        return ConcreteBatchDataFeature(_Feature = self.pv2feature(batchDataEnvironment.bufferPv[-1])) # (..., nPv) 
