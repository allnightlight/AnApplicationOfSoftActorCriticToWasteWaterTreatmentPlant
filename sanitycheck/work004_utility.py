'''
Created on 2020/11/29

@author: ukai
'''
from datetime import datetime

import numpy as np
import pandas

from concrete.concrete_application import ConcreteApplication
from concrete.concrete_build_parameter import ConcreteBuildParameter
from concrete.concrete_builder import ConcreteBuilder
from concrete.concrete_loader import ConcreteLoader
from framework.store import Store
from sac.sac_evaluator import SacEvaluator
from sanitycheck.work004_evaluator import Work004Evaluator


class Work004Utility(object):
    '''
    classdocs
    '''
    
    @classmethod
    def create(cls, nAgent = 2**10, nEpoch = 2**11):
        
        store = Store(dbPath = "trained_agent.sqlite", trainLogFolderPath = "tmpTrainLog")        
        builder = ConcreteBuilder(store)
        loader = ConcreteLoader(store)
        evaluators = [Work004Evaluator(),]
        
        return Work004Utility(app = ConcreteApplication(builder, loader, evaluators), nSimulationStep = 2**7, nAgent = nAgent, nEpoch = nEpoch), store


    def __init__(self, app, nSimulationStep, nAgent, nEpoch):
        '''
        Constructor
        '''
        
        assert isinstance(app, ConcreteApplication)
        self.app = app
        self.nSimulationStep = nSimulationStep
        self.nAgent = nAgent
        self.nEpoch = nEpoch
        
    def build(self):
        
        for buildParameter in self.generateBuildParameter():
            self.app.runBuild(buildParameter)
        
    def evaluate(self):
        
        tbl = []
        for row, agent, buildParameter, epoch, environment, trainer in self.app.runEvaluationWithSimulation(nSimulationStep = self.nSimulationStep):
            tbl.append(pandas.DataFrame([{**row, **buildParameter.__dict__, "epoch": epoch, "agentKey": agent.getAgentKey()}]))
        tbl = pandas.concat(tbl, axis=0)
        
        fileName = "work004_export_%s.csv" % datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        
        assert isinstance(tbl, pandas.DataFrame)
        
        tbl.to_csv(fileName)
        print(">> Evaluated simulation result was exported into the file: %s" % fileName)
        
        return fileName
    
    def generateBuildParameter(self):
        
        for _ in range(self.nAgent):
            buildParameter = ConcreteBuildParameter(nIntervalSave = self.nEpoch//2
                                                , nEpoch = self.nEpoch
                                                , label = "caseStudy001"
                                                , plantClass = "ConcretePlant001"
                                                , discountFactor = 0.5
                                                , alphaTemp = float(np.random.choice([1e-1, 1e+1]))
                                                , saveFolderPathAgent = "checkpoint"
                                                , nFeature = 1
                                                , nSampleOfActionsInValueFunctionApproximator = int(np.random.choice([2**0, 2**3]))
                                                , nHiddenValueFunctionApproximator = 2**5
                                                , nStepEnvironment = int(np.random.choice([2**0, 2**3]))
                                                , nStepGradient = int(np.random.choice([2**0, 2**3]))
                                                , nIntervalUpdateStateValueFunction = int(np.random.choice([2**0, 2**3]))
                                                , nIterationPerEpoch = 1
                                                , bufferSizeReplayBuffer = 2**10
                                                , featureExtractorClass = "ConcreteFeatureExtractor002")
            
            yield buildParameter