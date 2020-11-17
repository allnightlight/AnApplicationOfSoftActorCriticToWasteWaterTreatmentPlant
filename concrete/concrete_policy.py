'''
Created on 2020/11/15

@author: ukai
'''

from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from skeleton.abstract_policy import AbstractPolicy


class ConcretePolicy(AbstractPolicy):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        
        AbstractPolicy.__init__(self)
                
        
    def call(self, batchDataFeature):
                
        return ConcreteBatchDataAgent(None)
    