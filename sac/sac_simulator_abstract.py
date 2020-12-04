'''
Created on 2020/12/04

@author: ukai
'''
from sac.sac_agent import SacAgent
from sac.sac_environment import SacEnvironment


class SacSimulatorAbstract(object):
    '''
    classdocs
    '''


    def __init__(self, agent, environment, nSimulationStep):
        '''
        Constructor
        '''
        assert isinstance(agent, SacAgent)
        assert isinstance(environment, SacEnvironment)
        
        self.agent = agent
        self.environment = environment
        self.nSimulationStep = nSimulationStep
        
    # <<public, final>>
    def reset(self):
        self.agent.reset()
        self.environment.reset()
    
    # <<protected, abstract>>
    def step(self):
        
        raise NotImplementedError()
        #return batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep
    
    # <<public, final>>
    def generateSeries(self):
        for _ in range(self.nSimulationStep):
            yield self.step() 
        
    