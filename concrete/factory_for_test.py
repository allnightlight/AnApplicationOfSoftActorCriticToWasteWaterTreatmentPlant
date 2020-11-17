'''
Created on 2020/11/16

@author: ukai
'''
import tensorflow
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_batch_data_feature import ConcreteBatchDataFeature
from concrete.concrete_policy import ConcretePolicy
from concrete.concrete_value_function_approximator import ConcreteValueFunctionApproximator


class FactoryForTest(object):
    '''
    classdocs
    '''


    def __init__(self, nMv = 3, nPv = 2, nFeature = 4, nBatch = 1):
        
        self.nMv = nMv
        self.nPv = nPv
        self.nFeature = nFeature
        self.nBatch = nBatch
                
    def createBatchDataAgent(self):
        
        _Mv = tensorflow.random.normal(shape = (self.nBatch, self.nMv))
        
        return ConcreteBatchDataAgent(_Mv = _Mv) 
        
    def createBatchDataFeature(self):
        
        _Feature = tensorflow.random.normal(shape = (self.nBatch, self.nFeature))
        
        return ConcreteBatchDataFeature(_Feature = _Feature)
    
    def createPolicy(self):
        
        return ConcretePolicy(nMv = self.nMv)
    
    def createValueFunctionApproximator(self):
        
        return ConcreteValueFunctionApproximator()