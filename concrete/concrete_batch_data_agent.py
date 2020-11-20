'''
Created on 2020/11/15

@author: ukai
'''
from skeleton.abstract_batch_data_agent import AbstractBatchDataAgent

class ConcreteBatchDataAgent(AbstractBatchDataAgent):
    '''
    classdocs
    '''


    def __init__(self, _Mean, _LogSd):
        AbstractBatchDataAgent.__init__(self)
        self._Mv = _Mean
        self._LogSd = _LogSd
        
    def getValue(self):
        return self._Mv