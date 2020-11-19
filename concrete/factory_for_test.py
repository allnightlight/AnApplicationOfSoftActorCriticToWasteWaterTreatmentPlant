'''
Created on 2020/11/16

@author: ukai
'''
from concrete.concrete_agent import ConcreteAgent
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_batch_data_environment import ConcreteBatchDataEnvironment
from concrete.concrete_batch_data_feature import ConcreteBatchDataFeature
from concrete.concrete_feature_extractor import ConcreteFeatureExtractor
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
        
    def createBatchDataEnvironment(self):
        
        return ConcreteBatchDataEnvironment() 

                
    def createBatchDataAgent(self):
        
        _Mv = None
        
        return ConcreteBatchDataAgent(_Mv = _Mv) 
        
    def createBatchDataFeature(self):
        
        _Feature = None
        
        return ConcreteBatchDataFeature(_Feature = _Feature)
    
    def createPolicy(self):
        
        return ConcretePolicy()
    
    def createValueFunctionApproximator(self):
        
        return ConcreteValueFunctionApproximator()
    
    def createFeatureExtractor(self):
        
        return ConcreteFeatureExtractor()
    
    def createAgent(self):
        
        return ConcreteAgent(policy = self.createPolicy()
                             , valueFunctionApproximator = self.createValueFunctionApproximator()
                             , featureExtractor = self.createFeatureExtractor()
                             , discountFactor = 0.99)