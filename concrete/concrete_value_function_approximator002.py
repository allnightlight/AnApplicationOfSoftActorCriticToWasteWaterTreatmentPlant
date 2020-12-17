'''
Created on 2020/11/16

@author: ukai
'''

import tensorflow

from concrete.concrete_batch_data_value import ConcreteBatchDataValue
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_batch_data_feature import ConcreteBatchDataFeature
from concrete.concrete_value_function_approximator import ConcreteValueFunctionApproximator


class ConcreteValueFunctionApproximator002(ConcreteValueFunctionApproximator):
    '''
    classdocs
    '''


    def __init__(self, nFeature, nMv, nSampleOfActionsInValueFunctionApproximator, nHidden, nRedundancy):
        super(ConcreteValueFunctionApproximator, self).__init__()
        
        assert nRedundancy == 1 or nRedundancy == 2, "nRedundancy is allowed for only 1 or 2"
        
        self.nMv = nMv
        self.nSample = nSampleOfActionsInValueFunctionApproximator
        self.nRedundancy = nRedundancy
        
        self.featureAndAction2actionValuePrimary = tensorflow.keras.Sequential((
            tensorflow.keras.Input(shape = (nFeature + nMv,))
            , tensorflow.keras.layers.Dense(nHidden, activation="relu")
            , tensorflow.keras.layers.Dense(1))) 

        self.featureAndAction2actionValueSecondary = None
        if nRedundancy == 2:
            self.featureAndAction2actionValueSecondary = tensorflow.keras.Sequential((
                tensorflow.keras.Input(shape = (nFeature + nMv,))
                , tensorflow.keras.layers.Dense(nHidden, activation="relu")
                , tensorflow.keras.layers.Dense(1))) 

        self.feature2stateValue = tensorflow.keras.Sequential((
            tensorflow.keras.Input(shape = (nFeature,))
            , tensorflow.keras.layers.Dense(nHidden, activation="relu")
            , tensorflow.keras.layers.Dense(1))) 
      
    def call(self, _Feature, _SampledAction):

        if self.nRedundancy == 1:
            _ValuePrimary = self.featureAndAction2actionValuePrimary(tensorflow.concat((_Feature, _SampledAction), axis=-1)) # (..., 1)
            return _ValuePrimary            

        if self.nRedundancy == 2:
            _ValuePrimary = self.featureAndAction2actionValuePrimary(tensorflow.concat((_Feature, _SampledAction), axis=-1)) # (..., 1)
            _ValueSecondary= self.featureAndAction2actionValueSecondary(tensorflow.concat((_Feature, _SampledAction), axis=-1)) # (..., 1)
            return tensorflow.concat((_ValuePrimary, _ValueSecondary), axis=-1) # (..., 2)
        
    def getActionValue(self, batchDataFeature, batchDataAgent):
        
        _Feature = batchDataFeature.getFeature() # (..., nFeature)
        _SampledAction = batchDataAgent.getSampledAction() # (..., nMv)
        
        return ConcreteBatchDataValue(_Value = self.call(_Feature, _SampledAction))

    def getStateValue(self, batchDataFeature):

        _Feature = batchDataFeature.getFeature() # (..., nFeature)
        _Value = self.feature2stateValue(_Feature) # (..., 1)
                    
        return ConcreteBatchDataValue(_Value = _Value)
        
    def getAveragedActionValue(self, batchDataFeature, batchDataAgent):
        
        assert isinstance(batchDataFeature, ConcreteBatchDataFeature)
        assert isinstance(batchDataAgent, ConcreteBatchDataAgent)
        
        _Feature = batchDataFeature.getFeature() # (..., nFeature)
        
        ActionValues = []
        for _SampledAction in batchDataAgent.generateSamples(self.nSample):            
            ActionValues.append(tensorflow.reduce_min(self.call(_Feature, _SampledAction), axis=-1, keepdims=True))        
        _ActionValueAveraged = tensorflow.reduce_mean(tensorflow.concat(ActionValues, axis=-1), axis=-1, keepdims=True) # (..., 1)
       
        return ConcreteBatchDataValue(_Value = _ActionValueAveraged)
    
    def getTrainableVariablesOfActionValueFunction(self):
        if self.nRedundancy == 1:
            return self.featureAndAction2actionValuePrimary.trainable_variables

        if self.nRedundancy == 2:
            return self.featureAndAction2actionValuePrimary.trainable_variables + self.featureAndAction2actionValueSecondary.trainable_variables
    
    def getTrainableVariablesOfStateValueFunction(self):
        return self.feature2stateValue.trainable_variables