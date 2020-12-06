'''
Created on 2020/11/28

@author: ukai
'''
from concrete.concrete_build_parameter import ConcreteBuildParameter
from concrete.concrete_environment import ConcreteEnvironment
from concrete.concrete_plant001 import ConcretePlant001
from concrete.concrete_plant002 import ConcretePlant002
from concrete.concrete_plant003 import ConcretePlant003
from concrete.concrete_plant004 import ConcretePlant004
from framework.environment_factory import EnvironmentFactory


class ConcreteEnvironmentFactory(EnvironmentFactory):
    '''
    classdocs
    '''


    def create(self, buildParameter):
        assert isinstance(buildParameter, ConcreteBuildParameter)
        
        return ConcreteEnvironment(plant = self.createPlant(buildParameter))
        
        
    def createPlant(self, buildParameter):
        assert isinstance(buildParameter, ConcreteBuildParameter)
        
        if buildParameter.plantClass == "ConcretePlant001":
            return ConcretePlant001()
        if buildParameter.plantClass == "ConcretePlant002":
            return ConcretePlant002()
        if buildParameter.plantClass == "ConcretePlant003":
            return ConcretePlant003(amplitudePeriodicDv=2.0)
        if buildParameter.plantClass == "ConcretePlant004":
            return ConcretePlant004(amplitudePeriodicDv=2.0)
        
        assert False
        