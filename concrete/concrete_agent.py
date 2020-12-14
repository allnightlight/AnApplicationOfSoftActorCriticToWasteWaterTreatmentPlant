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
from concrete.concrete_feature_extractor002 import ConcreteFeatureExtractor002
import traceback
import time


class ConcreteAgent(SacAgent, Agent):
    '''
    classdocs
    '''


    def __init__(self, policy, valueFunctionApproximator, featureExtractor, discountFactor, alphaTemp, updatePolicyByAdvantage, saveFolderPath, learningRateForUpdateActionValueFunction, learningRateForUpdatePolicy, learningRateForUpdateStateValueFunction, nLoadTrial=12):
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
        
        self.learningRateForUpdateActionValueFunction = learningRateForUpdateActionValueFunction
        self.learningRateForUpdatePolicy = learningRateForUpdatePolicy
        self.learningRateForUpdateStateValueFunction = learningRateForUpdateStateValueFunction
        
        self.nLoadTrial = nLoadTrial
        
    def reset(self):
        SacAgent.reset(self)  
        
        self.optimizerForUpdateActionValueFunction = tensorflow.keras.optimizers.Adam(learning_rate = self.learningRateForUpdateActionValueFunction)
        self.optimizerForUpdatePolicy = tensorflow.keras.optimizers.Adam(learning_rate = self.learningRateForUpdatePolicy)
        self.optimizerForUpdateStateValueFunction = tensorflow.keras.optimizers.Adam(learning_rate = self.learningRateForUpdateStateValueFunction)
        
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

            if not isinstance(obj, ConcreteFeatureExtractor002):
                
                exit_flag = True
                for k1 in range(self.nLoadTrial):
                    try:
                        obj.load_weights(os.path.join(self.saveFolderPath, "{prefix}_{label}.ckpt".format(label = label, prefix = saveFilePrefix))).expect_partial()
                        exit_flag = False
                    except:
                        exit_flag = True
                        print("""\
>> An error happened on loading tensorflow network parameters.
>> Please, see the following message to see the detail.
                        """)
                        traceback.print_exc()
                        if k1 < self.nLoadTrial-1:
                            print(">> Pause 5[sec] until the next trial ...")
                            time.sleep(5)
                    if exit_flag == False:
                        break         
                assert exit_flag == False, ">> Failed to load the network."
            
    def createMemento(self):
        agentMemento = Utils.generateRandomString(16)
        self.saveNetworks(agentMemento)
        return agentMemento
        
    def loadMemento(self, agentMemento, agentKey):
        super(ConcreteAgent, self).loadMemento(agentMemento, agentKey)
        self.loadNetworks(agentMemento)