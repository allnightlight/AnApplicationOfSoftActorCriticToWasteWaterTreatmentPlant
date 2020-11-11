'''
Created on 2020/11/11

@author: ukai
'''
from skeleton.abstract_environment import AbstractEnvironment

class AbstractEnvironmentFactory(object):
    '''
    classdocs
    '''


    def create(self, context):
        return AbstractEnvironment()