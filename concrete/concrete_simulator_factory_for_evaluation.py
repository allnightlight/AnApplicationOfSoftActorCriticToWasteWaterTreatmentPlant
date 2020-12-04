'''
Created on 2020/12/04

@author: ukai
'''
from sac.sac_simulator_factory import SacSimulatorFactory
from sac.sac_with_deterministic_action import SacSimulatorWithDeterministicAction

class ConcreteSimulatorFactoryForEvaluation(SacSimulatorFactory):
    '''
    classdocs
    '''


    def __init__(self, nSimulationStep):
        SacSimulatorFactory.__init__(self, nSimulationStep)
        
    def create(self, agent, environment):        
        return SacSimulatorWithDeterministicAction(agent, environment, self.nSimulationStep)