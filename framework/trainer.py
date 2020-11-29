'''
Created on 2020/07/09

@author: ukai
'''
from framework.agent import Agent
from framework.environment import Environment


class Trainer(object):
    '''
    classdocs
    '''
    
    def __init__(self, agent, environment):
        assert isinstance(agent, Agent)
        assert isinstance(environment, Environment)
        self.agent = agent
        self.environment = environment
        
    # <<public>>
    def train(self):
        return
        
    # <<public>>
    def trainPreprocess(self):
        return