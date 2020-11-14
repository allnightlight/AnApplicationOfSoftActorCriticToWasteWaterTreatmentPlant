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


    def __init__(self, agent, environment, nStepEnvironment = 1, nStepGradient = 1, nIntervalUpdateStateValueFunction = 1):
        '''
        Constructor
        '''
        
        assert isinstance(agent, AbstractAgent)
        self.agent = agent
        
        assert isinstance(environment, AbstractEnvironment)
        self.environment = environment
        
        self.nStepEnvironment = nStepEnvironment
        self.nStepGradient = nStepGradient
        self.nIntervalUpdateStateValueFunction = nIntervalUpdateStateValueFunction
        
    def reset(self):
        self.cntStepGradient = 0
        self.agent.reset()
        self.environment.reset()
        self.resetBuffer()
        
    def stepEnvironment(self):
        
        batchDataEnvironment = self.environment.observe()
        batchDataAgent = self.agent.getAction(batchDataEnvironment)
        batchDataReward = self.environment.update(batchDataAgent)
        batchDataEnvironmentNextStep = self.environment.observe()
        
        self.appendToBuffer(batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep)
        
    def stepGradient(self):

        batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep = self.getBatchDataFromBuffer()
        
        if self.cntStepGradient % self.nIntervalUpdateStateValueFunction == 0:                    
            self.agent.updateStateValueFunction(batchDataEnvironment)
        self.agent.updatePolicy(batchDataEnvironment)
        self.agent.updateActionValue(batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep)
        
        self.cntStepGradient += 1
        
        
    def train(self, nIteration):
        
        for _ in range(nIteration//self.nStepEnvironment):
            
            for _ in range(self.nStepEnvironment):                
                self.stepEnvironment()
                
            for _ in range(self.nStepGradient):
                self.stepGradient()
            
    def resetBuffer(self):
        pass
    
    def appendToBuffer(self, batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep):
        pass
    
    def getBatchDataFromBuffer(self):
        return (AbstractBatchDataEnvironment()
                , AbstractBatchDataAgent()
                , AbstractBatchDataReward()
                , AbstractBatchDataEnvironment())