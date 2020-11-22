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
               , nStepEnvironment = 1
               , nStepGradient = 1
               , nIntervalUpdateStateValueFunction = 1
               , bufferSize = 10
               , discountFactor = 0.99
               , alphaTemp = 1.0):
        
        return AbstractContext(nStepEnvironment, nStepGradient, nIntervalUpdateStateValueFunction, bufferSize, discountFactor, alphaTemp)