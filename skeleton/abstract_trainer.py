'''
Created on 2020/11/10

@author: ukai
'''
from skeleton.abstract_agent import AbstractAgent
from skeleton.abstract_environment import AbstractEnvironment
from skeleton.abstract_batch_data_environment import AbstractBatchDataEnvironment
from skeleton.abstract_batch_data_agent import AbstractBatchDataAgent
from skeleton.abstract_batch_data_reward import AbstractBatchDataReward

class AbstractTrainer(object):
    '''
    classdocs
    '''


    def __init__(self, agent, environment, nIteration = 10, nStepEnvironment = 1, nStepGradient = 1, nIntervalUpdateStateValueFunction = 1):
        '''
        Constructor
        '''
        
        assert isinstance(agent, AbstractAgent)
        self.agent = agent
        
        assert isinstance(environment, AbstractEnvironment)
        self.environment = environment
        
        self.nIteration = nIteration
        self.nStepEnvironment = nStepEnvironment
        self.nStepGradient = nStepGradient
        self.nIntervalUpdateStateValueFunction = nIntervalUpdateStateValueFunction
        
    def train(self):
        cnt = 0
        for _ in range(self.nIteration):
            for _ in range(self.nStepEnvironment):
                
                batchDataEnvironment = self.environment.observe()
                batchDataAgent = self.agent.getAction(batchDataEnvironment)
                batchDataReward = self.environment.update(batchDataAgent)
                
                self.appendToBuffer(batchDataEnvironment, batchDataAgent, batchDataReward)
        
            for _ in range(self.nStepGradient):
                
                batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep = self.getBatchDataFromBuffer()
                
                if cnt % self.nIntervalUpdateStateValueFunction == 0:                    
                    self.agent.updateStateValueFunction(batchDataEnvironment)
                self.agent.updatePolicy(batchDataEnvironment)
                self.agent.updateActionValue(batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep)
                
                cnt += 1
            
    def appendToBuffer(self, batchDataEnvironment, batchDataAgent, batchDataReward):
        pass
    
    def getBatchDataFromBuffer(self):
        return (AbstractBatchDataEnvironment()
                , AbstractBatchDataAgent()
                , AbstractBatchDataReward()
                , AbstractBatchDataEnvironment())