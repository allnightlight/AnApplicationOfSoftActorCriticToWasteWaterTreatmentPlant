'''
Created on 2020/11/15

@author: ukai
'''

from skeleton.abstract_agent import AbstractAgent


class ConcreteAgent(AbstractAgent):
    '''
    classdocs
    '''


    def __init__(self, policy, valueFunctionApproximator, featureExtractor):
        AbstractAgent.__init__(self, policy, valueFunctionApproximator, featureExtractor)
                
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