'''
Created on 2020/11/15

@author: ukai
'''

from skeleton.abstract_agent import AbstractAgent
from concrete.concrete_policy import ConcretePolicy
from concrete.concrete_value_function_approximator import ConcreteValueFunctionApproximator
from concrete.concrete_feature_extractor import ConcreteFeatureExtractor


class ConcreteAgent(AbstractAgent):
    '''
    classdocs
    '''


    def __init__(self, policy, valueFunctionApproximator, featureExtractor):
        AbstractAgent.__init__(self, policy, valueFunctionApproximator, featureExtractor)
        
        assert isinstance(policy, ConcretePolicy)
        self.policy = policy
        
        assert isinstance(valueFunctionApproximator, ConcreteValueFunctionApproximator)
        self.valueFunctionApproximator = valueFunctionApproximator
        
        assert isinstance(featureExtractor, ConcreteFeatureExtractor)
        self.featureExtractor = featureExtractor
                
    def applyGradientsForUpdateActionValue(self, grads, trainableVariables):
        pass
    
    def applyGradientsForUpdatePolicy(self, grads, trainableVariables):
        pass
    
    def applyGradientsForUpdateStateValueFunction(self, grads, trainableVariables):
        pass
        
    def getGradientsForUpdateActionValue(self, batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep, trainableVariables):
        return None
    
    def getGradientsForUpdatePolicy(self, batchDataEnvironment, trainableVariables):
        return None
        
    def getGradientsForUpdateStateValueFunction(self, batchDataEnvironment, trainableVariables):
        return None
    
    def getErrForUpdateStateValueFunction(self, batchDataEnvironment):
        
        batchDataAgent = self.getAction(batchDataEnvironment)
        batchDataActionValueAveraged = self.valueFunctionApproximator.getAveragedActionValue(batchDataEnvironment, batchDataAgent)
        batchDataStateValue = self.valueFunctionApproximator.call(batchDataEnvironment, batchDataAgent = None)
                
        return batchDataStateValue.getValue() - batchDataActionValueAveraged.getValue()
