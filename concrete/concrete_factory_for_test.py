'''
Created on 2020/11/16

@author: ukai
'''
import tensorflow

from concrete.concrete_agent import ConcreteAgent
from concrete.concrete_application import ConcreteApplication
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_batch_data_environment import ConcreteBatchDataEnvironment
from concrete.concrete_batch_data_feature import ConcreteBatchDataFeature
from concrete.concrete_batch_data_reward import ConcreteBatchDataReward
from concrete.concrete_build_parameter import ConcreteBuildParameter
from concrete.concrete_build_parameter_factory import ConcreteBuildParameterFactory
from concrete.concrete_builder import ConcreteBuilder
from concrete.concrete_environment import ConcreteEnvironment
from concrete.concrete_evaluation_db import ConcreteEvaluationDb
from concrete.concrete_feature_extractor001 import ConcreteFeatureExtractor001
from concrete.concrete_feature_extractor002 import ConcreteFeatureExtractor002
from concrete.concrete_loader import ConcreteLoader
from concrete.concrete_plant001 import ConcretePlant001
from concrete.concrete_plant002 import ConcretePlant002
from concrete.concrete_plant003 import ConcretePlant003
from concrete.concrete_simulator_factory_for_evaluation import ConcreteSimulatorFactoryForEvaluation
from concrete.concrete_trainer import ConcreteTrainer
from concrete.concrete_value_function_approximator import ConcreteValueFunctionApproximator
from framework.mylogger import MyLogger
from framework.store import Store
import numpy as np
from sac.sac_evaluate_method import SacEvaluateMethod
from sac.sac_evaluator import SacEvaluator
from sac.sac_replay_buffer import SacReplayBuffer
from sac.sac_simulator_factory import SacSimulatorFactory
from concrete.concrete_evaluate_method001 import ConcreteEvaluateMethod001
import os
import shutil
from concrete.concrete_evaluate_method002 import ConcreteEvaluateMethod002
from concrete.concrete_policy002 import ConcretePolicy002
from concrete.concrete_policy001 import ConcretePolicy001


