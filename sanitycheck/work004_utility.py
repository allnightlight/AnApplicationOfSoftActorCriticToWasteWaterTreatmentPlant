'''
Created on 2020/11/29

@author: ukai
'''
from datetime import datetime, timedelta
import os
import time

import pandas

from concrete.concrete_application import ConcreteApplication
from concrete.concrete_build_parameter_factory import ConcreteBuildParameterFactory
from concrete.concrete_builder import ConcreteBuilder
from concrete.concrete_evaluate_method001 import ConcreteEvaluateMethod001
from concrete.concrete_evaluation_db import ConcreteEvaluationDb
from concrete.concrete_loader import ConcreteLoader
from concrete.concrete_simulator_factory_for_evaluation import ConcreteSimulatorFactoryForEvaluation
from framework.store import Store
from sac.sac_evaluator import SacEvaluator
from sanitycheck.work004_config import evaluateMethods, generateBuildParameter, \
    buildParameterLabel, nSimulationStep


class Work004Utility(object):
    '''
    classdocs
    '''
    
    @classmethod
    def create(cls, updateEvaluationInterval = timedelta(seconds = 5), nUpdateEvaluation = None):
        
        store = Store(dbPath = "trained_agent.sqlite", trainLogFolderPath = "tmpTrainLog")        
        builder = ConcreteBuilder(store)
        loader = ConcreteLoader(store)
        
        evaluationDbPath = "evaluationDb.sqlite"        
        evaluationDb = ConcreteEvaluationDb(evaluationDbPath = evaluationDbPath, buildParameterFactory = ConcreteBuildParameterFactory())
        if not os.path.exists(evaluationDbPath):
            evaluationDb.initDb()
        
        evaluator = SacEvaluator(simulatorFactory = ConcreteSimulatorFactoryForEvaluation(nSimulationStep = nSimulationStep))
        
        return Work004Utility(app = ConcreteApplication(builder, loader, evaluationDb, evaluator)\
                              , figSize = [12,8], figFolderPath = "./fig", updateEvaluationInterval = updateEvaluationInterval, nUpdateEvaluation = nUpdateEvaluation), store, evaluationDb

    def __init__(self, app, figSize, figFolderPath, updateEvaluationInterval, nUpdateEvaluation):
        '''
        Constructor
        '''
        
        assert isinstance(app, ConcreteApplication)
        self.app = app
        self.figFolderPath = figFolderPath
        self.figSize = figSize
        self.updateEvaluationInterval = updateEvaluationInterval
        self.nUpdateEvaluation = nUpdateEvaluation
        
    def build(self):
        
        for buildParameter in generateBuildParameter():
            self.app.runBuild(buildParameter)
        
    def evaluate(self):
        
        fileName = "work004_export_%s.csv" % datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')

        cnt = 0
        while True:
                        
            self.app.runEvaluationWithSimulation(evaluateMethods=evaluateMethods, buildParameterLabel=buildParameterLabel)
            tbl = self.app.exportEvaluationTable(buildParameterLabel=buildParameterLabel)
            
            tbl = pandas.concat([pandas.DataFrame([row]) for row in tbl], axis=0)
            
            assert isinstance(tbl, pandas.DataFrame)
            
            tbl.to_csv(fileName)
            print(">> Updated evaluation table and exported the file: %s" % fileName)
                        
            if (self.nUpdateEvaluation is not None) and cnt >= self.nUpdateEvaluation:
                break
            else:
                cnt += 1
                time.sleep(self.updateEvaluationInterval.total_seconds())
        
        return fileName
    
    def exportSimulationResultAsFigure(self, agentKey, epoch):
        
        self.app.runEvaluationWithSimulation(evaluateMethods = [ConcreteEvaluateMethod001(self.figSize, self.figFolderPath, useDeterministicAction = True)]
                                             , epoch = epoch, agentKey = agentKey)        
        tbl = self.app.exportEvaluationTable(buildParameterLabel="%", agentKey=agentKey, epoch=epoch, evaluatorClass="ConcreteEvaluateMethod001")
        figFilePath = tbl[0]["evaluationValue"]
        print(">> Exported the simulation result in the file: %s" % figFilePath)
        
        return figFilePath