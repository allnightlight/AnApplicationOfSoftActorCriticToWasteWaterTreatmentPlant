'''
Created on 2020/12/04

@author: ukai
'''
from sac.sac_simulator_abstract import SacSimulatorAbstract


class SacSimulatorWithStochasticAction(SacSimulatorAbstract):    
    '''
    classdocs
    '''

    
    def __init__(self, agent, environment, nSimulationStep):
        SacSimulatorAbstract.__init__(self, agent, environment, nSimulationStep)

    def step(self):
        
        batchDataEnvironment = self.environment.observe()
        batchDataAgent = self.agent.getAction(batchDataEnvironment)
        batchDataReward = self.environment.updateWithStochasticAction(batchDataAgent)
        batchDataEnvironmentNextStep = self.environment.observe()

        return batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep
