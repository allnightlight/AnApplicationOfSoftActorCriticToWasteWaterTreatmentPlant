'''
Created on 2020/07/09

@author: ukai
'''
from framework.agent import Agent
from framework.build_parameter import BuildParameter


class AgentFactory(object):
    '''
    classdocs
    '''


    def create(self, buildParameter, environment):
        isinstance(buildParameter, BuildParameter)
        
        agent = Agent()
        
        return agent        