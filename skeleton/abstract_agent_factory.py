'''
Created on 2020/11/10

@author: ukai
'''
from skeleton.abstract_agent import AbstractAgent
from skeleton.abstract_policy import AbstractPolicy
from skeleton.abstract_value_function_approximator import AbstractValueFunctionApproximator
from skeleton.abstract_feature_extractor import AbstractFeatureExtractor

class AbstractAgentFactory(object):
    '''
    classdocs
    '''


    def create(self, context):
        
        return AbstractAgent(policy = AbstractPolicy()
                             , valueFunctionApproximator = AbstractValueFunctionApproximator()
                             , featureExtractor = AbstractFeatureExtractor()
                             , discountFactor = context.discountFactor)