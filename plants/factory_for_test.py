'''
Created on 2020/11/23

@author: ukai
'''
import tensorflow

from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
import numpy as np
from plants.concrete_plant001 import ConcretePlant001
from plants.concrete_plant002 import ConcretePlant002
from skeleton.abstract_environment import AbstractEnvironment


class FactoryForTest(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
    def createPlant001(self):
        
        return ConcretePlant001()
    
    def createEnvironmentPoweredByPlant001(self):
        
        return AbstractEnvironment(plant = ConcretePlant001())
    
    def generateBatchDataAgentForPlant001(self):
        
        nMv = 1
        nBatch = 1
        
        for _ in range(10):
            yield ConcreteBatchDataAgent(_Mean = tensorflow.random.normal(shape = (nBatch, nMv))
                                     , _LogSd = tensorflow.random.normal(shape = (nBatch, nMv)))            
            
    def createPlant002(self):
        
        return ConcretePlant002()
    
    def createEnvironmentPoweredByPlant002(self):
        
        return AbstractEnvironment(plant = ConcretePlant002())
    
    def generateBatchDataAgentForPlant002(self):
        
        nMv = 1
        nBatch = 1
        
        for _ in range(10):
            yield ConcreteBatchDataAgent(_Mean = tensorflow.random.normal(shape = (nBatch, nMv))
                                     , _LogSd = tensorflow.random.normal(shape = (nBatch, nMv)))