'''
Created on 2020/11/10

@author: ukai
'''
from skeleton.abstract_context import AbstractContext

class AbstractContextFactory(object):
    '''
    classdocs
    '''


    def create(self
               , nIteration = 2
               , nStepEnvironment = 1
               , nStepGradient = 1
               , nIntervalUpdateStateValueFunction = 1):
        
        return AbstractContext(nIteration, nStepEnvironment, nStepGradient, nIntervalUpdateStateValueFunction)