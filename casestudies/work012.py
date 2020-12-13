'''
Created on 2020/12/08

@author: ukai
'''


import numpy as np
from casestudies.work_template import WorkTemplate
from concrete.concrete_build_parameter import ConcreteBuildParameter
import itertools


class Work012(WorkTemplate):
    '''

    2020-12-13

    Examine the effect of various hyper parameters.
    Especially, check plant003, of which the cost is the violation of NH4 if NH4 is beyond the SV, otherwise DO,
    and check the buffer size.
    
    '''
    
    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath):
        WorkTemplate.__init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
        

    def generateBuildParameter(self):

        nEpoch = self.nEpoch
       
        for _ in range(self.nAgent):
            
            for plantClass in ["ConcretePlant003", "ConcretePlant004"]:
                
                yield ConcreteBuildParameter(nIntervalSave = nEpoch//(2**1)
                                    , nEpoch = nEpoch
                                    , label = self.workName
                                    , plantClass = plantClass
                                    , discountFactor = float(np.random.choice([1-1/2**2, 1-1/2**4])) # Q(s,a) = (1-gamma) * reward(s,a) + gamma * V(s+)
                                    , alphaTemp = float(np.random.choice([0., 1.,]))
                                    , saveFolderPathAgent = self.saveFolderPathAgent
                                    , nFeature = 1
                                    , nSampleOfActionsInValueFunctionApproximator = int(np.random.choice([2**0, 2**3,]))
                                    , nHiddenValueFunctionApproximator = 2**5
                                    , nStepEnvironment = 1
                                    , nStepGradient = int(np.random.choice([2**0, 2**3,]))
                                    , nIntervalUpdateStateValueFunction = int(np.random.choice([2**0, 2**3,]))
                                    , nIterationPerEpoch = 1
                                    , bufferSizeReplayBuffer = int(np.random.choice([2**10, 2**16,]))
                                    , featureExtractorClass = "ConcreteFeatureExtractor002"
                                    , learningRateForUpdateActionValueFunction = 1e-3
                                    , learningRateForUpdatePolicy = 1e-3
                                    , learningRateForUpdateStateValueFunction = float(np.random.choice([1e-4, 1e-3]))
                                    , policyClass = "ConcretePolicy002")
