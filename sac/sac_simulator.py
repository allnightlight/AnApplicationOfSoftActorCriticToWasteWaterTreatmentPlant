'''
Created on 2020/11/29

@author: ukai
'''
from sac.sac_agent import SacAgent
from sac.sac_environment import SacEnvironment

class SacSimulator(object):
    '''
    classdocs
    '''


    def __init__(self, agent, environment):
        '''
        Constructor
        '''
        assert isinstance(agent, SacAgent)
        assert isinstance(environment, SacEnvironment)
        self.agent = agent
        self.environment = environment
        
    def reset(self):
        self.agent.reset()
        self.environment.reset()
    
    # <<private>>    
    def stepPrivate(self, mode):
        
        batchDataEnvironment = self.environment.observe()
        batchDataAgent = self.agent.getAction(batchDataEnvironment)
        if mode == "stochastic":
            batchDataReward = self.environment.updateWithStochasticAction(batchDataAgent)
        if mode == "deterministic":
            batchDataReward = self.environment.updateWithDeterministicAction(batchDataAgent)
        batchDataEnvironmentNextStep = self.environment.observe()

        return batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep
    
    # <<public>>
    def stepWithDeterministicAction(self):
        return self.stepPrivate(mode = "deterministic")
        
    # <<public>>
    def stepWithStochasticAction(self):
        return self.stepPrivate(mode = "stochastic")