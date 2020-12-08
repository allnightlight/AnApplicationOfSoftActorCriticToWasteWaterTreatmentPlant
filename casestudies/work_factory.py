'''
Created on 2020/12/07

@author: ukai
'''
from datetime import timedelta
import os

from casestudies.work_template import WorkTemplate
from concrete.concrete_build_parameter_factory import ConcreteBuildParameterFactory
from concrete.concrete_builder import ConcreteBuilder
from concrete.concrete_evaluation_db import ConcreteEvaluationDb
from concrete.concrete_loader import ConcreteLoader
from concrete.concrete_simulator_factory_for_evaluation import ConcreteSimulatorFactoryForEvaluation
from framework.store import Store
from sac.sac_evaluator import SacEvaluator
from concrete.concrete_application import ConcreteApplication
from casestudies.work001 import Work001
from casestudies.work002 import Work002


class WorkFactory(object):
    '''
    classdocs
    '''


    def create(self, workName, nSimulationStep = 96*12, nEpoch = 2**12, nAgent = 2**10, saveFolderPathAgent = "checkpoint",  updateEvaluationInterval = timedelta(seconds = 5), nUpdateEvaluation = None, figSize = [12,8], figFolderPath = "./fig", nSampleOverLearningCurve = 2**3):
        
        store = Store(dbPath = "trained_agent.sqlite", trainLogFolderPath = "tmpTrainLog")        
        builder = ConcreteBuilder(store)
        loader = ConcreteLoader(store)
        
        evaluationDbPath = "evaluationDb.sqlite"        
        evaluationDb = ConcreteEvaluationDb(evaluationDbPath = evaluationDbPath, buildParameterFactory = ConcreteBuildParameterFactory())
        if not os.path.exists(evaluationDbPath):
            evaluationDb.initDb()
        
        evaluator = SacEvaluator(simulatorFactory = ConcreteSimulatorFactoryForEvaluation(nSimulationStep = nSimulationStep))

        app = ConcreteApplication(builder, loader, evaluationDb, evaluator)

#         workInstance = WorkTemplate(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work001":
                    
            workInstance = Work001(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work002":
                    
            workInstance = Work002(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath, nSampleOverLearningCurve = nSampleOverLearningCurve)

        assert isinstance(workInstance, WorkTemplate)         
        return  workInstance