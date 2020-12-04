'''
Created on 2020/12/04

@author: ukai
'''

import numpy as np
from concrete.concrete_build_parameter import ConcreteBuildParameter
from sanitycheck.work004_evaluator import Work004Evaluator


evaluateMethods = [Work004Evaluator(),]

def generateBuildParameter(nAgent, nEpoch):
    
    for _ in range(nAgent):
        buildParameter = ConcreteBuildParameter(nIntervalSave = nEpoch//2
                                            , nEpoch = nEpoch
                                            , label = "caseStudy001"
                                            , plantClass = "ConcretePlant001"
                                            , discountFactor = 0.5
                                            , alphaTemp = float(np.random.choice([1e-1, 1e+1]))
                                            , saveFolderPathAgent = "checkpoint"
                                            , nFeature = 1
                                            , nSampleOfActionsInValueFunctionApproximator = int(np.random.choice([2**0, 2**3]))
                                            , nHiddenValueFunctionApproximator = 2**5
                                            , nStepEnvironment = int(np.random.choice([2**0, 2**3]))
                                            , nStepGradient = int(np.random.choice([2**0, 2**3]))
                                            , nIntervalUpdateStateValueFunction = int(np.random.choice([2**0, 2**3]))
                                            , nIterationPerEpoch = 1
                                            , bufferSizeReplayBuffer = 2**10
                                            , featureExtractorClass = "ConcreteFeatureExtractor002")
        
        yield buildParameter