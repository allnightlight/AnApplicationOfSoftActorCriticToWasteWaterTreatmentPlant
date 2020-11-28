'''
Created on 2020/11/28

@author: ukai
'''
from framework.agent_factory import AgentFactory
from concrete.concrete_build_parameter import ConcreteBuildParameter
from concrete.concrete_environment import ConcreteEnvironment
from concrete.concrete_agent import ConcreteAgent
from concrete.concrete_policy import ConcretePolicy
from concrete.concrete_value_function_approximator import ConcreteValueFunctionApproximator
from concrete.concrete_feature_extractor002 import ConcreteFeatureExtractor002

class ConcreteAgentFactory(AgentFactory):
    '''
    classdocs
    '''


    def create(self, buildParameter, environment):
        
        assert isinstance(buildParameter, ConcreteBuildParameter)
        assert isinstance(environment, ConcreteEnvironment)
        
        return ConcreteAgent(policy = self.createPolicy(buildParameter, environment)
                             , valueFunctionApproximator = self.createValueFunctionApproximator(buildParameter, environment)
                             , featureExtractor = self.createFeatureExtractor(buildParameter, environment)
                             , discountFactor = buildParameter.discountFactor
                             , alphaTemp = buildParameter.alphaTemp
                             , updatePolicyByAdvantage = False
                             , saveFolderPath = buildParameter.saveFolderPathAgent)
        
    def createPolicy(self, buildParameter, environment):
        return ConcretePolicy(nMv = environment.getNmv())
    
    def createValueFunctionApproximator(self, buildParameter, environment):
        
        if buildParameter.featureExtractorClass != "ConcreteFeatureExtractor002":
            nFeature = buildParameter.nFeature
        else:
            nFeature = environment.getNmv()
        
        return ConcreteValueFunctionApproximator(nFeature = nFeature
                                                 , nMv = environment.getNmv()
                                                 , nSampleOfActionsInValueFunctionApproximator = buildParameter.nSampleOfActionsInValueFunctionApproximator
                                                 , nHidden = buildParameter.nHiddenValueFunctionApproximator)
    
    def createFeatureExtractor(self, buildParameter, environment):
        return ConcreteFeatureExtractor002(nFeature = environment.getNmv())