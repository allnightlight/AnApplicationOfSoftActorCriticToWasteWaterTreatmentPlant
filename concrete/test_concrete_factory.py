'''
Created on 2020/11/28

@author: ukai
'''
import unittest
from concrete.concrete_environment_factory import ConcreteEnvironmentFactory
from concrete.concrete_build_parameter_factory import ConcreteBuildParameterFactory
from concrete.concrete_environment import ConcreteEnvironment
from concrete.concrete_agent_factory import ConcreteAgentFactory
from concrete.concrete_agent import ConcreteAgent
from concrete.concrete_trainer import ConcreteTrainer
from concrete.concrete_trainer_factory import ConcreteTrainerFactory
from concrete.concrete_build_parameter import ConcreteBuildParameter
import traceback


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.buildParameterFactory = ConcreteBuildParameterFactory()
        self.environmentFactory = ConcreteEnvironmentFactory()
        self.agentFactory = ConcreteAgentFactory()
        self.trainerFactory = ConcreteTrainerFactory()


    def test001(self):
        
        buildParameter = self.buildParameterFactory.create()
        environment = self.environmentFactory.create(buildParameter)
        
        assert isinstance(environment, ConcreteEnvironment)
        
        agent = self.agentFactory.create(buildParameter, environment)
        
        assert isinstance(agent, ConcreteAgent)
        
        trainer = self.trainerFactory.create(buildParameter, agent, environment)
        
        assert isinstance(trainer, ConcreteTrainer)

    def test002(self):
        
        buildParameter: ConcreteBuildParameter = self.buildParameterFactory.create()
        environment: ConcreteEnvironment = self.environmentFactory.create(buildParameter)
        
        try:
            buildParameter.featureExtractorClass = "ConcreteFeatureExtractor001"        
            self.agentFactory.create(buildParameter, environment)
            assert False
        except :
            traceback.print_exc()
            assert True

        buildParameter.featureExtractorClass = "ConcreteFeatureExtractor002"        
        self.agentFactory.create(buildParameter, environment)
        assert True

        buildParameter.nFeature = 99
        self.agentFactory.create(buildParameter, environment)
        assert True
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()