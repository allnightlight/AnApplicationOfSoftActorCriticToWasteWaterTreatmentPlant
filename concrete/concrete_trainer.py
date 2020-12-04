'''
Created on 2020/11/27

@author: ukai
'''
from sac.sac_trainer import SacTrainer
from framework.trainer import Trainer

class ConcreteTrainer(SacTrainer, Trainer):
    '''
    classdocs
    '''
    
    def __init__(self, agent, environment, replayBuffer, simulatorFactory, nStepEnvironment, nStepGradient, nIntervalUpdateStateValueFunction, nIterationPerEpoch):
        SacTrainer.__init__(self, agent, environment, replayBuffer, simulatorFactory, nStepEnvironment, nStepGradient, nIntervalUpdateStateValueFunction, nIterationPerEpoch)
        Trainer.__init__(self, agent, environment)