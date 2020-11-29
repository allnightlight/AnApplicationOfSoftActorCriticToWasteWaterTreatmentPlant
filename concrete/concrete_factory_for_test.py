'''
Created on 2020/11/16

@author: ukai
'''
import tensorflow

from concrete.concrete_agent import ConcreteAgent
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_batch_data_environment import ConcreteBatchDataEnvironment
from concrete.concrete_batch_data_feature import ConcreteBatchDataFeature
from concrete.concrete_batch_data_reward import ConcreteBatchDataReward
from concrete.concrete_build_parameter import ConcreteBuildParameter
from concrete.concrete_environment import ConcreteEnvironment
from concrete.concrete_feature_extractor001 import ConcreteFeatureExtractor001
from concrete.concrete_feature_extractor002 import ConcreteFeatureExtractor002
from concrete.concrete_plant001 import ConcretePlant001
from concrete.concrete_plant002 import ConcretePlant002
from concrete.concrete_plant003 import ConcretePlant003
from concrete.concrete_policy import ConcretePolicy
from concrete.concrete_trainer import ConcreteTrainer
from concrete.concrete_value_function_approximator import ConcreteValueFunctionApproximator
from framework.store import Store
import numpy as np
from sac.sac_replay_buffer import SacReplayBuffer


class ConcreteFactoryForTest(object):
    '''
    classdocs
    '''


    def __init__(self, nMv = 3, nPv = 2, nFeature = 4, nBatch = 1, nSampleOfActionsInValueFunctionApproximator = 3, nFeatureHorizon = 2, nHidden = 2**2, alphaTemp = 1.0, updatePolicyByAdvantage = False):
        
        self.nMv = nMv
        self.nPv = nPv
        self.nFeature = nFeature
        self.nBatch = nBatch
        self.nSampleOfActionsInValueFunctionApproximator = nSampleOfActionsInValueFunctionApproximator
        self.nFeatureHorizon = nFeatureHorizon
        self.nHidden = nHidden
        self.alphaTemp = alphaTemp
        self.updatePolicyByAdvantage = updatePolicyByAdvantage
        
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
        
        return ConcreteFeatureExtractor001(nFeature = self.nFeature)

    def createFeatureExtractor002(self):
        
        return ConcreteFeatureExtractor002(nFeature = self.nPv)
    
    def createAgent(self):
        
        return ConcreteAgent(policy = self.createPolicy()
                             , valueFunctionApproximator = self.createValueFunctionApproximator()
                             , featureExtractor = self.createFeatureExtractor()
                             , discountFactor = 0.99
                             , alphaTemp = self.alphaTemp
                             , updatePolicyByAdvantage = self.updatePolicyByAdvantage
                             , saveFolderPath = "./test")
            
    def createTrainer(self):
        
        environment = ConcreteEnvironment(plant = ConcretePlant001()) 
        
        nHidden = 2**3
        nSampleOfActionsInValueFunctionApproximator = 2**3
        nFeature = 2**0
        
        agent = ConcreteAgent(policy = ConcretePolicy(nMv = environment.getNmv())
                              , valueFunctionApproximator = ConcreteValueFunctionApproximator(nFeature, environment.getNmv(), nSampleOfActionsInValueFunctionApproximator, nHidden)
                              , featureExtractor = ConcreteFeatureExtractor001(nFeature)
                              , discountFactor = 0.99
                              , alphaTemp = 1.0
                              , updatePolicyByAdvantage = True
                              , saveFolderPath = "./test")
        
        return ConcreteTrainer(agent = agent
                               , environment = environment
                               , replayBuffer = SacReplayBuffer(bufferSize = 2**10)
                               , nStepEnvironment = 1
                               , nStepGradient = 1
                               , nIntervalUpdateStateValueFunction = 1
                               , nIterationPerEpoch = 10)
        
    def createPlant001(self):
        
        return ConcretePlant001()
    
    def createEnvironmentPoweredByPlant001(self):
        
        return ConcreteEnvironment(plant = ConcretePlant001())
    
    def generateBatchDataAgentForPlant001(self):
        
        nMv = 1
        nBatch = 1
        
        for _ in range(10):
            yield ConcreteBatchDataAgent(_Mean = tensorflow.random.normal(shape = (nBatch, nMv))
                                     , _LogSd = tensorflow.random.normal(shape = (nBatch, nMv)))            
            
    def createPlant002(self):
        
        return ConcretePlant002()
    
    def createEnvironmentPoweredByPlant002(self):
        
        return ConcreteEnvironment(plant = ConcretePlant002())
    
    def generateBatchDataAgentForPlant002(self):
        
        nMv = 1
        nBatch = 1
        
        for _ in range(10):
            yield ConcreteBatchDataAgent(_Mean = tensorflow.random.normal(shape = (nBatch, nMv))
                                     , _LogSd = tensorflow.random.normal(shape = (nBatch, nMv)))
                        
    def createPlant003(self):
        
        return ConcretePlant003()
    
    def createEnvironmentPoweredByPlant003(self):
        
        return ConcreteEnvironment(plant = ConcretePlant003())
    
    def generateBatchDataAgentForPlant003(self):
        
        nMv = ConcretePlant003().getNmv()
        nBatch = 1
        
        for _ in range(10):
            yield ConcreteBatchDataAgent(_Mean = tensorflow.random.normal(shape = (nBatch, nMv))
                                     , _LogSd = tensorflow.random.normal(shape = (nBatch, nMv)))            
            
    def generateBuildParameter(self):
        
        yield ConcreteBuildParameter(nIntervalSave = 1
            , nEpoch = 2**2
            , label = "test"
            , nSampleOfActionsInValueFunctionApproximator = 2**1
            , nStepEnvironment = 1
            , nStepGradient = 1
            , nIntervalUpdateStateValueFunction = 1
            , nIterationPerEpoch = 1
            , bufferSizeReplayBuffer = 2**10)
        
    def createStore(self):
        return Store(dbPath = "testDb.sqlite", trainLogFolderPath = "testTrainLog")