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
    

    def __init__(self, builder, loader):
        '''
        Constructor
        '''
        
        assert isinstance(builder, ConcreteBuilder)
        assert isinstance(loader, ConcreteLoader)
        
        self.builder = builder
        self.loader = loader
        
    def runBuild(self, buildParameter):
        
        self.builder.build(buildParameter)        
        
    def runEvaluationWithSimulation(self, evaluators, nSimulationStep, buildParameterLabel = "%", epoch = None, buildParameterKey = None):
        
        assert isinstance(evaluators, list)
        for x in evaluators:
            assert isinstance(x, SacEvaluator)

        for agent, buildParameter, epoch, environment, trainer in self.loader.load(buildParameterLabel, epoch, buildParameterKey):
            
            simulator = SacSimulator(agent, environment)
            simulator.reset()
            
            row = {}
            for evaluator in evaluators:
                assert isinstance(evaluator, SacEvaluator)
                row = {**row, **evaluator.evaluate(simulator.getSimulationResultGenerator(nStep = nSimulationStep))}
            
            yield row, agent, buildParameter, epoch, environment, trainer
