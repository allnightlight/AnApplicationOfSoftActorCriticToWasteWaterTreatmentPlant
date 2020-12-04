'''
Created on 2020/12/04

@author: ukai
'''
from sac.sac_with_stochastic_action import SacSimulatorWithStochasticAction

class SacSimulatorFactory(object):
    '''
    classdocs
    '''

    def __init__(self, nSimulationStep):
        self.nSimulationStep = nSimulationStep

    def create(self, agent, environment):
        
        return SacSimulatorWithStochasticAction(agent, environment, self.nSimulationStep)