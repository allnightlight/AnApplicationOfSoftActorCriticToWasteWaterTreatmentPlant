'''
Created on 2020/11/10

@author: ukai
'''
from sac.sac_agent import SacAgent
from sac.sac_environment import SacEnvironment
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from sac.sac_batch_data_agent import SacBatchDataAgent
from sac.sac_batch_data_reward import SacBatchDataReward

class SacTrainer(object):
    '''
    classdocs
    '''


    def __init__(self, agent, environment, replayBuffer, nStepEnvironment = 1, nStepGradient = 1, nIntervalUpdateStateValueFunction = 1):
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
        
        assert len(self.replayBuffer.buffer) > 0, "Replay buffer is empty so far. Please, run stepEnvironment at least once."

        batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep = self.replayBuffer.getStateActionRewardAndNextState()
        
        if self.cntStepGradient % self.nIntervalUpdateStateValueFunction == 0:                    
            self.agent.updateStateValueFunction(batchDataEnvironment)
        self.agent.updatePolicy(batchDataEnvironment)
        self.agent.updateActionValueFunction(batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep)
        
        self.cntStepGradient += 1
        
        
    def train(self, nIteration):
        
        for _ in range(nIteration//self.nStepEnvironment):
            
            for _ in range(self.nStepEnvironment):                
                self.stepEnvironment()
                
            for _ in range(self.nStepGradient):
                self.stepGradient()