'''
Created on 2020/11/29

@author: ukai
'''
from concrete.concrete_builder import ConcreteBuilder
from concrete.concrete_loader import ConcreteLoader
from sac.sac_evaluator import SacEvaluator
from concrete.concrete_evaluation_db import ConcreteEvaluationDb
from sac.sac_evaluate_method import SacEvaluateMethod
import sys

class ConcreteApplication(object):
    '''
    classdocs
    '''
    

    def __init__(self, builder, loader, evaluationDb, evaluator, showProgress):
        '''
        Constructor
        '''
        
        assert isinstance(builder, ConcreteBuilder)
        assert isinstance(loader, ConcreteLoader)
        assert isinstance(evaluationDb, ConcreteEvaluationDb)
        assert isinstance(evaluator, SacEvaluator)
        
        self.builder = builder
        self.loader = loader
        self.evaluationDb = evaluationDb        
        self.evaluator = evaluator
        self.showProgress = showProgress
        
        
    def runBuild(self, buildParameter):
        
        self.builder.build(buildParameter)
        
    def runEvaluationWithSimulation(self, evaluateMethods, buildParameterLabel = "%", epochGiven = None, buildParameterKey = None, agentKey = None):
        
        for evaluateMethod in evaluateMethods:
            assert isinstance(evaluateMethod, SacEvaluateMethod)

        def generateStats():

            if self.showProgress:
                sys.stdout.write(">> Start Evaluation ...")
            
            for agent, buildParameter, epoch, environment, _ in self.loader.load(buildParameterLabel, epochGiven, buildParameterKey, agentKey):
                if self.showProgress:
                    sys.stdout.write("\r>> buildParameterLabel:{buildParameterLabel}, agent:{agent}, epoch:{epoch}".format(buildParameterLabel=buildParameter.label, agent=agent.getAgentKey(), epoch=epoch))
                
                evaluateMethodsNotYetDone = [evaluateMethod for evaluateMethod in evaluateMethods
                    if not self.evaluationDb.exists(agentKey = agent.getAgentKey(), epoch = epoch, evaluatorClass = evaluateMethod.__class__.__name__)]
                
                for evaluateMethod, stats in self.evaluator.evaluate(agent, environment, evaluateMethodsNotYetDone):
                    
                    yield agent.getAgentKey(), epoch, buildParameterLabel, buildParameter.createMemento(), evaluateMethod.__class__.__name__, stats

            if self.showProgress:
                sys.stdout.write("\r>> Finished evaluation.")
                    
        return self.evaluationDb.saveGeneratedStats(generateStats())
                
    def exportEvaluationTable(self, buildParameterLabel = "%", agentKey = None, epoch = None, evaluatorClass = None):
        
        return self.evaluationDb.export(buildParameterLabel, agentKey, epoch, evaluatorClass)