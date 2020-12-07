'''
Created on 2020/12/07

@author: ukai
'''


import numpy as np
from casestudies.work_template import WorkTemplate
from concrete.concrete_build_parameter import ConcreteBuildParameter


class Work001(WorkTemplate):
    '''
    
    Work001 inspects the sensitivity of the reward to the following hyper parameters:
    
    * epoch
    * alphaTemp
    * nSampleOfActionsInValueFunctionApproximator
    * nStepGradient
    * nIntervalUpdateStateValueFunction
    * learningRateForUpdateStateValueFunction
    
    Note, it uses plant004, of which the cost is the summation of DO and the excess of NH4 over the threshold,  
    and the agent without any feature extractor, which means the feature is the PV.
    '''

    def generateBuildParameter(self):
        
        for _ in range(self.nAgent):
            yield ConcreteBuildParameter(nIntervalSave = self.nEpoch//2
                                            , nEpoch = self.nEpoch
                                            , label = self.workName
                                            , plantClass = "ConcretePlant004"
                                            , discountFactor = 0.9
                                            , alphaTemp = float(np.random.choice([1e-1, 1e+1]))
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
                                            , learningRateForUpdateStateValueFunction = float(np.random.choice([1e-3,])))
        