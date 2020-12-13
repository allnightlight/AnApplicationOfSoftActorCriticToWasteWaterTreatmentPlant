'''
Created on 2020/12/08

@author: ukai
'''


from casestudies.work_template import WorkTemplate
import numpy as np
from concrete.concrete_build_parameter import ConcreteBuildParameter


class Work013(WorkTemplate):
    '''

    2020-12-14

    Examine the effects of the following parameters:
    learning rates(for policy, state value function and action value function)
    nStepGradient
    
    Note, all the learning rate are normalized by nStepGradient, 
    more preciesely say, 
    if lr = 1e-3 and nStepGradinet = 10,
    then actual learning rate is lr / nStepGradient = 1e-3.
    
    '''
    
    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath):
        WorkTemplate.__init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
        

    def generateBuildParameter(self):

        nEpoch = self.nEpoch
       
        for _ in range(self.nAgent):
            
            plantClass = "ConcretePlant004"
            
            nStepGradient = int(np.random.choice([1, 10]))
            learningRateForUpdateActionValueFunction = float(np.random.choice([1e-2, 1e-3]))/nStepGradient
            learningRateForUpdatePolicy = float(np.random.choice([1e-2, 1e-3]))/nStepGradient
            learningRateForUpdateStateValueFunction = float(np.random.choice([1e-2, 1e-3]))/nStepGradient
                
            yield ConcreteBuildParameter(nIntervalSave = nEpoch//(2**1)
                                , nEpoch = nEpoch
                                , label = self.workName
                                , plantClass = plantClass
                                , discountFactor = float(np.random.choice([0.99,])) # Q(s,a) = (1-gamma) * reward(s,a) + gamma * V(s+)
                                , alphaTemp = float(np.random.choice([0.,]))
                                , saveFolderPathAgent = self.saveFolderPathAgent
                                , nFeature = 1
                                , nSampleOfActionsInValueFunctionApproximator = int(np.random.choice([2**0,]))
                                , nHiddenValueFunctionApproximator = 2**5
                                , nStepEnvironment = 1
                                , nStepGradient = nStepGradient
                                , nIntervalUpdateStateValueFunction = int(np.random.choice([2**0,]))
                                , nIterationPerEpoch = 1
                                , bufferSizeReplayBuffer = int(np.random.choice([2**16,]))
                                , featureExtractorClass = "ConcreteFeatureExtractor002"
                                , learningRateForUpdateActionValueFunction = learningRateForUpdateActionValueFunction 
                                , learningRateForUpdatePolicy = learningRateForUpdatePolicy
                                , learningRateForUpdateStateValueFunction = learningRateForUpdateStateValueFunction
                                , policyClass = "ConcretePolicy002")
