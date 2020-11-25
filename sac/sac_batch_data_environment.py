'''
Created on 2020/11/10

@author: ukai
'''

class AbstractBatchDataEnvironment(object):
    '''
    classdocs
    '''

    def __init__(self, bufferPv = None, bufferMv = None):
        
        self.bufferPv = bufferPv
        self.bufferMv = bufferMv