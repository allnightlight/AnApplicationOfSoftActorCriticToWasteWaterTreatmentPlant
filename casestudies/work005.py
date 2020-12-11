'''
Created on 2020/12/08

@author: ukai
'''


import numpy as np
from casestudies.work_template import WorkTemplate
from concrete.concrete_build_parameter import ConcreteBuildParameter
import itertools


class Work005(WorkTemplate):
    '''

    2020-12-11

    Work005 has the same configuration to the one of Work004 except policyClass.
    
    Here, compare the performance between agents with policyClass = "ConcretePolicy001", which has been already examined
    and agents with policyClass = "ConcretePolicy002", which are implemented in this work. 
          
    '''
    
    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath):
        WorkTemplate.__init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
        

    def generateBuildParameter(self):

        nEpoch = self.nEpoch        
       
        for _ in range(self.nAgent):
                            
            yield ConcreteBuildParameter(nIntervalSave = nEpoch//2
                                        , nEpoch = nEpoch
                                        , label = self.workName
                                        , plantClass = "ConcretePlant004"
                                        , discountFactor = 0.75 # Q(s,a) = (1-gamma) * reward(s,a) + gamma * V(s+)
                                        , alphaTemp = float(np.random.choice([0.0,]))
                                        , saveFolderPathAgent = self.saveFolderPathAgent
                                        , nFeature = 1
                                        , nSampleOfActionsInValueFunctionApproximator = int(np.random.choice([2**0, 2**3]))
                                        , nHiddenValueFunctionApproximator = 2**5
                                        , nStepEnvironment = 1
                                        , nStepGradient = int(np.random.choice([2**0, 2**3]))
                                        , nIntervalUpdateStateValueFunction = int(np.random.choice([2**0, 2**3]))
                                        , nIterationPerEpoch = 1
                                        , bufferSizeReplayBuffer = 2**10
                                        , featureExtractorClass = "ConcreteFeatureExtractor002"
                                        , learningRateForUpdateActionValueFunction = 1e-3
                                        , learningRateForUpdatePolicy = 1e-3
                                        , learningRateForUpdateStateValueFunction = float(np.random.choice([1e-3, 1e-4]))
                                        , policyClass = "ConcretePolicy002")
