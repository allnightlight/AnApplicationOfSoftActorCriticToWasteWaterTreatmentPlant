'''
Created on 2020/12/08

@author: ukai
'''


import numpy as np
from casestudies.work_template import WorkTemplate
from concrete.concrete_build_parameter import ConcreteBuildParameter
import itertools


class Work901(WorkTemplate):
    '''

    2020-12-10
    To debug SAC algorithm, 
        learn agents with gamma = 1 and nIntervalUpdateValuefunction = infinity, which means skip updating state value function,
        and alphaTemp = 0, which means policy is allowed to seek for maximizing only action value(in this case, just reward), ignoring entropy.
    Learning rate configuration:
        for action value: 1e-3(fair)
        for policy: 1e-4(slow)    
    '''
    
    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath):
        WorkTemplate.__init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
        

    def generateBuildParameter(self):

        nEpoch = self.nEpoch        
        nIntervalUpdateStateValueFunction = nEpoch + 1
       
        for _ in range(self.nAgent):
            
            yield ConcreteBuildParameter(nIntervalSave = nEpoch//2
                                            , nEpoch = nEpoch
                                            , label = self.workName
                                            , plantClass = "ConcretePlant001"
                                            , discountFactor = 1.
                                            , alphaTemp = float(np.random.choice([0.0,]))
                                            , saveFolderPathAgent = self.saveFolderPathAgent
                                            , nFeature = 1
                                            , nSampleOfActionsInValueFunctionApproximator = int(np.random.choice([2**0, 2**3]))
                                            , nHiddenValueFunctionApproximator = 2**5
                                            , nStepEnvironment = 1
                                            , nStepGradient = int(np.random.choice([2**0, 2**3]))
                                            , nIntervalUpdateStateValueFunction = nIntervalUpdateStateValueFunction
                                            , nIterationPerEpoch = 1
                                            , bufferSizeReplayBuffer = 2**10
                                            , featureExtractorClass = "ConcreteFeatureExtractor002"
                                            , learningRateForUpdateActionValueFunction = 1e-3
                                            , learningRateForUpdatePolicy = 1e-4
                                            , learningRateForUpdateStateValueFunction = float(np.random.choice([1e-3, 1e-4])))
        
