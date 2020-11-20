'''
Created on 2020/11/17

@author: ukai
'''
from skeleton.abstract_batch_data_environment import AbstractBatchDataEnvironment

class ConcreteBatchDataEnvironment(AbstractBatchDataEnvironment):
    '''
    classdocs
    '''
    
    
    def __init__(self, bufferPv, bufferMv):
        super(ConcreteBatchDataEnvironment, self).__init__(bufferPv, bufferMv)

        