'''
Created on 2020/11/10

@author: ukai
'''

class AbstractContext(object):
    '''
    classdocs
    '''


    def __init__(self, nIteration, nStepEnvironment, nStepGradient, nIntervalUpdateStateValueFunction):
        '''
        Constructor
        '''
        
        self.nIteration = nIteration
        self.nStepEnvironment = nStepEnvironment
        self.nStepGradient = nStepGradient
        self.nIntervalUpdateStateValueFunction = nIntervalUpdateStateValueFunction
        