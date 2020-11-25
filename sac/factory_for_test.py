'''
Created on 2020/11/25

@author: ukai
'''
from sac.sac_agent import SacAgent
from sac.sac_batch_data_agent import SacBatchDataAgent
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from sac.sac_batch_data_reward import SacBatchDataReward
from sac.sac_environment import SacEnvironment
from sac.sac_feature_extractor import SacFeatureExtractor
from sac.sac_plant import SacPlant
from sac.sac_policy import SacPolicy
from sac.sac_replay_buffer import SacReplayBuffer
from sac.sac_trainer import SacTrainer
from sac.sac_value_function_approximator import SacValueFunctionApproximator


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
        return SacBatchDataAgent()
    
    def createBatchDataEnvironment(self):
        return SacBatchDataEnvironment()
    
    def createBatchDataReward(self):
        return SacBatchDataReward()
    
    def createPlant(self):
        return SacPlant()
    
    def createEnvironment(self):
        return SacEnvironment(self.createPlant())
    
    def createAgent(self):
        return SacAgent(policy = SacPolicy()
                     , valueFunctionApproximator = SacValueFunctionApproximator()
                     , featureExtractor = SacFeatureExtractor()
                     , discountFactor = self.discountFactor
                     , alphaTemp = self.alphaTemp)
        
    def createTrainer(self):
        return SacTrainer(agent = self.createAgent()
                       , environment = self.createEnvironment()
                       , replayBuffer = SacReplayBuffer(bufferSize = self.bufferSize)
                       , nStepEnvironment = self.nStepEnvironment
                       , nStepGradient = self.nStepGradient
                       , nIntervalUpdateStateValueFunction = self.nIntervalUpdateStateValueFunction)