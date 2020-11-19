'''
Created on 2020/11/16

@author: ukai
'''

from skeleton.abstract_value_function_approximator import AbstractValueFunctionApproximator
from concrete.concrete_batch_data_value import ConcreteBatchDataValue


class ConcreteValueFunctionApproximator(AbstractValueFunctionApproximator):
    '''
    classdocs
    '''


    def __init__(self):
        super(ConcreteValueFunctionApproximator, self).__init__()
        
        
    def call(self, batchDataFeature, batchDataAgent):
                
        return ConcreteBatchDataValue()
        
    def getAveragedActionValue(self, batchDataFeature, batchDataAgent):
       
        return 1.