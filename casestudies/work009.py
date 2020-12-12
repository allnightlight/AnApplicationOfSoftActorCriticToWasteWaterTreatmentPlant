'''
Created on 2020/12/08

@author: ukai
'''


import numpy as np
from casestudies.work_template import WorkTemplate
from concrete.concrete_build_parameter import ConcreteBuildParameter
import itertools


class Work009(WorkTemplate):
    '''

    2020-12-12

    To verify the effect of gamma, 
    compares learning curves trained with gamma chosen from {1-1/2**1, 1-1/2**4, 1-1/2**7} and with alpha = 0.0.
    
    The hyper parameters other than gamma and alpha have the same values in  work007.
              
    '''
    
    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath):
        WorkTemplate.__init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
        

    def generateBuildParameter(self):

        nEpoch = self.nEpoch
        nStepGradient = 2**3        
        alphaTemp = 0.0
       
        for _ in range(self.nAgent):
            for discountFactor in [1-1/2**1, 1-1/2**4, 1-1/2**7]:
                yield ConcreteBuildParameter(nIntervalSave = nEpoch//(2**4)
                                        , nEpoch = nEpoch
                                        , label = self.workName
                                        , plantClass = "ConcretePlant004"
                                        , discountFactor = discountFactor # Q(s,a) = (1-gamma) * reward(s,a) + gamma * V(s+)
                                        , alphaTemp = alphaTemp
                                        , saveFolderPathAgent = self.saveFolderPathAgent
                                        , nFeature = 1
                                        , nSampleOfActionsInValueFunctionApproximator = int(np.random.choice([2**0,]))
                                        , nHiddenValueFunctionApproximator = 2**5
                                        , nStepEnvironment = 1
                                        , nStepGradient = nStepGradient
                                        , nIntervalUpdateStateValueFunction = int(np.random.choice([2**0,]))
                                        , nIterationPerEpoch = 1
                                        , bufferSizeReplayBuffer = 2**10
                                        , featureExtractorClass = "ConcreteFeatureExtractor002"
                                        , learningRateForUpdateActionValueFunction = 1e-3
                                        , learningRateForUpdatePolicy = 1e-3
                                        , learningRateForUpdateStateValueFunction = float(np.random.choice([1e-4,]))
                                        , policyClass = "ConcretePolicy002")
