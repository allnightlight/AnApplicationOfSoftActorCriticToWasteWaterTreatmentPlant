'''
Created on 2020/12/08

@author: ukai
'''


import numpy as np
from casestudies.work_template import WorkTemplate
from concrete.concrete_build_parameter import ConcreteBuildParameter
import itertools


class Work011(WorkTemplate):
    '''

    2020-12-13

    To train agents by mini-batch sampling,
    test with the following configuration:
        nBatch = 1, 32
        nStepGradient = 1
        alphaTemp = 1e-2, 1.0
    the parameters other than the above ones are same with the ones of work007.
          
    '''
    
    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath):
        WorkTemplate.__init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
        

    def generateBuildParameter(self):

        nEpoch = self.nEpoch
        nStepGradient = 2**0
       
        for _ in range(self.nAgent):
            for nBatch, alphaTemp in itertools.product((2**0, 2**5), (1e-2, 1.0)):
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
                                        , nStepGradient = nStepGradient
                                        , nIntervalUpdateStateValueFunction = int(np.random.choice([2**0,]))
                                        , nIterationPerEpoch = 1
                                        , bufferSizeReplayBuffer = 2**10
                                        , featureExtractorClass = "ConcreteFeatureExtractor002"
                                        , learningRateForUpdateActionValueFunction = 1e-3
                                        , learningRateForUpdatePolicy = 1e-3
                                        , learningRateForUpdateStateValueFunction = float(np.random.choice([1e-4,]))
                                        , policyClass = "ConcretePolicy002"
                                        , nBatch = nBatch
                                        , replayBufferClass = "ConcreteReplayBuffer001")
