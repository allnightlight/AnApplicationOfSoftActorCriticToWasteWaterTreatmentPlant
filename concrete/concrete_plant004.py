'''
Created on 2020/12/06

@author: ukai
'''
from concrete.concrete_plant003 import ConcretePlant003
from concrete.wwtp_domain_knowledge import WwtpDomainKnowledge


class ConcretePlant004(ConcretePlant003):
    '''
    classdocs
    '''


    def __init__(self, h=15 / 60 / 24, volume=12, flow=24, rho=1 / 24, amplitudePeriodicDv=1.0, SvNh4=3.0, thresholdDo=1.5, maxDo=3.0, minDo=0.0, weightOnMv = 0.0, domainKnoledge = WwtpDomainKnowledge()):
        ConcretePlant003.__init__(self, h=h, volume=volume, flow=flow, rho=rho, amplitudePeriodicDv=amplitudePeriodicDv, SvNh4=SvNh4, thresholdDo=thresholdDo, maxDo=maxDo, minDo=minDo, weightOnMv=weightOnMv, domainKnoledge=domainKnoledge)
        
    
    def getReward(self, xPrev, Do, xNext):
    
        S_NH4 = xNext[self.idxNH4] # (,)
        
        if S_NH4 > self.SvNh4:
            cost = S_NH4 - self.SvNh4 + Do
        else:
            cost = Do
        
        return -cost    
