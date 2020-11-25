'''
Created on 2020/11/15

@author: ukai
'''

from sac.sac_agent import SacAgent
from concrete.concrete_policy import ConcretePolicy
from concrete.concrete_value_function_approximator import ConcreteValueFunctionApproximator
from concrete.concrete_feature_extractor import ConcreteFeatureExtractor
import tensorflow


class ConcreteAgent(SacAgent):
    '''
    classdocs
    '''


    def __init__(self, policy, valueFunctionApproximator, featureExtractor, discountFactor, alphaTemp):
        SacAgent.__init__(self, policy, valueFunctionApproximator, featureExtractor, discountFactor, alphaTemp)
        
        assert isinstance(policy, ConcretePolicy)
        self.policy = policy
        
        assert isinstance(valueFunctionApproximator, ConcreteValueFunctionApproximator)
        self.valueFunctionApproximator = valueFunctionApproximator
        
        assert isinstance(featureExtractor, ConcreteFeatureExtractor)
        self.featureExtractor = featureExtractor
        
        self.optimizerForUpdateActionValueFunction = None
        self.optimizerForUpdatePolicy = None 
        self.optimizerForUpdateStateValueFunction = None
        
    def reset(self):
        SacAgent.reset(self)  
        
        self.optimizerForUpdateActionValueFunction = tensorflow.keras.optimizers.Adam()
        self.optimizerForUpdatePolicy = tensorflow.keras.optimizers.Adam()
        self.optimizerForUpdateStateValueFunction = tensorflow.keras.optimizers.Adam()
        
    def applyGradientSomeoneToReduce(self, fh, trainableVariables, optimizer):
        
        assert isinstance(optimizer, tensorflow.keras.optimizers.Optimizer)
            
        with tensorflow.GradientTape() as tape:
            _loss = tensorflow.reduce_mean(fh())
        grads = tape.gradient(_loss, trainableVariables)
        optimizer.apply_gradients(zip(grads, trainableVariables))
        
    def getOptimizerForUpdateActionValueFunction(self):
        return self.optimizerForUpdateActionValueFunction
    
    def getOptimizerForUpdatePolicy(self):
        return self.optimizerForUpdatePolicy

    def getOptimizerForUpdateStateValueFunction(self):
        return self.optimizerForUpdateStateValueFunction

    def getTrainableVariablesForUpdateActionValueFunction(self):
        return self.valueFunctionApproximator.trainable_variables + self.featureExtractor.trainable_variables
    
    def getTrainableVariablesForUpdatePolicy(self):
        return self.policy.trainable_variables + self.featureExtractor.trainable_variables
        
    def getTrainableVariablesForUpdateStateValueFunction(self):
        return self.valueFunctionApproximator.trainable_variables + self.featureExtractor.trainable_variables