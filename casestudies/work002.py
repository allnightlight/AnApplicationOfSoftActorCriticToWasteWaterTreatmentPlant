'''
Created on 2020/12/08

@author: ukai
'''


import numpy as np
from casestudies.work_template import WorkTemplate
from concrete.concrete_build_parameter import ConcreteBuildParameter
import itertools


class Work002(WorkTemplate):
    '''
    
    Work002 examines how the learning curve over epoch can vary against the following hyper parameters:
    
    * alphaTemp
    * nStepGradient
    
    Note, it uses plant004, of which the cost is the summation of DO and the excess of NH4 beyond the threshold,  
    and the agent without any feature extractor, which means the feature is the PV.
    '''
    
    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath, nSampleOverLearningCurve):
        WorkTemplate.__init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
        
        self.nSampleOverLearningCurve = nSampleOverLearningCurve

    def generateBuildParameter(self):
        
        for _ in range(self.nAgent):
            
            for alphaTemp, nStepGradient in itertools.product([1e-1, 1e+1], [2**0, 2**3]):
            
                yield ConcreteBuildParameter(nIntervalSave = self.nEpoch//self.nSampleOverLearningCurve
                                                , nEpoch = self.nEpoch
                                                , label = self.workName
                                                , plantClass = "ConcretePlant004"
                                                , discountFactor = 0.9
                                                , alphaTemp = alphaTemp
                                                , saveFolderPathAgent = self.saveFolderPathAgent
                                                , nFeature = 1
                                                , nSampleOfActionsInValueFunctionApproximator = int(np.random.choice([2**3,]))
                                                , nHiddenValueFunctionApproximator = 2**5
                                                , nStepEnvironment = 1
                                                , nStepGradient = nStepGradient
                                                , nIntervalUpdateStateValueFunction = int(np.random.choice([2**3,]))
                                                , nIterationPerEpoch = 1
                                                , bufferSizeReplayBuffer = 2**10
                                                , featureExtractorClass = "ConcreteFeatureExtractor002"
                                                , learningRateForUpdateActionValueFunction = 1e-3
                                                , learningRateForUpdatePolicy = 1e-3
                                                , learningRateForUpdateStateValueFunction = float(np.random.choice([1e-3,])))
