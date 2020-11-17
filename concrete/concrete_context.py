'''
Created on 2020/11/16

@author: ukai
'''
from skeleton.abstract_context import AbstractContext

class ConcreteContext(AbstractContext):
    '''
    classdocs
    '''


    def __init__(self, nStepEnvironment, nStepGradient, nIntervalUpdateStateValueFunction, bufferSize, nFeature):
        AbstractContext.__init__(self, nStepEnvironment, nStepGradient, nIntervalUpdateStateValueFunction, bufferSize)
        
        self.nFeature = nFeature