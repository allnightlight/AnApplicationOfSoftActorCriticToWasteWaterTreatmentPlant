'''
Created on 2020/11/28

@author: ukai
'''
from framework.build_parameter_factory import BuildParameterFactory
from concrete.concrete_build_parameter import ConcreteBuildParameter

class ConcreteBuildParameterFactory(BuildParameterFactory):
    '''
    classdocs
    '''


    def create(self):
        return ConcreteBuildParameter()