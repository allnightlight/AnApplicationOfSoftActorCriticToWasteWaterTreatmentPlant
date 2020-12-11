'''
Created on 2020/12/08

@author: ukai
'''


import numpy as np
from casestudies.work_template import WorkTemplate
from concrete.concrete_build_parameter import ConcreteBuildParameter
import itertools


class Work907(WorkTemplate):
    '''

    2020-12-11
    
    This configuration examines the standard deviation(sd) of agent's output.
    
    For Policy002, it's expected to have moderate sd 
    because Policy002 is supposed to serve for limiting the sd into a bounded range
    even when alphaTemp has a large number.    
    
    '''
    
    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath):
        WorkTemplate.__init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
        

    def generateBuildParameter(self):

        nEpoch = self.nEpoch        
        nIntervalUpdateStateValueFunction = nEpoch + 1
       
        for _ in range(self.nAgent):
            
            for alphaTemp, policyClass in itertools.product([0.0, 1e+2,], ["ConcretePolicy001", "ConcretePolicy002"]):
                yield ConcreteBuildParameter(nIntervalSave = nEpoch//2
                                            , nEpoch = nEpoch
                                            , label = self.workName
                                            , plantClass = "ConcretePlant001"
                                            , discountFactor = 0. # Q(s,a) = (1-gamma) * r(s,a) + gamma * V(s+)
                                            , alphaTemp = alphaTemp
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
                                            , learningRateForUpdatePolicy = 1e-3
                                            , learningRateForUpdateStateValueFunction = float(np.random.choice([1e-3, 1e-4]))
                                            , policyClass = policyClass)