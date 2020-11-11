'''
Created on 2020/11/10

@author: ukai
'''
from skeleton.abstract_batch_data_environment import AbstractBatchDataEnvironment

class AbstractBatchDataEnvironmentFactory(object):
    '''
    classdocs
    '''


    def create(self, context):
        return AbstractBatchDataEnvironment()