'''
Created on 2020/11/27

@author: ukai
'''
from sac.sac_environment import SacEnvironment
from framework.environment import Environment

class ConcreteEnvironment(SacEnvironment, Environment):
    '''
    classdocs
    '''


    def __init__(self, plant):
        SacEnvironment.__init__(self, plant)