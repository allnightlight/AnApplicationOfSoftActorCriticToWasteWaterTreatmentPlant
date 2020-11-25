'''
Created on 2020/11/10

@author: ukai
'''
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from sac.sac_batch_data_feature import SacBatchDataFeature

class SacFeatureExtractor(object):
    '''
    classdocs
    '''


    def call(self, batchDataEnvironment):
        
        assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
        
        return SacBatchDataFeature()