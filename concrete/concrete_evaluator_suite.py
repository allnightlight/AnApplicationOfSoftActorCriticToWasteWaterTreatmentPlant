'''
Created on 2020/12/02

@author: ukai
'''
from sac.sac_evaluator import SacEvaluator
from sac.sac_simulator import SacSimulator


class ConcreteEvaluatorSuite(object):
    '''
    classdocs
    '''


    def __init__(self, evaluators):
        '''
        Constructor
        '''
                
        assert isinstance(evaluators, list)
        for x in evaluators:
            assert isinstance(x, SacEvaluator)
        
        self.evaluators = evaluators

    def evaluate(self, agent, environment, nSimulationStep):
        
        simulator = SacSimulator(agent, environment)
        simulator.reset()
        
        series = [simulator.stepWithDeterministicAction() for _ in range(nSimulationStep)]
        
        for evaluator in self.evaluators:
            assert isinstance(evaluator, SacEvaluator)
            yield evaluator, evaluator.evaluate(series)