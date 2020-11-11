'''
Created on 2020/11/10

@author: ukai
'''
from skeleton.abstract_batch_data_agent import AbstractBatchDataAgent

class AbstractBatchDataAgentFactory(object):
    '''
    classdocs
    '''


    def create(self, context):
        return AbstractBatchDataAgent()