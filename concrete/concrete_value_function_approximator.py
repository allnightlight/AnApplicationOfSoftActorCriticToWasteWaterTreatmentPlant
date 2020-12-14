'''
Created on 2020/11/16

@author: ukai
'''

import tensorflow

from sac.sac_value_function_approximator import SacValueFunctionApproximator

class ConcreteValueFunctionApproximator(SacValueFunctionApproximator, tensorflow.keras.Model):
    '''
    classdocs
    '''


    def __init__(self):
        super(ConcreteValueFunctionApproximator, self).__init__()
        
    def call(self, batchDataFeature, batchDataAgent):
        raise NotImplementedError()
        
    def getActionValue(self, batchDataFeature, batchDataAgent):
        raise NotImplementedError()
    
    def getStateValue(self, batchDataFeature):
        raise NotImplementedError()
    
    def getAveragedActionValue(self, batchDataFeature, batchDataAgent):
        raise NotImplementedError()            