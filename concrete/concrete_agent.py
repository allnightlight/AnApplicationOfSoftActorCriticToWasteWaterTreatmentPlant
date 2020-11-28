'''
Created on 2020/11/15

@author: ukai
'''

from sac.sac_agent import SacAgent
from concrete.concrete_policy import ConcretePolicy
from concrete.concrete_value_function_approximator import ConcreteValueFunctionApproximator
import tensorflow
from sac.sac_feature_extractor import SacFeatureExtractor
import os
from framework.agent import Agent
from framework.util import Utils


class ConcreteAgent(SacAgent, Agent):
    '''
    classdocs
    '''


    def __init__(self, policy, valueFunctionApproximator, featureExtractor, discountFactor, alphaTemp, updatePolicyByAdvantage, saveFolderPath):
        SacAgent.__init__(self, policy, valueFunctionApproximator, featureExtractor, discountFactor, alphaTemp, updatePolicyByAdvantage)
        Agent.__init__(self)
        
        assert isinstance(policy, ConcretePolicy)
        self.policy = policy
        
        assert isinstance(valueFunctionApproximator, ConcreteValueFunctionApproximator)
        self.valueFunctionApproximator = valueFunctionApproximator
        
        assert isinstance(featureExtractor, SacFeatureExtractor)
        self.featureExtractor = featureExtractor
        
        self.optimizerForUpdateActionValueFunction = None
        self.optimizerForUpdatePolicy = None 
        self.optimizerForUpdateStateValueFunction = None
        self.saveFolderPath = saveFolderPath
        
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
        return self.valueFunctionApproximator.trainable_variables 
    
    def getTrainableVariablesForUpdatePolicy(self):
        return self.policy.trainable_variables 
        
    def getTrainableVariablesForUpdateStateValueFunction(self):
        return self.valueFunctionApproximator.trainable_variables
    
    def saveNetworks(self, saveFilePrefix):
        
        for (obj, label) in [
            (self.policy, "policy")
            , (self.valueFunctionApproximator, "valueFunc")
            , (self.featureExtractor, "feature")]:
            
            obj.save_weights(os.path.join(self.saveFolderPath, "{prefix}_{label}.ckpt".format(label = label, prefix = saveFilePrefix)))
            
    def loadNetworks(self, saveFilePrefix):
        
        for (obj, label) in [
            (self.policy, "policy")
            , (self.valueFunctionApproximator, "valueFunc")
            , (self.featureExtractor, "feature")]:
            
            obj.load_weights(os.path.join(self.saveFolderPath, "{prefix}_{label}.ckpt".format(label = label, prefix = saveFilePrefix)))
            
    def createMemento(self):
        agentMemento = Utils.generateRandomString(16)
        self.saveNetworks(agentMemento)
        return agentMemento
        
    def loadMemento(self, agentMemento):
        self.loadNetworks(agentMemento)