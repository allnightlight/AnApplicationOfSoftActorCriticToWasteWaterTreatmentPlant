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
        
    def getAction(self, batchDataEnvironment):
        
        return self.policy.call(self.featureExtractor.call(batchDataEnvironment))
                
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
        batchDataAveragedActionValue = self.valueFunctionApproximator.getAveragedActionValue(self.featureExtractor.call(batchDataEnvironment), batchDataAgent)        
        batchDataStateValue = self.valueFunctionApproximator.getStateValue(self.featureExtractor.call(batchDataEnvironment))
                
        return (batchDataStateValue.getValue() - batchDataAveragedActionValue.getValue() - batchDataAgent.getEntropy())**2
            
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
        batchDataAveragedActionValue = self.valueFunctionApproximator.getAveragedActionValue(self.featureExtractor.call(batchDataEnvironment), batchDataAgent)
                
        return - batchDataAgent.getEntropy() - batchDataAveragedActionValue.getValue()
            
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
        
        batchDataActionValue = self.valueFunctionApproximator.getActionValue(self.featureExtractor.call(batchDataEnvironment), batchDataAgent)
        batchDataStateValueNext = self.valueFunctionApproximator.getStateValue(self.featureExtractor.call(batchDataEnvironmentNextStep))
        
        return (batchDataActionValue.getValue() - ((1-self.discountFactor) * batchDataReward.getValue() + self.discountFactor * batchDataStateValueNext.getValue()))**2