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


    def __init__(self, policy, valueFunctionApproximator, featureExtractor, discountFactor):
        
        assert isinstance(policy, AbstractPolicy)        
        self.policy = policy
        
        assert isinstance(valueFunctionApproximator, AbstractValueFunctionApproximator)
        self.valueFunctionApproximator = valueFunctionApproximator
        
        assert isinstance(featureExtractor, AbstractFeatureExtractor)
        self.featureExtractor = featureExtractor
        
        self.discountFactor = discountFactor
                
    def reset(self):
        pass
    
    def getFeature(self, batchDataEnvironment):
        
        return self.featureExtractor.call(batchDataEnvironment)
    
    def getAction(self, batchDataEnvironment):
        
        return self.policy.call(self.getFeature(batchDataEnvironment))
        
    def getStateValue(self, batchDataEnvironment):
        
        return self.valueFunctionApproximator.getStateValue(self.getFeature(batchDataEnvironment))
    
    def getActionValue(self, batchDataEnvironment, batchDataAgent):
        
        return self.valueFunctionApproximator.getActionValue(self.getFeature(batchDataEnvironment), batchDataAgent)
    
    def getAveragedActionValue(self, batchDataEnvironment, batchDataAgent):
        
        return self.valueFunctionApproximator.getAveragedActionValue(self.getFeature(batchDataEnvironment), batchDataAgent)
        
    # <<protected, abstract>>
    def applyGradientSomeoneToReduce(self, fh, trainableVariables, optimizer):
        # with tensorflow.Gtape() as tape:
        #     loss = tf.reduce_mean(fh())
        # grad = tape.gradient(losss, trainableVariables)
        # opt.apply_gradient(zip(grad, trainableVariables))
        fh()
        pass
        
    # <<public, final>>
    def updateStateValueFunction(self, batchDataEnvironment):
        
        self.applyGradientSomeoneToReduce(
            fh = lambda : self.getErrForUpdateStateValueFunction(batchDataEnvironment)
            , trainableVariables = self.getTrainableVariablesForUpdateStateValueFunction()
            , optimizer = self.getOptimizerForUpdateStateValueFunction())

    # << protected, abstract>>
    def getOptimizerForUpdateStateValueFunction(self):
        return None
    
    # <<protected, abstract>>
    def getTrainableVariablesForUpdateStateValueFunction(self):
        return None
        
    # <<private, final>>
    def getErrForUpdateStateValueFunction(self, batchDataEnvironment):
        
        batchDataAgent = self.getAction(batchDataEnvironment)
        batchDataAveragedActionValue= self.getAveragedActionValue(batchDataEnvironment, batchDataAgent)        
        batchDataStateValue = self.getStateValue(batchDataEnvironment)
                
        return batchDataStateValue.getValue() - batchDataAveragedActionValue.getValue()
            
    # <<public, final>>
    def updatePolicy(self, batchDataEnvironment):
        
        self.applyGradientSomeoneToReduce(
            fh = lambda : self.getErrForUpdatePolicy(batchDataEnvironment)
            , trainableVariables = self.getTrainableVariablesForUpdatePolicy()
            , optimizer = self.getOptimizerForUpdatePolicy())

    # << protected, abstract>>
    def getOptimizerForUpdatePolicy(self):
        return None
    
    # <<protected, abstract>>
    def getTrainableVariablesForUpdatePolicy(self):
        return None
    
    # <<private, final>>
    def getErrForUpdatePolicy(self, batchDataEnvironment):
        
        batchDataAgent = self.getAction(batchDataEnvironment)
        _Entropy = batchDataAgent.getEntropy()
        batchDataAveragedActionValue = self.getAveragedActionValue(batchDataEnvironment, batchDataAgent)
                
        return -_Entropy - batchDataAveragedActionValue.getValue()
            
    # <<public>>
    def updateActionValueFunction(self, batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep):
        
        self.applyGradientSomeoneToReduce(
            fh = lambda : self.getErrForUpdateActionValueFunction(batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep)
            , trainableVariables = self.getTrainableVariablesForUpdateActionValueFunction()
            , optimizer = self.getOptimizerForUpdateStateValueFunction())

    # << protected, abstract>>
    def getOptimizerForUpdateActionValueFunction(self):
        return None
        
    # <<protected, abstract>>
    def getTrainableVariablesForUpdateActionValueFunction(self):
        return None

    # <<private, final>>
    def getErrForUpdateActionValueFunction(self, batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep):
        
        batchDataActionValue = self.getActionValue(batchDataEnvironment, batchDataAgent)
        batchDataStateValueNext = self.getStateValue(batchDataEnvironmentNextStep)
        
        return batchDataActionValue.getValue() - ((1-self.discountFactor) * batchDataReward.getValue() + self.discountFactor * batchDataStateValueNext.getValue())