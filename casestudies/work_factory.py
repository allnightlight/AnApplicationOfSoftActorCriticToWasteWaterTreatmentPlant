'''
Created on 2020/12/07

@author: ukai
'''
from datetime import timedelta
import os

from casestudies.work001 import Work001
from casestudies.work002 import Work002
from casestudies.work003 import Work003
from casestudies.work004 import Work004
from casestudies.work005 import Work005
from casestudies.work006 import Work006
from casestudies.work007 import Work007
from casestudies.work008 import Work008
from casestudies.work009 import Work009
from casestudies.work900 import Work900
from casestudies.work901 import Work901
from casestudies.work902 import Work902
from casestudies.work903 import Work903
from casestudies.work904 import Work904
from casestudies.work905 import Work905
from casestudies.work906 import Work906
from casestudies.work907 import Work907
from casestudies.work908 import Work908
from casestudies.work_template import WorkTemplate
from concrete.concrete_application import ConcreteApplication
from concrete.concrete_build_parameter_factory import ConcreteBuildParameterFactory
from concrete.concrete_builder import ConcreteBuilder
from concrete.concrete_evaluation_db import ConcreteEvaluationDb
from concrete.concrete_loader import ConcreteLoader
from concrete.concrete_simulator_factory_for_evaluation import ConcreteSimulatorFactoryForEvaluation
from framework.store import Store
from sac.sac_evaluator import SacEvaluator
from casestudies.work010 import Work010


class WorkFactory(object):
    '''
    classdocs
    '''


    def create(self, workName, nSimulationStep = 96*12, nEpoch = None, nAgent = 2**10, saveFolderPathAgent = "checkpoint",  updateEvaluationInterval = timedelta(seconds = 5), nUpdateEvaluation = None, figSize = [12,8], figFolderPath = "./fig", nSampleOverLearningCurve = 2**3, showProgress = True, maxNumOfEvaluateAgents = 2**4):
        
        store = Store(dbPath = "trained_agent.sqlite", trainLogFolderPath = "tmpTrainLog")        
        builder = ConcreteBuilder(store)
        loader = ConcreteLoader(store)
        
        evaluationDbPath = "evaluationDb.sqlite"        
        evaluationDb = ConcreteEvaluationDb(evaluationDbPath = evaluationDbPath, buildParameterFactory = ConcreteBuildParameterFactory())
        if not os.path.exists(evaluationDbPath):
            evaluationDb.initDb()
        
        evaluator = SacEvaluator(simulatorFactory = ConcreteSimulatorFactoryForEvaluation(nSimulationStep = nSimulationStep))

        app = ConcreteApplication(builder, loader, evaluationDb, evaluator, showProgress, maxNumOfEvaluateAgents)

#         workInstance = WorkTemplate(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        workInstance = None
        
        if workName == "work001":
                    
            workInstance = Work001(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work002":
                    
            workInstance = Work002(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath, nSampleOverLearningCurve = nSampleOverLearningCurve)

        if workName == "work003":
                    
            workInstance = Work003(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work004":
                    
            workInstance = Work004(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work005":
                    
            workInstance = Work005(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work006":
                    
            workInstance = Work006(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work007":
                    
            workInstance = Work007(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work008":
                    
            workInstance = Work008(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work009":
                    
            workInstance = Work009(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work010":
                    
            workInstance = Work010(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)
            
        if workName == "work900":
                    
            workInstance = Work900(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work901":
                    
            workInstance = Work901(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work902":
                    
            workInstance = Work902(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work903":
                    
            workInstance = Work903(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work904":
                    
            workInstance = Work904(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work905":
                    
            workInstance = Work905(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work906":
                    
            workInstance = Work906(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work907":
                    
            workInstance = Work907(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        if workName == "work908":
                    
            workInstance = Work908(app, store, evaluationDb, nEpoch, nAgent, saveFolderPathAgent, updateEvaluationInterval, nUpdateEvaluation, figSize, figFolderPath)

        assert isinstance(workInstance, WorkTemplate)         
        return  workInstance