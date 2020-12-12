'''
Created on 2020/12/08

@author: ukai
'''


import numpy as np
from casestudies.work_template import WorkTemplate
from concrete.concrete_build_parameter import ConcreteBuildParameter
import itertools


class Work008(WorkTemplate):
    '''

    2020-12-12

    To investigate the monotonous increase of agent's sd,
    set nStepGradient = 8 * 32 and learningRate = 1e-3/32
          
    '''
    
    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath):
        WorkTemplate.__init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
        

    def generateBuildParameter(self):

        nEpoch = self.nEpoch
        nStepGradient = 2**3
        nBatch = 2**5        
       
        for _ in range(self.nAgent):
            for alphaTemp in [0.0, 1.0]:
                yield ConcreteBuildParameter(nIntervalSave = nEpoch//(2**4)
                                        , nEpoch = nEpoch
                                        , label = self.workName
                                        , plantClass = "ConcretePlant004"
                                        , discountFactor = 0.75 # Q(s,a) = (1-gamma) * reward(s,a) + gamma * V(s+)
                                        , alphaTemp = alphaTemp
                                        , saveFolderPathAgent = self.saveFolderPathAgent
                                        , nFeature = 1
                                        , nSampleOfActionsInValueFunctionApproximator = int(np.random.choice([2**0,]))
                                        , nHiddenValueFunctionApproximator = 2**5
                                        , nStepEnvironment = 1
                                        , nStepGradient = nStepGradient * nBatch
                                        , nIntervalUpdateStateValueFunction = int(np.random.choice([2**0,]))
                                        , nIterationPerEpoch = 1
                                        , bufferSizeReplayBuffer = 2**10
                                        , featureExtractorClass = "ConcreteFeatureExtractor002"
                                        , learningRateForUpdateActionValueFunction = 1e-3/nBatch
                                        , learningRateForUpdatePolicy = 1e-3/nBatch
                                        , learningRateForUpdateStateValueFunction = float(np.random.choice([1e-4/nBatch,]))
                                        , policyClass = "ConcretePolicy002")
