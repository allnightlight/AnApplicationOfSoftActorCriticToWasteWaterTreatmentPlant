'''
Created on 2020/12/08

@author: ukai
'''


from casestudies.work_template import WorkTemplate
import numpy as np
from concrete.concrete_build_parameter import ConcreteBuildParameter


class Work020(WorkTemplate):
    '''

    2020-12-18

    To draw learning curves depending on alphaTemp,
    build agents with weightOnMv = 0.5.
    
    '''
    
    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath):
        WorkTemplate.__init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
        

    def generateBuildParameter(self):

        nEpoch = self.nEpoch
       
        for _ in range(self.nAgent):
                        
            plantClasses = ["ConcretePlant003",]
            plantClass = plantClasses[int(np.random.randint(len(plantClasses)))]
            
            policyClasses = ["ConcretePolicy001",]
            policyClass = policyClasses[int(np.random.randint(len(policyClasses)))]
            
            nQfunctionRedundancy = int(np.random.choice([2,]))
            
            nBatch = 2**5
            nStepGradient = 1
            learningRateForUpdatePolicy = float(np.random.choice([1e-2,]))/nStepGradient
            learningRateForUpdateActionValueFunction = float(np.random.choice([1e-2,]))/nStepGradient
            learningRateForUpdateStateValueFunction = float(np.random.choice([1e-3,]))/nStepGradient
            alphaTemp = float(np.random.choice([0., 0.1, 0.5,]))
            weightOnMv = float(np.random.choice([0.5,]))
                
            yield ConcreteBuildParameter(nIntervalSave = nEpoch//(2**4)
                                , nEpoch = nEpoch
                                , label = self.workName
                                , plantClass = plantClass
                                , discountFactor = float(np.random.choice([0.99,])) # Q(s,a) = (1-gamma) * reward(s,a) + gamma * V(s+)
                                , alphaTemp = alphaTemp
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
                                , policyClass = policyClass
                                , replayBufferClass = "ConcreteReplayBuffer001"
                                , nBatch = nBatch
                                , nQfunctionRedundancy = nQfunctionRedundancy
                                , valueFunctionApproximatorClass = "ConcreteValueFunctionApproximator002"
                                , weightOnMv = weightOnMv)