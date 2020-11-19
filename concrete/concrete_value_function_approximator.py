'''
Created on 2020/11/16

@author: ukai
'''

import tensorflow

from concrete.concrete_batch_data_value import ConcreteBatchDataValue
from skeleton.abstract_value_function_approximator import AbstractValueFunctionApproximator


class ConcreteValueFunctionApproximator(AbstractValueFunctionApproximator, tensorflow.keras.Model):
    '''
    classdocs
    '''


    def __init__(self):
        super(ConcreteValueFunctionApproximator, self).__init__()
        
        
    def call(self, batchDataFeature, batchDataAgent):
                
        return ConcreteBatchDataValue()
        
    def getAveragedActionValue(self, batchDataFeature, batchDataAgent):
       
        return 1.