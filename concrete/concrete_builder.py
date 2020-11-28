'''
Created on 2020/11/28

@author: ukai
'''
from framework.builder import Builder
from concrete.concrete_trainer_factory import ConcreteTrainerFactory
from concrete.concrete_agent_factory import ConcreteAgentFactory
from concrete.concrete_environment_factory import ConcreteEnvironmentFactory
from framework.mylogger import MyLogger

class ConcreteBuilder(Builder):
    '''
    classdocs
    '''


    def __init__(self, store, logger = MyLogger(console_print = True)):
        Builder.__init__(self
                         , trainerFactory = ConcreteTrainerFactory()
                         , agentFactory = ConcreteAgentFactory()
                         , environmentFactory = ConcreteEnvironmentFactory()
                         , store = store
                         , logger = logger)