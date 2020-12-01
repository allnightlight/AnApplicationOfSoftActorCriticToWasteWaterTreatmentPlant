'''
Created on 2020/11/29

@author: ukai
'''
from concrete.concrete_builder import ConcreteBuilder
from concrete.concrete_loader import ConcreteLoader
from sac.sac_evaluator import SacEvaluator
from sac.sac_simulator import SacSimulator

class ConcreteApplication(object):
    '''
    classdocs
    '''
    

    def __init__(self, builder, loader, evaluators):
        '''
        Constructor
        '''
        
        assert isinstance(builder, ConcreteBuilder)
        assert isinstance(loader, ConcreteLoader)
        assert isinstance(evaluators, list)
        for x in evaluators:
            assert isinstance(x, SacEvaluator)
        
        self.builder = builder
        self.loader = loader
        self.evaluators = evaluators
        
        
    def runBuild(self, buildParameter):
        
        self.builder.build(buildParameter)        
        
    def runEvaluationWithSimulation(self, nSimulationStep, buildParameterLabel = "%", epoch = None, buildParameterKey = None, agentKey = None):
        
        for agent, buildParameter, epoch, environment, trainer in self.loader.load(buildParameterLabel, epoch, buildParameterKey, agentKey):
            
            simulator = SacSimulator(agent, environment)
            simulator.reset()
            
            row = {}
            for evaluator in self.evaluators:
                assert isinstance(evaluator, SacEvaluator)
                row = {**row, **evaluator.evaluate([simulator.stepWithDeterministicAction() for _ in range(nSimulationStep)])}
            
            yield row, agent, buildParameter, epoch, environment, trainer
