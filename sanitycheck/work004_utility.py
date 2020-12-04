'''
Created on 2020/11/29

@author: ukai
'''
from datetime import datetime

import pandas

from concrete.concrete_application import ConcreteApplication
from concrete.concrete_build_parameter_factory import ConcreteBuildParameterFactory
from concrete.concrete_builder import ConcreteBuilder
from concrete.concrete_evaluation_db import ConcreteEvaluationDb
from concrete.concrete_loader import ConcreteLoader
from framework.store import Store
from sac.sac_evaluator import SacEvaluator
import os
from concrete.concrete_simulator_factory_for_evaluation import ConcreteSimulatorFactoryForEvaluation
from sanitycheck.work004_config import evaluateMethods, generateBuildParameter


class Work004Utility(object):
    '''
    classdocs
    '''
    
    @classmethod
    def create(cls, nAgent = 2**10, nEpoch = 2**11, nSimulationStep = 2**7):
        
        store = Store(dbPath = "trained_agent.sqlite", trainLogFolderPath = "tmpTrainLog")        
        builder = ConcreteBuilder(store)
        loader = ConcreteLoader(store)
        
        evaluationDbPath = "evaluationDb.sqlite"        
        evaluationDb = ConcreteEvaluationDb(evaluationDbPath = evaluationDbPath, buildParameterFactory = ConcreteBuildParameterFactory())
        if not os.path.exists(evaluationDbPath):
            evaluationDb.initDb()
        
        evaluator = SacEvaluator(simulatorFactory = ConcreteSimulatorFactoryForEvaluation(nSimulationStep = nSimulationStep))
        
        return Work004Utility(app =ConcreteApplication(builder, loader, evaluationDb, evaluator) 
                              , nAgent = nAgent
                              , nEpoch = nEpoch), store, evaluationDb

    def __init__(self, app, nAgent, nEpoch):
        '''
        Constructor
        '''
        
        assert isinstance(app, ConcreteApplication)
        self.app = app
        self.nAgent = nAgent
        self.nEpoch = nEpoch
        
    def build(self):
        
        for buildParameter in generateBuildParameter(nAgent = self.nAgent, nEpoch = self.nEpoch):
            self.app.runBuild(buildParameter)
        
    def evaluate(self):
        
        self.app.runEvaluationWithSimulation(evaluateMethods=evaluateMethods)
        tbl = self.app.exportEvaluationTable()
        
        tbl = pandas.concat([pandas.DataFrame([row]) for row in tbl], axis=0)
                
        fileName = "work004_export_%s.csv" % datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        
        assert isinstance(tbl, pandas.DataFrame)
        
        tbl.to_csv(fileName)
        print(">> Evaluated simulation result was exported into the file: %s" % fileName)
        
        return fileName