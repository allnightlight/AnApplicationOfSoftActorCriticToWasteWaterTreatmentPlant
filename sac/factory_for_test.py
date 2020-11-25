'''
Created on 2020/11/25

@author: ukai
'''
from skeleton.abstract_agent import AbstractAgent
from skeleton.abstract_batch_data_agent import AbstractBatchDataAgent
from skeleton.abstract_batch_data_environment import AbstractBatchDataEnvironment
from skeleton.abstract_batch_data_reward import AbstractBatchDataReward
from skeleton.abstract_environment import AbstractEnvironment
from skeleton.abstract_feature_extractor import AbstractFeatureExtractor
from skeleton.abstract_plant import AbstractPlant
from skeleton.abstract_policy import AbstractPolicy
from skeleton.abstract_replay_buffer import AbstractReplayBuffer
from skeleton.abstract_trainer import AbstractTrainer
from skeleton.abstract_value_function_approximator import AbstractValueFunctionApproximator


class FactoryForTest(object):
    '''
    classdocs
    '''

    def __init__(self
            , nStepEnvironment = 1
            , nStepGradient = 1
            , nIntervalUpdateStateValueFunction = 1
            , bufferSize = 10
            , discountFactor = 0.99
            , alphaTemp = 1.0):

        self.nStepEnvironment = nStepEnvironment
        self.nStepGradient = nStepGradient
        self.nIntervalUpdateStateValueFunction = nIntervalUpdateStateValueFunction
        self.bufferSize = bufferSize
        self.alphaTemp = alphaTemp
        self.discountFactor = discountFactor

    def createBatchDataAgent(self):
        return AbstractBatchDataAgent()
    
    def createBatchDataEnvironment(self):
        return AbstractBatchDataEnvironment()
    
    def createBatchDataReward(self):
        return AbstractBatchDataReward()
    
    def createPlant(self):
        return AbstractPlant()
    
    def createEnvironment(self):
        return AbstractEnvironment(self.createPlant())
    
    def createAgent(self):
        return AbstractAgent(policy = AbstractPolicy()
                     , valueFunctionApproximator = AbstractValueFunctionApproximator()
                     , featureExtractor = AbstractFeatureExtractor()
                     , discountFactor = self.discountFactor
                     , alphaTemp = self.alphaTemp)
        
    def createTrainer(self):
        return AbstractTrainer(agent = self.createAgent()
                       , environment = self.createEnvironment()
                       , replayBuffer = AbstractReplayBuffer(bufferSize = self.bufferSize)
                       , nStepEnvironment = self.nStepEnvironment
                       , nStepGradient = self.nStepGradient
                       , nIntervalUpdateStateValueFunction = self.nIntervalUpdateStateValueFunction)