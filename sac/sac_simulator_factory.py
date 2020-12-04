'''
Created on 2020/12/04

@author: ukai
'''
from sac.sac_with_stochastic_action import SacSimulatorWithStochasticAction

class SacSimulatorFactory(object):
    '''
    classdocs
    '''


    def create(self, agent, environment, nSimulationStep):
        
        return SacSimulatorWithStochasticAction(agent, environment, nSimulationStep)