'''
Created on 2020/11/29

@author: ukai
'''
from concrete.concrete_builder import ConcreteBuilder
from concrete.concrete_loader import ConcreteLoader
from sac.sac_evaluator import SacEvaluator, SacEvaluatorDummy
from sac.sac_simulator import SacSimulator
from concrete.concrete_evaluator_suite import ConcreteEvaluatorSuite
from concrete.concrete_evaluation_db import ConcreteEvaluationDb
from sac.sac_evaluate_method import SacEvaluateMethod

class ConcreteApplication(object):
    '''
    classdocs
    '''
    

    def __init__(self, builder, loader, evaluatorSuite, evaluationDb, evaluatorDummy):
        '''
        Constructor
        '''
        
        assert isinstance(builder, ConcreteBuilder)
        assert isinstance(loader, ConcreteLoader)
        assert isinstance(evaluatorSuite, ConcreteEvaluatorSuite)
        assert isinstance(evaluationDb, ConcreteEvaluationDb)
        assert isinstance(evaluatorDummy, SacEvaluatorDummy)
        
        self.builder = builder
        self.loader = loader
        self.evaluatorSuite = evaluatorSuite
        self.evaluationDb = evaluationDb        
        self.evaluatorDummy = evaluatorDummy
        
        
    def runBuild(self, buildParameter):
        
        self.builder.build(buildParameter)
        
    def runEvaluationWithSimulationDummy(self, evaluateMethods, buildParameterLabel = "%", epoch = None, buildParameterKey = None, agentKey = None):
        
        for evaluateMethod in evaluateMethods:
            assert isinstance(evaluateMethod, SacEvaluateMethod)

        cntCallSimulation = 0
        for agent, buildParameter, epoch, environment, _ in self.loader.load(buildParameterLabel, epoch, buildParameterKey, agentKey):
            
            evaluateMethodsNotYetDone = [evaluateMethod for evaluateMethod in evaluateMethods
                if not self.evaluationDb.exists(agentKey = agent.getAgentKey(), epoch = epoch, evaluatorClass = evaluateMethod.__class__.__name__)]
            
            for evaluateMethod, stats in self.evaluatorDummy.evaluate(agent, environment, evaluateMethodsNotYetDone):
                cntCallSimulation += 1

                self.evaluationDb.save(agentKey = agent.getAgentKey()
                                       , epoch = epoch
                                       , buildParameterLabel = buildParameterLabel
                                       , buildParameterMemnto = buildParameter.createMemento()
                                       , evaluatorClass = evaluateMethod.__class__.__name__
                                       , stats = stats)                        
        return cntCallSimulation
    
    def runEvaluationWithSimulation(self, nSimulationStep, buildParameterLabel = "%", epoch = None, buildParameterKey = None, agentKey = None):
        
        cntCallSimulation = 0
        for agent, buildParameter, epoch, environment, trainer in self.loader.load(buildParameterLabel, epoch, buildParameterKey, agentKey):
            
            if self.evaluationDb.exists(agentKey = agent.getAgentKey(), epoch = epoch):
                continue
            else:
                cntCallSimulation += 1
                
            for evaluator, stats in self.evaluatorSuite.evaluate(agent, environment, nSimulationStep):
            
                self.evaluationDb.save(agentKey = agent.getAgentKey()
                                       , epoch = epoch
                                       , buildParameterLabel = buildParameterLabel
                                       , buildParameterMemnto = buildParameter.createMemento()
                                       , evaluatorClass = evaluator.__class__.__name__
                                       , stats = stats)
        return cntCallSimulation
            
    def exportEvaluationTable(self, buildParameterLabel = None):
        
        return self.evaluationDb.export(buildParameterLabel)