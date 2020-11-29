'''
Created on 2020/11/29

@author: ukai
'''
from concrete.concrete_application import ConcreteApplication
import pandas
from datetime import datetime
from concrete.concrete_builder import ConcreteBuilder
from concrete.concrete_loader import ConcreteLoader
from sac.sac_evaluator import SacEvaluator
from framework.store import Store

class Work004Utility(object):
    '''
    classdocs
    '''
    
    @classmethod
    def create(cls):
        
        store = Store(dbPath = "trained_agent.sqlite", trainLogFolderPath = "tmpTrainLog")        
        builder = ConcreteBuilder(store)
        loader = ConcreteLoader(store)
        evaluators = [SacEvaluator(),]
        
        return Work004Utility(app = ConcreteApplication(builder, loader, evaluators)), store


    def __init__(self, app):
        '''
        Constructor
        '''
        
        assert isinstance(app, ConcreteApplication)
        self.app = app
        
    def build(self, buildParameter):
        
        self.app.runBuild(buildParameter)
        
    def evaluate(self):
        
        tbl = []
        for row, agent, buildParameter, epoch, environment, trainer in self.app.runEvaluationWithSimulation(nSimulationStep = 1):
            tbl.append(pandas.DataFrame([{**row, **buildParameter.__dict__, "epoch": epoch, "agentKey": agent.getAgentKey()}]))
        tbl = pandas.concat(tbl, axis=0)
        
        fileName = "work004_export_%s.csv" % datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        
        assert isinstance(tbl, pandas.DataFrame)
        
        tbl.to_csv(fileName)
        print(">> Evaluated simulation result was exported into the file: %s" % fileName)
        
        return fileName