'''
Created on 2020/07/09

@author: ukai
'''
from builtins import isinstance

from framework.agent import Agent
from framework.agent_factory import AgentFactory
from framework.build_parameter import BuildParameter
from framework.environment_factory import EnvironmentFactory
from framework.store import Store
from framework.store_field import StoreField
from framework.trainer_factory import TrainerFactory


class Builder(object):
    '''
    classdocs
    '''


    def __init__(self, trainerFactory, agentFactory, environmentFactory, store, logger):
        '''
        Constructor
        '''
        
        assert isinstance(trainerFactory, TrainerFactory)
        assert isinstance(agentFactory, AgentFactory)
        assert isinstance(environmentFactory, EnvironmentFactory)
        assert isinstance(store, Store)
        
        self.environmentFactory = environmentFactory
        self.agentFactory = agentFactory
        self.trainerFactory = trainerFactory
        self.store = store
        self.logger = logger
                

    # <<public>>        
    def build(self, buildParameter):
        isinstance(buildParameter, BuildParameter)

        environment = self.environmentFactory.create(buildParameter)
        agent = self.agentFactory.create(buildParameter, environment)                
        trainer = self.trainerFactory.create(buildParameter, agent, environment)
        
        nEpoch = buildParameter.nEpoch
        nIntervalSave = buildParameter.nIntervalSave
        
        trainer.trainPreprocess()
        
        epoch = 0
        self.save(agent, buildParameter, epoch)
        self.logger.info(agent, buildParameter, environment, epoch, trainer)
            
        while True:
            if epoch >= nEpoch:
                break
            else:
                nEpochLoc = min(nIntervalSave, nEpoch - epoch)
                for _ in range(nEpochLoc):
                    trainer.train()
                    epoch += 1
                self.save(agent, buildParameter, epoch)
                self.logger.info(agent, buildParameter, environment, epoch, trainer)

    
    # <<private>>
    def save(self, agent, buildParameter, epoch):
        
        assert isinstance(agent, Agent)
        assert isinstance(buildParameter, BuildParameter)
        
        agentMemento = agent.createMemento()
        buildParameterMemento = buildParameter.createMemento()
        buildParameterKey = buildParameter.key
        buildParameterLabel = buildParameter.label
        agentKey = agent.getAgentKey()
                        
        storeField = StoreField(agentMemento, epoch, buildParameterMemento, buildParameterKey, buildParameterLabel, agentKey)
        self.store.append(storeField)