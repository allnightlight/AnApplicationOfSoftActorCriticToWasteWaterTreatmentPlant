'''
Created on 2020/11/10

@author: ukai
'''
from skeleton.abstract_policy import AbstractPolicy
from skeleton.abstract_value_function_approximator import AbstractValueFunctionApproximator
from skeleton.abstract_feature_extractor import AbstractFeatureExtractor

class AbstractAgent(object):
    '''
    classdocs
    '''


    def __init__(self, policy, valueFunctionApproximator, featureExtractor):
        
        assert isinstance(policy, AbstractPolicy)        
        self.policy = policy
        
        assert isinstance(valueFunctionApproximator, AbstractValueFunctionApproximator)
        self.valueFunctionApproximator = valueFunctionApproximator
        
        assert isinstance(featureExtractor, AbstractFeatureExtractor)
        self.featureExtractor = featureExtractor
                
    def getFeature(self, batchDataEnvironment):
        
        return self.featureExtractor.call(batchDataEnvironment)
    
    def getAction(self, batchDataEnvironment):
        
        return self.policy.call(self.getFeature(batchDataEnvironment))
        
    def getStateValue(self, batchDataEnvironment):
        
        return self.valueFunctionApproximator.call(self.getFeature(batchDataEnvironment), batchDataAgent = None)
    
    def getActionValue(self, batchDataEnvironment, batchDataAgent):
        
        return self.valueFunctionApproximator.call(self.getFeature(batchDataEnvironment), batchDataAgent)
    
    def getSampleAveragedActionValue(self, batchDataEnvironment, batchDataAgent, nSampleOfActionInStateValueFunctionUpdate):

        assert nSampleOfActionInStateValueFunctionUpdate == 1
        
        return self.valueFunctionApproximator.call(self.getFeature(batchDataEnvironment), batchDataAgent)

    def getTrainableVariables(self):
        return None
    
    # <<public>>
    def updateStateValueFunction(self, batchDataEnvironment):
        trainableVariables = self.getTrainableVariables()
        self.applyGradientsForUpdateStateValueFunction(grads = self.getGradientsForUpdateStateValueFunction(batchDataEnvironment, trainableVariables)
                                                       , trainableVariables = trainableVariables)
    
    # <<protected>>
    def applyGradientsForUpdateStateValueFunction(self, grads, trainableVariables):
        pass
    
    # <<protected>>
    def getGradientsForUpdateStateValueFunction(self, batchDataEnvironment, trainableVariables):
        return None
        
        # <<public>>
    def updatePolicy(self, batchDataEnvironment):
        trainableVariables = self.getTrainableVariables()
        self.applyGradientsForUpdatePolicy(grads = self.getGradientsForUpdatePolicy(batchDataEnvironment, trainableVariables)
                                                       , trainableVariables = trainableVariables)
    
    # <<protected>>
    def applyGradientsForUpdatePolicy(self, grads, trainableVariables):
        pass
    
    # <<protected>>
    def getGradientsForUpdatePolicy(self, batchDataEnvironment, trainableVariables):
        return None
        
    # <<public>>
    def updateActionValue(self, batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep):
        trainableVariables = self.getTrainableVariables()
        self.applyGradientsForUpdateActionValue(grads = self.getGradientsForUpdateActionValue(batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep, trainableVariables)
                                                       , trainableVariables = trainableVariables)
    
    # <<protected>>
    def applyGradientsForUpdateActionValue(self, grads, trainableVariables):
        pass
    
    # <<protected>>
    def getGradientsForUpdateActionValue(self, batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep, trainableVariables):
        return None