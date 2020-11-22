'''
Created on 2020/11/16

@author: ukai
'''

import tensorflow

from concrete.concrete_batch_data_value import ConcreteBatchDataValue
from skeleton.abstract_value_function_approximator import AbstractValueFunctionApproximator
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_batch_data_feature import ConcreteBatchDataFeature


class ConcreteValueFunctionApproximator(AbstractValueFunctionApproximator, tensorflow.keras.Model):
    '''
    classdocs
    '''


    def __init__(self, nFeature, nMv, nSampleOfActionsInValueFunctionApproximator, nHidden):
        super(ConcreteValueFunctionApproximator, self).__init__()
        
        self.nMv = nMv
        self.nSample = nSampleOfActionsInValueFunctionApproximator
        
        self.featureAndAction2value = tensorflow.keras.Sequential((
            tensorflow.keras.Input(shape = (nFeature + nMv,))
            , tensorflow.keras.layers.Dense(nHidden, activation="relu")
            , tensorflow.keras.layers.Dense(1))) 
        
      
    def call(self, _Feature, _SampledAction):
        
        return self.featureAndAction2value(tensorflow.concat((_Feature, _SampledAction), axis=-1)) # (..., 1)   
        
    def getActionValue(self, batchDataFeature, batchDataAgent):
        
        _Feature = batchDataFeature.getFeature() # (..., nFeature)
        _SampledAction = batchDataAgent.getSampledAction() # (..., nMv)
                
        return ConcreteBatchDataValue(_Value = self.call(_Feature, _SampledAction))

    def getStateValue(self, batchDataFeature):
        
        _Feature = batchDataFeature.getFeature() # (..., nFeature)
        _SampledAction = tensorflow.zeros(shape = (*_Feature.shape[:-1], self.nMv)) # (..., nMv)
                
        return ConcreteBatchDataValue(_Value = self.call(_Feature, _SampledAction))
        
    def getAveragedActionValue(self, batchDataFeature, batchDataAgent):
        
        assert isinstance(batchDataFeature, ConcreteBatchDataFeature)
        assert isinstance(batchDataAgent, ConcreteBatchDataAgent)
        
        _Feature = batchDataFeature.getFeature() # (..., nFeature)
        
        ActionValues = []
        for _SampledAction in batchDataAgent.generateSamples(self.nSample):
            ActionValues.append(self.call(_Feature, _SampledAction))        
        _ActionValueAveraged = tensorflow.reduce_mean(tensorflow.concat(ActionValues, axis=-1), axis=-1, keepdims=True) # (..., 1)
       
        return ConcreteBatchDataValue(_Value = _ActionValueAveraged)
    