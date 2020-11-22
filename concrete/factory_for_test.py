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
from concrete.concrete_batch_data_reward import ConcreteBatchDataReward
import tensorflow
import numpy as np


class FactoryForTest(object):
    '''
    classdocs
    '''


    def __init__(self, nMv = 3, nPv = 2, nFeature = 4, nBatch = 1, nSampleOfActionsInValueFunctionApproximator = 3, nFeatureHorizon = 2, nHidden = 2**2, alphaTemp = 1.0):
        
        self.nMv = nMv
        self.nPv = nPv
        self.nFeature = nFeature
        self.nBatch = nBatch
        self.nSampleOfActionsInValueFunctionApproximator = nSampleOfActionsInValueFunctionApproximator
        self.nFeatureHorizon = nFeatureHorizon
        self.nHidden = nHidden
        self.alphaTemp = alphaTemp
        
    def createBatchDataEnvironment(self):
        
        bufferPv = [np.random.randn(self.nBatch, self.nPv).astype(np.float32) for _ in range(self.nFeatureHorizon + 1)]
        bufferMv = [np.random.randn(self.nBatch, self.nMv).astype(np.float32) for _ in range(self.nFeatureHorizon)]
        
        return ConcreteBatchDataEnvironment(bufferPv, bufferMv) 

                
    def createBatchDataAgent(self):
        
        return ConcreteBatchDataAgent(_Mean = tensorflow.random.normal(shape = (self.nBatch, self.nMv))
                                      , _LogSd  = tensorflow.random.normal(shape = (self.nBatch, self.nMv))) 
        
    def createBatchDataFeature(self):
        
        _Feature = tensorflow.random.normal(shape = (self.nBatch, self.nFeature))
        
        return ConcreteBatchDataFeature(_Feature = _Feature)

    def createBatchDataReward(self):
        
        return ConcreteBatchDataReward(reward = 1.0)
    
    def createPolicy(self):
        
        return ConcretePolicy(nMv = self.nMv)
    
    def createValueFunctionApproximator(self):
        
        return ConcreteValueFunctionApproximator(nFeature = self.nFeature, nMv = self.nMv, nSampleOfActionsInValueFunctionApproximator = self.nSampleOfActionsInValueFunctionApproximator, nHidden = self.nHidden)
    
    def createFeatureExtractor(self):
        
        return ConcreteFeatureExtractor(nFeature = self.nFeature)
    
    def createAgent(self):
        
        return ConcreteAgent(policy = self.createPolicy()
                             , valueFunctionApproximator = self.createValueFunctionApproximator()
                             , featureExtractor = self.createFeatureExtractor()
                             , discountFactor = 0.99
                             , alphaTemp = self.alphaTemp)