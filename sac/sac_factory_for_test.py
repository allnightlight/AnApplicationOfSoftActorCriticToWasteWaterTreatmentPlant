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
from sac.sac_simulator import SacSimulator
from sac.sac_evaluator import SacEvaluator
from sac.sac_with_deterministic_action import SacSimulatorWithDeterministicAction
from sac.sac_with_stochastic_action import SacSimulatorWithStochasticAction
from sac.sac_simulator_factory import SacSimulatorFactory


class SacFactoryForTest(object):
    '''
    classdocs
    '''

    def __init__(self
            , nStepEnvironment = 2
            , nStepGradient = 1
            , nIntervalUpdateStateValueFunction = 1
            , bufferSize = 10
            , discountFactor = 0.99
            , alphaTemp = 1.0
            , updatePolicyByAdvantage = False
            , nIterationPerEpoch = 9
            , nSimulationStep = 10):

        self.nStepEnvironment = nStepEnvironment
        self.nStepGradient = nStepGradient
        self.nIntervalUpdateStateValueFunction = nIntervalUpdateStateValueFunction
        self.bufferSize = bufferSize
        self.alphaTemp = alphaTemp
        self.discountFactor = discountFactor
        self.updatePolicyByAdvantage = updatePolicyByAdvantage
        self.nIterationPerEpoch = nIterationPerEpoch
        self.nSimulationStep = nSimulationStep

    def createBatchDataAgent(self):
        return SacBatchDataAgent()
    
    def createBatchDataEnvironment(self):
        return SacBatchDataEnvironment()
    
    def createBatchDataReward(self):
        return SacBatchDataReward(1.23)
    
    def createPlant(self):
        return SacPlant()
    
    def createEnvironment(self):
        return SacEnvironment(self.createPlant())
    
    def createAgent(self):
        return SacAgent(policy = SacPolicy()
                     , valueFunctionApproximator = SacValueFunctionApproximator()
                     , featureExtractor = SacFeatureExtractor()
                     , discountFactor = self.discountFactor
                     , alphaTemp = self.alphaTemp
                     , updatePolicyByAdvantage = self.updatePolicyByAdvantage)
        
    def createTrainer(self):
        return SacTrainer(agent = self.createAgent()
                       , environment = self.createEnvironment()
                       , replayBuffer = SacReplayBuffer(bufferSize = self.bufferSize)
                       , simulatorFactory = SacSimulatorFactory()
                       , nStepEnvironment = self.nStepEnvironment
                       , nStepGradient = self.nStepGradient
                       , nIntervalUpdateStateValueFunction = self.nIntervalUpdateStateValueFunction
                       , nIterationPerEpoch = self.nIterationPerEpoch)
        
    def generateSimulator(self):
        yield SacSimulatorWithDeterministicAction(agent = self.createAgent()
                                                   , environment = self.createEnvironment()
                                                   , nSimulationStep = self.nSimulationStep)
        
        yield SacSimulatorWithStochasticAction(agent = self.createAgent()
                                                   , environment = self.createEnvironment()
                                                   , nSimulationStep = self.nSimulationStep)

    def createEvaluator(self):
        return SacEvaluator()
    
    def createSimulatorFactory(self):
        
        return SacSimulatorFactory()