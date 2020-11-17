'''
Created on 2020/11/15

@author: ukai
'''
from skeleton.abstract_batch_data_agent import AbstractBatchDataAgent

class ConcreteBatchDataAgent(AbstractBatchDataAgent):
    '''
    classdocs
    '''


    def __init__(self, _Mv):
        AbstractBatchDataAgent.__init__(self)
        self._Mv = _Mv
        
    def getValue(self):
        return self._Mv