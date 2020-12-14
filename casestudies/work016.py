'''
Created on 2020/12/08

@author: ukai
'''


from casestudies.work_template import WorkTemplate
import numpy as np
from concrete.concrete_build_parameter import ConcreteBuildParameter


class Work016(WorkTemplate):
    '''

    2020-12-15

    Examine the stabilization by minibatch sampling.             
    
    '''
    
    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath):
        WorkTemplate.__init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
        

    def generateBuildParameter(self):

        nEpoch = self.nEpoch
       
        for _ in range(self.nAgent):
            
            
            plantClasses = ["ConcretePlant003", "ConcretePlant004"]
            plantClass = plantClasses[int(np.random.randint(len(plantClasses)))]
            
            nBatch = 2**5
            nStepGradient = 1
            learningRateForUpdateActionValueFunction = 1e-2/nStepGradient
            learningRateForUpdatePolicy = 1e-3/nStepGradient
            learningRateForUpdateStateValueFunction = 1e-2/nStepGradient
                
            yield ConcreteBuildParameter(nIntervalSave = nEpoch//(2**4)
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
                                , policyClass = "ConcretePolicy002"
                                , replayBufferClass = "ConcreteReplayBuffer001"
                                , nBatch = nBatch)
