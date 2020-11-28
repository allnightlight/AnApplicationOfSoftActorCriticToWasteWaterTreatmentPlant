'''
Created on 2020/11/28

@author: ukai
'''
from framework.build_parameter import BuildParameter

class ConcreteBuildParameter(BuildParameter):
    '''
    classdocs
    '''


    def __init__(self
                 , nIntervalSave=2 ** 4
                 , nEpoch=2 ** 8
                 , label="None"
                 , plantClass = "ConcretePlant001"        
                 , discountFactor = 0.9
                 , alphaTemp = 1.0
                 , saveFolderPathAgent = "checkpoint"
                 , nFeature = 2**3
                 , nSampleOfActionsInValueFunctionApproximator = 2**2
                 , nHiddenFeatureExtractor = 2**5
                 , nStepEnvironment = 1
                 , nStepGradient = 2**5
                 , nIntervalUpdateStateValueFunction = 1
                 , nIterationPerEpoch = 2**7
                 , bufferSizeReplayBuffer = 2**10):
        
        BuildParameter.__init__(self, nIntervalSave=nIntervalSave, nEpoch=nEpoch, label=label)
        
        self.plantClass = plantClass
        self.discountFactor = discountFactor
        self.alphaTemp = alphaTemp
        self.saveFolderPathAgent = saveFolderPathAgent
        self.nFeature = nFeature
        self.nSampleOfActionsInValueFunctionApproximator = nSampleOfActionsInValueFunctionApproximator
        self.nHiddenFeatureExtractor = nHiddenFeatureExtractor        
        self.nStepEnvironment = nStepEnvironment
        self.nStepGradient = nStepGradient
        self.nIntervalUpdateStateValueFunction = nIntervalUpdateStateValueFunction
        self.nIterationPerEpoch = nIterationPerEpoch
        self.bufferSizeReplayBuffer = bufferSizeReplayBuffer
