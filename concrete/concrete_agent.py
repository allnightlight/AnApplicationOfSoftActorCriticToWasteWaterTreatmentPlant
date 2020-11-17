'''
Created on 2020/11/15

@author: ukai
'''
import tensorflow

from skeleton.abstract_agent import AbstractAgent


class ConcreteAgent(AbstractAgent):
    '''
    classdocs
    '''


    def __init__(self, policy, valueFunctionApproximator, featureExtractor
                 , learningRateForUpdateActionValue
                 , learningRateForUpdatePolicy
                 , learningRateForUpdateStateValueFunction
                 , nSampleActionsOnUpdateStateValueFunction):
        AbstractAgent.__init__(self, policy, valueFunctionApproximator, featureExtractor)
        
        self.optimizerForUpdateActionValue = tensorflow.keras.optimizers.Adam(learning_rate = learningRateForUpdateActionValue)
        self.optimizerForUpdatePolicy = tensorflow.keras.optimizers.Adam(learning_rate = learningRateForUpdatePolicy)
        self.optimizerForUpdateStateValueFunction = tensorflow.keras.optimizers.Adam(learning_rate = learningRateForUpdateStateValueFunction)
        self.nSampleActionsOnUpdateStateValueFunction = nSampleActionsOnUpdateStateValueFunction
        
    def applyGradientsForUpdateActionValue(self, grads, trainableVariables):
        self.optimizerForUpdateActionValue.apply_gradients(zip(grads, trainableVariables))
    
    def applyGradientsForUpdatePolicy(self, grads, trainableVariables):
        self.optimizerForUpdatePolicy.apply_gradients(zip(grads, trainableVariables))
    
    def applyGradientsForUpdateStateValueFunction(self, grads, trainableVariables):
        self.optimizerForUpdateStateValueFunction.apply_gradients(zip(grads, trainableVariables))
        
    def getGradientsForUpdateActionValue(self, batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep, trainableVariables):
        return None
    
    def getGradientsForUpdatePolicy(self, batchDataEnvironment, trainableVariables):
        return None
        
    def getGradientsForUpdateStateValueFunction(self, batchDataEnvironment, trainableVariables):
        _loss = None
        with tensorflow.GradientTape() as tape:
            _V = self.valueFunctionApproximator(batchDataEnvironment).getValue() # (..., 1)            
            Qs = []
            for batchDataAgent in self.policy(batchDataEnvironment, self.nSampleActionsOnUpdateStateValueFunction):
                Qs.append(self.valueFunctionApproximator(batchDataEnvironment, batchDataAgent).getValue())
            
            _Err = _V - tensorflow.reduce_mean(tensorflow.stack(Qs, axis=-1), axis=-1) # (..., 1)            
            _loss = tensorflow.reduce_mean(tensorflow.abs(_Err)) # (,)
                
        return tape.gradient(_loss, trainableVariables)
