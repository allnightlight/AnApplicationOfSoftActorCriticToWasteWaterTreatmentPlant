'''
Created on 2020/07/09

@author: ukai
'''
from framework.build_parameter import BuildParameter
from framework.environment import Environment


class EnvironmentFactory(object):
    '''
    classdocs
    '''

        
    def create(self, buildParameter):
        isinstance(buildParameter, BuildParameter)
        
        environment = Environment()
        
        return environment
