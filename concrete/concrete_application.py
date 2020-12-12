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
    

    def __init__(self, builder, loader, evaluationDb, evaluator, showProgress, maxNumOfEvaluateAgents):
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
        self.maxNumOfEvaluateAgents = maxNumOfEvaluateAgents
        
        
    def runBuild(self, buildParameter):
        
        self.builder.build(buildParameter)
        
    def runEvaluationWithSimulation(self, evaluateMethods, buildParameterLabel = "%", epochGiven = None, buildParameterKey = None, agentKey = None):
        
        for evaluateMethod in evaluateMethods:
            assert isinstance(evaluateMethod, SacEvaluateMethod)
        
        if self.showProgress:
            sys.stdout.write(">> Start Evaluation ...")
            
        pairs = self.evaluationDb.getPairsOfAgentKeyEpochEvaluatorClass()
        
        cnt = 0
        statsArr = []
        for agentKey, epochFound in self.loader.getPairsOfAgentKeyAndEpoch(buildParameterLabel, epochGiven, buildParameterKey, agentKey):
            
            if self.maxNumOfEvaluateAgents is not None and not cnt < self.maxNumOfEvaluateAgents:
                break
            
            evaluateMethodsNotYetDone = [evaluateMethod for evaluateMethod in evaluateMethods if not (agentKey, epochFound, evaluateMethod.__class__.__name__) in pairs]            
            
            if len(evaluateMethodsNotYetDone) == 0:
                continue
            else:
                cnt += 1

            # The unique pair of agent at the epoch will be found:
            agent, buildParameter, epoch, environment, _ = self.loader.load(buildParameterLabel=buildParameterLabel, epoch = epochFound, buildParameterKey = buildParameterKey, agentKey = agentKey).__next__()

            if self.showProgress:
                sys.stdout.write("\r>> buildParameterLabel:{buildParameterLabel}, agent:{agent}, epoch:{epoch}".format(buildParameterLabel=buildParameter.label, agent=agent.getAgentKey(), epoch=epoch))
            
            for evaluateMethod, stats in self.evaluator.evaluate(agent, environment, evaluateMethodsNotYetDone):                    
                statsArr.append((agent.getAgentKey(), epoch, buildParameterLabel, buildParameter.createMemento(), evaluateMethod.__class__.__name__, stats))
                                                
        return self.evaluationDb.saveGeneratedStats(statsArr)
                
    def exportEvaluationTable(self, buildParameterLabel = "%", agentKey = None, epoch = None, evaluatorClass = None):
        
        return self.evaluationDb.export(buildParameterLabel, agentKey, epoch, evaluatorClass)