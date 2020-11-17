'''
Created on 2020/11/16

@author: ukai
'''
import tensorflow

from skeleton.abstract_value_function_approximator import AbstractValueFunctionApproximator
from concrete.concrete_batch_data_value import ConcreteBatchDataValue


class ConcreteValueFunctionApproximator(AbstractValueFunctionApproximator, tensorflow.keras.Model):
    '''
    classdocs
    '''


    def __init__(self):
        super(ConcreteValueFunctionApproximator, self).__init__()
        
        self.dense = tensorflow.keras.layers.Dense(1)
        
    def call(self, batchDataFeature, batchDataAgent):
        
        _Feature = batchDataFeature.getFeature() # (..., nFeature)
        _Mv = batchDataAgent.getMv() # (..., nMv)
        
        _Pair = tensorflow.concat((_Feature, _Mv), axis = -1) # (..., nFeature + nMv)
        
        _Value = self.dense(_Pair)
        
        return ConcreteBatchDataValue(_Value = _Value)
        
        