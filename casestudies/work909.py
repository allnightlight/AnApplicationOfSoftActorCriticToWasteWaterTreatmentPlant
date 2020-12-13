'''
Created on 2020/12/08

@author: ukai
'''


import numpy as np
from casestudies.work_template import WorkTemplate
from concrete.concrete_build_parameter import ConcreteBuildParameter
import itertools


class Work909(WorkTemplate):
    '''

    2020-12-13

    To check the control performance with mini-batch sampling,
    
    '''
    
    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath):
        WorkTemplate.__init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
        

    def generateBuildParameter(self):

        nEpoch = self.nEpoch        
       
        for _ in range(self.nAgent):
                                
            for nBatch, replayBufferClass in [
                (None, "SacReplayBuffer")
                , (2**0, "ConcreteReplayBuffer001")
                , (2**5, "ConcreteReplayBuffer001")]:
                
                yield ConcreteBuildParameter(nIntervalSave = nEpoch//2
                                            , nEpoch = nEpoch
                                            , label = self.workName
                                            , plantClass = "ConcretePlant001"
                                            , discountFactor = 0.9 # Q(s,a) = (1-gamma) * reward(s,a) + gamma * V(s+)
                                            , alphaTemp = 1.0
                                            , saveFolderPathAgent = self.saveFolderPathAgent
                                            , nFeature = 1
                                            , nSampleOfActionsInValueFunctionApproximator = int(np.random.choice([2**0,]))
                                            , nHiddenValueFunctionApproximator = 2**5
                                            , nStepEnvironment = 1
                                            , nStepGradient = int(np.random.choice([2**3,]))
                                            , nIntervalUpdateStateValueFunction = int(np.random.choice([2**0,]))
                                            , nIterationPerEpoch = 1
                                            , bufferSizeReplayBuffer = 2**10
                                            , featureExtractorClass = "ConcreteFeatureExtractor002"
                                            , learningRateForUpdateActionValueFunction = 1e-3
                                            , learningRateForUpdatePolicy = 1e-3
                                            , learningRateForUpdateStateValueFunction = float(np.random.choice([1e-4,]))
                                            , policyClass = "ConcretePolicy002"
                                            , replayBufferClass = replayBufferClass
                                            , nBatch = nBatch)
