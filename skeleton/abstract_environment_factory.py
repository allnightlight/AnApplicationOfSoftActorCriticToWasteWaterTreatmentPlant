'''
Created on 2020/11/11

@author: ukai
'''
from skeleton.abstract_environment import AbstractEnvironment
from skeleton.abstract_plant import AbstractPlant


class AbstractEnvironmentFactory(object):
    '''
    classdocs
    '''


    def create(self, context):
        return AbstractEnvironment(self.createPlant(context))    
    
    def createPlant(self, context):
        return AbstractPlant()