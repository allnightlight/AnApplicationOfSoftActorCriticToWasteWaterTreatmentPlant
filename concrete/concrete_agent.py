'''
Created on 2020/11/15

@author: ukai
'''

from skeleton.abstract_agent import AbstractAgent
from concrete.concrete_policy import ConcretePolicy
from concrete.concrete_value_function_approximator import ConcreteValueFunctionApproximator
from concrete.concrete_feature_extractor import ConcreteFeatureExtractor
import tensorflow


class ConcreteAgent(AbstractAgent):
    '''
    classdocs
    '''


    def __init__(self, policy, valueFunctionApproximator, featureExtractor, discountFactor):
        AbstractAgent.__init__(self, policy, valueFunctionApproximator, featureExtractor, discountFactor)
        
        assert isinstance(policy, ConcretePolicy)
        self.policy = policy
        
        assert isinstance(valueFunctionApproximator, ConcreteValueFunctionApproximator)
        self.valueFunctionApproximator = valueFunctionApproximator
        
        assert isinstance(featureExtractor, ConcreteFeatureExtractor)
        self.featureExtractor = featureExtractor
        
        
    def applyGradientSomeoneToReduce(self, fh, trainableVariables, optimizer):
        
        assert isinstance(optimizer, tensorflow.keras.optimizers.Optimizer)
            
        with tensorflow.GradientTape() as tape:
            _loss = tensorflow.reduce_mean(fh())
        grads = tape.gradient(_loss, trainableVariables)
        optimizer.apply_gradients(zip(grads, trainableVariables))