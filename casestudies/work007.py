'''
Created on 2020/12/08

@author: ukai
'''


import numpy as np
from casestudies.work_template import WorkTemplate
from concrete.concrete_build_parameter import ConcreteBuildParameter
import itertools


class Work007(WorkTemplate):
    '''

    2020-12-12

    To compare learning curves with various options of alphaTemp,  
    this work periodically saves trained agents over the training.
    
    Seeing from the result of work006,
    nStepGradient = 2**3 and nEpoch = 2**10 
    are enough to converge.      
          
    '''
    
    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath):
        WorkTemplate.__init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
        

    def generateBuildParameter(self):

        nEpoch = self.nEpoch
        nStepGradient = 2**3        
       
        for _ in range(self.nAgent):
            for alphaTemp in [1e-2, 1e-1, 1, 10]:
                yield ConcreteBuildParameter(nIntervalSave = nEpoch//(2**4)
                                        , nEpoch = nEpoch
                                        , label = self.workName
                                        , plantClass = "ConcretePlant004"
                                        , discountFactor = 0.75 # Q(s,a) = (1-gamma) * reward(s,a) + gamma * V(s+)
                                        , alphaTemp = float(np.random.choice([0.0,]))
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
