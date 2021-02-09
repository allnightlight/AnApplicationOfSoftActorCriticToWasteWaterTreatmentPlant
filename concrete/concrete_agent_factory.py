'''
Created on 2020/11/28

@author: ukai
'''
from concrete.concrete_agent import ConcreteAgent
from concrete.concrete_build_parameter import ConcreteBuildParameter
from concrete.concrete_environment import ConcreteEnvironment
from concrete.concrete_feature_extractor002 import ConcreteFeatureExtractor002
from concrete.concrete_policy001 import ConcretePolicy001
from concrete.concrete_policy002 import ConcretePolicy002
from framework.agent_factory import AgentFactory
from concrete.concrete_value_function_approximator001 import ConcreteValueFunctionApproximator001
from concrete.concrete_value_function_approximator002 import ConcreteValueFunctionApproximator002
from concrete.concrete_policy004 import ConcretePolicy004
from concrete.concrete_policy005 import ConcretePolicy005


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
                             , saveFolderPath = buildParameter.saveFolderPathAgent
                             , learningRateForUpdateActionValueFunction = buildParameter.learningRateForUpdateActionValueFunction
                             , learningRateForUpdatePolicy = buildParameter.learningRateForUpdatePolicy
                             , learningRateForUpdateStateValueFunction = buildParameter.learningRateForUpdateStateValueFunction)
        
    def createPolicy(self, buildParameter, environment):

        policy = None
        if buildParameter.policyClass == "ConcretePolicy001":
            policy = ConcretePolicy001(nMv = environment.getNmv())
        if buildParameter.policyClass == "ConcretePolicy002":
            policy = ConcretePolicy002(nMv = environment.getNmv())            
        if buildParameter.policyClass == "ConcretePolicy004":
            policy = ConcretePolicy004(nFeature = buildParameter.nFeature
                                       , nMv = environment.getNmv()
                                       , nHidden = buildParameter.nHiddenAgent)
        if buildParameter.policyClass == "ConcretePolicy005":
            policy = ConcretePolicy005(nFeature = buildParameter.nFeature
                                       , nMv = environment.getNmv()
                                       , nHidden = buildParameter.nHiddenAgent)

        assert policy is not None
        return policy
    
    def createValueFunctionApproximator(self, buildParameter, environment):
        
        if buildParameter.featureExtractorClass != "ConcreteFeatureExtractor002":
            nFeature = buildParameter.nFeature
        else:
            nFeature = environment.getNpv()

        if buildParameter.valueFunctionApproximatorClass == "ConcreteValueFunctionApproximator001":        
            return ConcreteValueFunctionApproximator001(nFeature = nFeature
                                                 , nMv = environment.getNmv()
                                                 , nSampleOfActionsInValueFunctionApproximator = buildParameter.nSampleOfActionsInValueFunctionApproximator
                                                 , nHidden = buildParameter.nHiddenValueFunctionApproximator
                                                 , nRedundancy = buildParameter.nQfunctionRedundancy)

        if buildParameter.valueFunctionApproximatorClass == "ConcreteValueFunctionApproximator002":        
            return ConcreteValueFunctionApproximator002(nFeature = nFeature
                                                 , nMv = environment.getNmv()
                                                 , nSampleOfActionsInValueFunctionApproximator = buildParameter.nSampleOfActionsInValueFunctionApproximator
                                                 , nHidden = buildParameter.nHiddenValueFunctionApproximator
                                                 , nRedundancy = buildParameter.nQfunctionRedundancy)
    
    def createFeatureExtractor(self, buildParameter, environment):
        
        assert buildParameter.featureExtractorClass == "ConcreteFeatureExtractor002", """
        
The given featureExtractorClass: {featureExtractorClass} was not available so far.
Please, specify \"ConcreteFeatureExtractor002\" as the parameter of featureExtractorClass in your buildParameter.
 
""".format(featureExtractorClass = buildParameter.featureExtractorClass)

        if buildParameter.nFeature != environment.getNpv():
            print("""\
You specified nFeature = {nFeature}, though, this setting would be ignored
since the ConcreteFeatureExtractor002 could only accept nPv = {nPv} as nFeature.
""".format(nFeature = buildParameter.nFeature, nPv = environment.getNpv()))
            
        return ConcreteFeatureExtractor002(nFeature = environment.getNpv())