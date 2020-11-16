'''
Created on 2020/11/10

@author: ukai
'''
from skeleton.abstract_trainer import AbstractTrainer
from skeleton.abstract_replay_buffer import AbstractReplayBuffer

class AbstractTrainerFactory(object):
    '''
    classdocs
    '''


    def create(self, context, agent, environment):
        
        return AbstractTrainer(agent = agent
                               , environment = environment
                               , replayBuffer = AbstractReplayBuffer(bufferSize = context.bufferSize)
                               , nStepEnvironment = context.nStepEnvironment
                               , nStepGradient = context.nStepGradient
                               , nIntervalUpdateStateValueFunction = context.nIntervalUpdateStateValueFunction)