class ConcreteFactoryForTest(object):
    '''
    classdocs
    '''


    def __init__(self, nMv = 3, nPv = 2, nFeature = 4, nBatch = 1, nSampleOfActionsInValueFunctionApproximator = 3, nFeatureHorizon = 2, nHidden = 2**2, alphaTemp = 1.0, updatePolicyByAdvantage = False, figFolderPath = "./fig", dataFolderPath = "./data"):
        
        self.nMv = nMv
        self.nPv = nPv
        self.nFeature = nFeature
        self.nBatch = nBatch
        self.nSampleOfActionsInValueFunctionApproximator = nSampleOfActionsInValueFunctionApproximator
        self.nFeatureHorizon = nFeatureHorizon
        self.nHidden = nHidden
        self.alphaTemp = alphaTemp
        self.updatePolicyByAdvantage = updatePolicyByAdvantage
        self.figFolderPath = figFolderPath
        self.dataFolderPath = dataFolderPath
        
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
    
    def generatePolicy(self):
        
        yield ConcretePolicy001(nMv = self.nMv)
        yield ConcretePolicy002(nMv = self.nMv)
    
    def createValueFunctionApproximator(self):
        
        return ConcreteValueFunctionApproximator(nFeature = self.nFeature, nMv = self.nMv, nSampleOfActionsInValueFunctionApproximator = self.nSampleOfActionsInValueFunctionApproximator, nHidden = self.nHidden)
    
    def createFeatureExtractor(self):
        
        return ConcreteFeatureExtractor001(nFeature = self.nFeature)

    def createFeatureExtractor002(self):
        
        return ConcreteFeatureExtractor002(nFeature = self.nPv)
    
    def createAgent(self):
        
        return ConcreteAgent(policy = ConcretePolicy001(nMv = self.nMv)
                             , valueFunctionApproximator = self.createValueFunctionApproximator()
                             , featureExtractor = self.createFeatureExtractor()
                             , discountFactor = 0.99
                             , alphaTemp = self.alphaTemp
                             , updatePolicyByAdvantage = self.updatePolicyByAdvantage
                             , saveFolderPath = "./test"
                             , learningRateForUpdateActionValueFunction = 1e-3
                             , learningRateForUpdatePolicy = 1e-3
                             , learningRateForUpdateStateValueFunction = 1e-3)            

    def generateTrainer(self):
        
        environment = ConcreteEnvironment(plant = ConcretePlant001()) 
        
        nHidden = 2**3
        nSampleOfActionsInValueFunctionApproximator = 2**3
        nFeature = 2**0
        
        for policy in [ConcretePolicy001(nMv = environment.getNmv()), ConcretePolicy002(nMv = environment.getNmv()),]:
            
            agent = ConcreteAgent(policy = policy
                                  , valueFunctionApproximator = ConcreteValueFunctionApproximator(nFeature, environment.getNmv(), nSampleOfActionsInValueFunctionApproximator, nHidden)
                                  , featureExtractor = ConcreteFeatureExtractor001(nFeature)
                                  , discountFactor = 0.99
                                  , alphaTemp = 1.0
                                  , updatePolicyByAdvantage = True
                                  , saveFolderPath = "./test"
                                  , learningRateForUpdateActionValueFunction = 1e-3
                                  , learningRateForUpdatePolicy = 1e-3
                                  , learningRateForUpdateStateValueFunction = 1e-3)
    
            
            yield ConcreteTrainer(agent = agent
                                   , environment = environment
                                   , replayBuffer = SacReplayBuffer(bufferSize = 2**10)
                                   , simulatorFactory = SacSimulatorFactory(nSimulationStep=1)
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

        for plantClass in ("ConcretePlant001", "ConcretePlant002", "ConcretePlant003", "ConcretePlant004"):        
            yield ConcreteBuildParameter(nIntervalSave = 1
                , nEpoch = 2**2
                , label = "test"
                , nSampleOfActionsInValueFunctionApproximator = 2**1
                , nStepEnvironment = 1
                , nStepGradient = 1
                , nIntervalUpdateStateValueFunction = 1
                , nIterationPerEpoch = 1
                , bufferSizeReplayBuffer = 2**10
                , plantClass=plantClass)
        
    def createStore(self):
        return Store(dbPath = "testDb.sqlite", trainLogFolderPath = "testTrainLog")
    
    def createApplication(self, dbPath = "train.sqlite"
               , trainLogFolderPath = "trainLog"
               , console_print = False):
        
        store = Store(dbPath, trainLogFolderPath)
        builder = ConcreteBuilder(store, logger = MyLogger(console_print = console_print))
        loader = ConcreteLoader(store)
        evaluationDb = ConcreteEvaluationDb(evaluationDbPath = "evaluationDb.sqlite", buildParameterFactory = ConcreteBuildParameterFactory())
        evaluationDb.initDb()
        
        return ConcreteApplication(builder, loader, evaluationDb, evaluator=SacEvaluator(simulatorFactory = ConcreteSimulatorFactoryForEvaluation(nSimulationStep=1)), showProgress = False, maxNumOfEvaluateAgents = None), store, evaluationDb
        
    def createConcreteEvaluationDb(self):
        return ConcreteEvaluationDb(evaluationDbPath = "test.sqlite")
    
    def createEvaluateMethods(self):
        return [SacEvaluateMethod(), SacEvaluateMethod(), ConcreteEvaluateMethod001(figFolderPath = self.figFolderPath, figSize=[8, 6]), ConcreteEvaluateMethod002(dataFolderPath = self.dataFolderPath)]
    
    def clean(self):
        
        if os.path.exists(self.figFolderPath):
            shutil.rmtree(self.figFolderPath)
            
        if os.path.exists(self.dataFolderPath):
            shutil.rmtree(self.dataFolderPath)