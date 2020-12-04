'''
Created on 2020/11/29

@author: ukai
'''
from sac.sac_simulator_factory import SacSimulatorFactory
    
class SacEvaluator(object):
    '''
    classdocs
    '''

    def __init__(self, simulatorFactory):
        
        assert isinstance(simulatorFactory, SacSimulatorFactory)
        self.simulatorFactory = simulatorFactory
        

    def evaluate(self, agent, environment, evaluateMethods):
        simulator = self.simulatorFactory.create(agent, environment)
        simulator.reset()
        
        g = [*simulator.generateSeries()]
        
        for evaluateMethod in evaluateMethods:
            yield evaluateMethod, evaluateMethod.evaluate(g) 