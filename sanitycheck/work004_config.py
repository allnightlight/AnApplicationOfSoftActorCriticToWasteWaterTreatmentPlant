'''
Created on 2020/12/04

@author: ukai
'''

import numpy as np
from concrete.concrete_build_parameter import ConcreteBuildParameter
from sanitycheck.work004_evaluator import Work004Evaluator

# the maximum number of agents to train in a build
nAgent = 2**10

# the number of epochs of training
nEpoch = 2**11

# the length of simulation period in a evaluation
nSimulationStep = 2**7

buildParameterLabel = "CaseStudy2020_1205_1523"

evaluateMethods = [Work004Evaluator(),]

def generateBuildParameter():
    
    for _ in range(nAgent):
        buildParameter = ConcreteBuildParameter(nIntervalSave = nEpoch//2
                                            , nEpoch = nEpoch
                                            , label = buildParameterLabel
                                            , plantClass = "ConcretePlant003"
                                            , discountFactor = 0.9
                                            , alphaTemp = float(np.random.choice([1e-1, 1e+1]))
                                            , saveFolderPathAgent = "checkpoint"
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
                                            , learningRateForUpdateStateValueFunction = float(np.random.choice([1e-3, 1e-4])))
        
        yield buildParameter