'''
Created on 2020/11/17

@author: ukai
'''
from sac.sac_batch_data_environment import SacBatchDataEnvironment

class ConcreteBatchDataEnvironment(SacBatchDataEnvironment):
    '''
    classdocs
    '''
    
    
    def __init__(self, bufferPv, bufferMv):
        super(ConcreteBatchDataEnvironment, self).__init__(bufferPv, bufferMv)

        