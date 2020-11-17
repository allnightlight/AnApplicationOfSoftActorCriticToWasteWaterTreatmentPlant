'''
Created on 2020/11/16

@author: ukai
'''
from skeleton.abstract_context_factory import AbstractContextFactory

class ContextContextFactory(AbstractContextFactory):
    '''
    classdocs
    '''


    def create(self, 
        nStepEnvironment=1, 
        nStepGradient=1, 
        nIntervalUpdateStateValueFunction=1, 
        bufferSize=10):
        
        return AbstractContextFactory.create(self, nStepEnvironment=nStepEnvironment, nStepGradient=nStepGradient, nIntervalUpdateStateValueFunction=nIntervalUpdateStateValueFunction, bufferSize=bufferSize)