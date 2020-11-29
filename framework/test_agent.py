'''
Created on 2020/07/09

@author: ukai
'''
from builtins import isinstance
import unittest

from framework.agent import Agent


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        agent = Agent()
        
        self.agents = [agent,]


    def test001(self):
        
        for agent in self.agents:
            
            assert isinstance(agent, Agent)
            agentMemento = agent.createMemento()
            
            agent2 = Agent()
            
            agent2.loadMemento(agentMemento, agent.getAgentKey())

            assert agent.getAgentKey() == agent2.getAgentKey()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()