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
        
    def step(self):
        
        batchDataEnvironment = self.environment.observe()
        batchDataAgent = self.agent.getAction(batchDataEnvironment)
        batchDataReward = self.environment.update(batchDataAgent)
        batchDataEnvironmentNextStep = self.environment.observe()

        return batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep
        
    def getSimulationResultGenerator(self, nStep):        
        for _ in range(nStep):
            yield self.step()
        