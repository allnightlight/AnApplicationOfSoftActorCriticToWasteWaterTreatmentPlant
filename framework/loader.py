'''
Created on 2020/07/10

@author: ukai
'''
from framework.agent_factory import AgentFactory
from framework.environment_factory import EnvironmentFactory
from framework.store import Store
from framework.trainer_factory import TrainerFactory


class Loader(object):
    '''
    classdocs
    '''


    def __init__(self, agentFactory, buildParameterFactory, environmentFactory, trainerFactory, store):
        '''
        Constructor
        '''
        
        assert isinstance(agentFactory, AgentFactory)
        assert isinstance(environmentFactory, EnvironmentFactory)
        assert isinstance(trainerFactory, TrainerFactory)        
        assert isinstance(store, Store)
        
        self.agentFactory = agentFactory
        self.environmentFactory = environmentFactory
        self.trainerFactory = trainerFactory
        self.buildParameterFactory = buildParameterFactory
        self.store = store        
        
    def load(self, buildParameterLabel = "%", epoch = None, buildParameterKey = None, agentKey = None):
        
        self.store.update_db()
        
        for storeField in self.store.restore(buildParameterLabel, epoch, buildParameterKey, agentKey):
            buildParameter = self.buildParameterFactory.create()            
            buildParameter.loadMemento(storeField.buildParameterMemento)
            
            environment = self.environmentFactory.create(buildParameter)
            agent = self.agentFactory.create(buildParameter, environment)
            agent.loadMemento(storeField.agentMemento)
            
            trainer = self.trainerFactory.create(buildParameter, agent, environment)
            
            epoch = storeField.epoch
            
            yield agent, buildParameter, epoch, environment, trainer