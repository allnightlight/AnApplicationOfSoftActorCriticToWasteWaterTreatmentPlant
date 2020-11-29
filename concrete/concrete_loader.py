'''
Created on 2020/11/29

@author: ukai
'''
from concrete.concrete_agent_factory import ConcreteAgentFactory
from concrete.concrete_environment_factory import ConcreteEnvironmentFactory
from concrete.concrete_trainer_factory import ConcreteTrainerFactory
from framework.loader import Loader
from concrete.concrete_build_parameter_factory import ConcreteBuildParameterFactory


class ConcreteLoader(Loader):
    '''
    classdocs
    '''

    def __init__(self, store):
        Loader.__init__(self
                         , buildParameterFactory = ConcreteBuildParameterFactory()
                         , trainerFactory = ConcreteTrainerFactory()
                         , agentFactory = ConcreteAgentFactory()
                         , environmentFactory = ConcreteEnvironmentFactory()
                         , store = store)