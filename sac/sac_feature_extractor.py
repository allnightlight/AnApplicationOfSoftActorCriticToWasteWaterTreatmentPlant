'''
Created on 2020/11/10

@author: ukai
'''
from skeleton.abstract_batch_data_environment import AbstractBatchDataEnvironment
from skeleton.abstract_batch_data_feature import AbstractBatchDataFeature

class AbstractFeatureExtractor(object):
    '''
    classdocs
    '''


    def call(self, batchDataEnvironment):
        
        assert isinstance(batchDataEnvironment, AbstractBatchDataEnvironment)
        
        return AbstractBatchDataFeature()