'''
Created on 2020/12/07

@author: ukai
'''
from datetime import  datetime
import os
import shutil
import time

import pandas

from casestudies.myEvaluateMethods import MyEvaluateMethod001
from concrete.concrete_application import ConcreteApplication
from concrete.concrete_build_parameter import ConcreteBuildParameter
from concrete.concrete_evaluate_method001 import ConcreteEvaluateMethod001
from concrete.concrete_evaluate_method002 import ConcreteEvaluateMethod002
from concrete.concrete_evaluation_db import ConcreteEvaluationDb
from framework.store import Store
import numpy as np


class WorkTemplate(object):
    '''
    classdocs
    '''


    def __init__(self, app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath):
        
        assert isinstance(app, ConcreteApplication)
        assert isinstance(store, Store)
        assert isinstance(evaluationDb, ConcreteEvaluationDb)
        
        self.app = app
        self.store = store
        self.evaluationDb = evaluationDb
        self.nAgent = nAgent
        self.nEpoch = nEpoch
        self.saveFolderPathAgent = saveFolderPathAgent
        self.updateEvaluationInterval = updateEvaluationInterval
        self.nUpdateEvaluation = nUpdateEvaluation
        self.workName = self.__class__.__name__
        self.figSize = figSize
        self.figFolderPath = figFolderPath

    # <<public, final>>
    def build(self):
        
        for buildParameter in self.generateBuildParameter():
            self.app.runBuild(buildParameter)

    
    # <<public, final>>
    def evaluate(self):
        
        fileName = self.workName + "_evaluation_table_%s.csv" % datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')

        cnt = 0
        while True:
                        
            self.app.runEvaluationWithSimulation(evaluateMethods=self.getEvaluateMethods(), buildParameterLabel=self.workName)
            tbl = self.app.exportEvaluationTable(buildParameterLabel=self.workName)
            
            if len(tbl) == 0:
                time.sleep(self.updateEvaluationInterval.total_seconds())
                continue
            
            tbl = pandas.concat([pandas.DataFrame([row]) for row in tbl], axis=0)
            
            assert isinstance(tbl, pandas.DataFrame)
            
            tbl.to_csv(fileName)
            print(">> Updated evaluation table and exported the file: %s" % fileName)
                        
            if (self.nUpdateEvaluation is not None) and cnt >= self.nUpdateEvaluation:
                break
            else:
                cnt += 1
                time.sleep(self.updateEvaluationInterval.total_seconds())
        
    
    # <<public, final>>
    def exportSimulationResultAsFigure(self, agentKey, epoch):
        
        self.app.runEvaluationWithSimulation(evaluateMethods = [ConcreteEvaluateMethod001(self.figSize, self.figFolderPath, useDeterministicAction = True)]
                                             , epoch = epoch, agentKey = agentKey)        
        tbl = self.app.exportEvaluationTable(buildParameterLabel="%", agentKey=agentKey, epoch=epoch, evaluatorClass="ConcreteEvaluateMethod001")
        for row in tbl:
            figFilePath = row["evaluationValue"]
            agentKey = row["agentKey"]
            epoch = row["epoch"]
            print(">> Exported the simulation result of Agent: %s at epoch = %d in the file: %s" % (agentKey, epoch, figFilePath))        
        
    # <<public, final>>
    def exportSimulationResultAsCsvFormatFile(self, agentKey, epoch):
        
        self.app.runEvaluationWithSimulation(evaluateMethods = [ConcreteEvaluateMethod002(self.figFolderPath)]
                                             , epoch = epoch, agentKey = agentKey)
        tbl = self.app.exportEvaluationTable(buildParameterLabel="%", agentKey=agentKey, epoch=epoch, evaluatorClass="ConcreteEvaluateMethod002")
        
        for row in tbl:
            dataFilePath = row["evaluationValue"]
            agentKey = row["agentKey"]
            epoch = row["epoch"]
            print(">> Exported the simulation result of Agent: %s at epoch = %d in the file: %s" % (agentKey, epoch, dataFilePath))        
    
    # <<public, final>>
    def clean(self):
        
        self.evaluationDb.removeRemainedFiles()
        self.store.removeHistory()
        for folderPath in [self.saveFolderPathAgent, self.figFolderPath]:
            if os.path.exists(folderPath):
                shutil.rmtree(folderPath)
        return
    
    # <<protected, abstract>>
    def generateBuildParameter(self):
        
        for _ in range(self.nAgent):
            buildParameter = ConcreteBuildParameter(nIntervalSave = self.nEpoch//2
                                            , nEpoch = self.nEpoch
                                            , label = self.workName
                                            , plantClass = "ConcretePlant003"
                                            , discountFactor = 0.9
                                            , alphaTemp = float(np.random.choice([1e-1, 1e+1]))
                                            , saveFolderPathAgent = self.saveFolderPathAgent
                                            , nFeature = 1
                                            , nSampleOfActionsInValueFunctionApproximator = int(np.random.choice([2**0, 2**3]))
                                            , nHiddenValueFunctionApproximator = 2**5
                                            , nStepEnvironment = 1
                                            , nStepGradient = int(np.random.choice([2**0, 2**3]))
                                            , nIntervalUpdateStateValueFunction = int(np.random.choice([2**0, 2**3]))
                                            , nIterationPerEpoch = 1
                                            , bufferSizeReplayBuffer = 2**10
                                            , featureExtractorClass = "ConcreteFeatureExtractor002"
                                            , learningRateForUpdateActionValueFunction = 1e-3
                                            , learningRateForUpdatePolicy = 1e-3
                                            , learningRateForUpdateStateValueFunction = float(np.random.choice([1e-3, 1e-4])))
        
        yield buildParameter
        
    # <<protected, abstract>>
    def getEvaluateMethods(self):
        
        return [MyEvaluateMethod001(),]