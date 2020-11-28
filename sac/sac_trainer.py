'''
Created on 2020/11/10

@author: ukai
'''
from sac.sac_agent import SacAgent
from sac.sac_environment import SacEnvironment

class SacTrainer(object):
    '''
    classdocs
    '''


    def __init__(self, agent, environment, replayBuffer, nStepEnvironment, nStepGradient, nIntervalUpdateStateValueFunction, nIterationPerEpoch):
        '''
        Constructor
        '''
        
        assert isinstance(agent, SacAgent)
        self.agent = agent
        
        assert isinstance(environment, SacEnvironment)
        self.environment = environment
        
        self.nStepEnvironment = nStepEnvironment
        self.nStepGradient = nStepGradient
        self.nIntervalUpdateStateValueFunction = nIntervalUpdateStateValueFunction
        self.replayBuffer = replayBuffer
        self.nIterationPerEpoch = nIterationPerEpoch
        
    def reset(self):
        self.cntStepGradient = 0
        self.agent.reset()
        self.environment.reset()
        self.replayBuffer.reset()
        
    def stepEnvironment(self):
        
        batchDataEnvironment = self.environment.observe()
        batchDataAgent = self.agent.getAction(batchDataEnvironment)
        batchDataReward = self.environment.update(batchDataAgent)
        batchDataEnvironmentNextStep = self.environment.observe()
        
        self.replayBuffer.append(batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep)
        
    def stepGradient(self):
        
        for batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep in self.replayBuffer.generateStateActionRewardAndNextState(self.nStepGradient):
        
            if self.cntStepGradient % self.nIntervalUpdateStateValueFunction == 0:                    
                self.agent.updateStateValueFunction(batchDataEnvironment)
            self.agent.updatePolicy(batchDataEnvironment)
            self.agent.updateActionValueFunction(batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep)
            
            self.cntStepGradient += 1
        
        
    def train(self):
        
        for _ in range(self.nIterationPerEpoch//self.nStepEnvironment):
            
            for _ in range(self.nStepEnvironment):                
                self.stepEnvironment()
                            
            self.stepGradient()
                
        for _ in range(self.nIterationPerEpoch - (self.nIterationPerEpoch//self.nStepEnvironment) * self.nIterationPerEpoch):                
            self.stepEnvironment()
