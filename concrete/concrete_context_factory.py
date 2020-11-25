'''
Created on 2020/11/16

@author: ukai
'''
from sac.sac_context_factory import SacContextFactory

class ContextContextFactory(SacContextFactory):
    '''
    classdocs
    '''


    def create(self, 
        nStepEnvironment=1, 
        nStepGradient=1, 
        nIntervalUpdateStateValueFunction=1, 
        bufferSize=10):
        
        return SacContextFactory.create(self, nStepEnvironment=nStepEnvironment, nStepGradient=nStepGradient, nIntervalUpdateStateValueFunction=nIntervalUpdateStateValueFunction, bufferSize=bufferSize)