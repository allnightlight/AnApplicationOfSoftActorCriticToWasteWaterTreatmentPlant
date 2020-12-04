'''
Created on 2020/11/10

@author: ukai
'''
from sac.sac_agent import SacAgent
from sac.sac_environment import SacEnvironment
from sac.sac_simulator_abstract import SacSimulatorAbstract
from sac.sac_simulator_factory import SacSimulatorFactory


class SacTrainer(object):
    '''
    classdocs
    '''


    def __init__(self, agent, environment, replayBuffer, simulatorFactory, nStepEnvironment, nStepGradient, nIntervalUpdateStateValueFunction, nIterationPerEpoch):
        '''
        Constructor
        '''
        
        assert isinstance(agent, SacAgent)
        self.agent = agent
        
        assert isinstance(environment, SacEnvironment)
        self.environment = environment
        
        assert isinstance(simulatorFactory, SacSimulatorFactory)
        self.simulator = simulatorFactory.create(agent, environment)
        
        assert isinstance(self.simulator, SacSimulatorAbstract)
        
        self.nStepEnvironment = nStepEnvironment
        self.nStepGradient = nStepGradient
        self.nIntervalUpdateStateValueFunction = nIntervalUpdateStateValueFunction
        self.replayBuffer = replayBuffer
        self.nIterationPerEpoch = nIterationPerEpoch
        
    def reset(self):
        self.cntStepEnvironment = 0
        self.cntStepGradient = 0        
        self.simulator.reset()
        self.replayBuffer.reset()
        
    def stepEnvironment(self):
                
        self.replayBuffer.append(*self.simulator.generateSeries().__next__())
        
    def stepGradient(self):
        
        for batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep in self.replayBuffer.generateStateActionRewardAndNextState(self.nStepGradient):
        
            if self.cntStepGradient % self.nIntervalUpdateStateValueFunction == 0:                    
                self.agent.updateStateValueFunction(batchDataEnvironment)
            self.agent.updatePolicy(batchDataEnvironment)
            self.agent.updateActionValueFunction(batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep)
            
            self.cntStepGradient += 1
        
        
    def train(self):
        
        for _ in range(self.nIterationPerEpoch):
            
            self.stepEnvironment()

            if self.cntStepEnvironment % self.nStepEnvironment == 0:                            
                self.stepGradient()
                
            self.cntStepEnvironment += 1
