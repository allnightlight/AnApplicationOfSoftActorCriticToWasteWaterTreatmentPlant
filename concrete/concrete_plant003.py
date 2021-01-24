'''
Created on 2020/11/26

@author: ukai
'''
from scipy.integrate import ode

from concrete.concrete_batch_data_reward import ConcreteBatchDataReward
import numpy as np
from sac.sac_plant import SacPlant
from concrete.wwtp_domain_knowledge import WwtpDomainKnowledge


class ConcretePlant003(SacPlant):
    '''
    classdocs
    '''

    def __init__(self, h = 15/60/24, volume = 12, flow = 24, rho = 1/24, amplitudePeriodicDv = 1.0, SvNh4 = 3.0, thresholdDo = 1.5, maxDo = 3.0, minDo = 0.0, weightOnMv = 0.0, domainKnoledge = WwtpDomainKnowledge()):
        super(ConcretePlant003, self).__init__()
        '''
        Constructor
        the unit of h is [day]
        '''
        
        self.domainKnoledge: WwtpDomainKnowledge = domainKnoledge
                
        self.odeHandler = ode(self.f)        
        self.t = None # (,)
        self.x = None # (*,)
        self.h = h
        self.flow = flow
        self.volume = volume
        self.rho = rho
        self.amplitudePeriodicDv = amplitudePeriodicDv
        self.idxNH4 = self.domainKnoledge.getAsmVarNames().index("S_NH4")
        self.SvNh4 = SvNh4
        self.thresholdDo = thresholdDo
        self.maxDo = maxDo
        self.minDo = minDo
        
        self.nAsm = len(self.domainKnoledge.getAsmVarNames())
        
        self.weightOnMv = weightOnMv

    def getPv(self):
            
        S_NH4 =self.x[self.idxNH4] # (,)
        e = S_NH4 - self.SvNh4 # (,)
        e = e.reshape(1,1).astype(np.float32) # (1,1)
        
        return e # (1,1)        
    
    def getNH4(self):
        return self.x[self.idxNH4]
    
    def reset(self):        
        self.t = 0
        self.x = np.array(self.domainKnoledge.getSteadyStateOfAerobicTank() + [0.,], dtype=np.float)
                
    def update(self, u):
        # u: (1, 1)
        '''
        The given variable u has an unlimited continuous value.
        The value beyond the interval [-threshold, +threshold] is truncated 
        and then it's converted into DO as follow:
        if u > threshold, then DO = 3.0
        else u < -threshold, then DO = 0.0
        otherwise, DO has the value with linearly proportion to the value of u.
        Do is used as a manipulated value.          
        '''
        
        if u[0,0] > self.thresholdDo:
            Do = self.maxDo
        elif u[0,0] < -self.thresholdDo:
            Do = self.minDo
        else:
            Do = (u[0,0] + self.thresholdDo)/(2*self.thresholdDo) * (self.maxDo - self.minDo) + self.minDo
        Mv = Do
        
        Dv = self.generateDv() # (nAsm,)
        
        xPrev = self.x
        
        self.odeHandler.set_initial_value(self.x, self.t)
        self.odeHandler.set_f_params(Dv, Mv)
        self.odeHandler.integrate(self.t + self.h)
        self.t = self.t + self.h
        self.x = self.odeHandler.y
        
        excess_u = np.abs(u[0,0]) - self.thresholdDo if np.abs(u[0,0]) > self.thresholdDo else 0.
                
        reward = (1-self.weightOnMv) * self.getReward(xPrev = xPrev, Do = Do, xNext = self.x) + self.weightOnMv * (-excess_u)  
                
        return ConcreteBatchDataReward(reward = np.array(reward).reshape(1,-1).astype(np.float32))

    def getNmv(self):
        return 1 # DO
    
    def getNpv(self):
        return 1 # deviation of NH4 beyond SV

    def getReward(self, xPrev, Do, xNext):
        
        S_NH4 = xNext[self.idxNH4] # (,)
        
        if S_NH4 > self.SvNh4:
            cost = S_NH4 - self.SvNh4
        else:
            cost = Do
        
        return -cost    
    
    def f(self, t, x, Dv, Mv):
        # x: (nAsm+1,)
        # Dv: (*, ), Mv: (*, )
        
        xAsm = x[:self.nAsm] # (nAsm,)
        errIntegral = x[self.nAsm] # (,)
        xAsmInflow = Dv # (nAsm,)
        Do = Mv # (,)
        
        dxdt = np.zeros(self.nAsm+1) # (nAsm+1,)
        dxAsmdt = dxdt[:self.nAsm] # (nAsm,)
        retentionTime = self.volume/self.flow
        
        # Volume * dX/dt = 
        #    Xinflow * flow
        #    - X * flow
        #    + (1-rho) * flow
        #    + ASM(S, X) * Volume

        # Volume * dS/dt = 
        #    Sinflow * flow
        #    - S * flow
        #    + ASM(S, X) * Volume
        #
        # dSO2/dt += Gain * max(DO - SO2, 0)
        
        dxAsmdt += xAsmInflow/retentionTime # (nAsm,)
        dxAsmdt[self.domainKnoledge.getIsSoluble()] -= xAsm[self.domainKnoledge.getIsSoluble()]/retentionTime # (nS,)
        dxAsmdt[~self.domainKnoledge.getIsSoluble()] -= self.rho * xAsm[~self.domainKnoledge.getIsSoluble()]/retentionTime # (nX,)
        
        dxAsmdtAsm, derrIntegraldt = self.domainKnoledge.getBiologicalProcessWithDoControl(*xAsm, errIntegral, Do)        
        dxAsmdt += np.array(dxAsmdtAsm) # (nAsm,)
        
        dxdt[self.nAsm] = derrIntegraldt
        
        return dxdt # (nAsm,)
    
    def generateDv(self):
        
        xInflow = np.array(self.domainKnoledge.getDefaultInflow()) # (nAsm,)
        Dv = xInflow * np.exp(np.log(self.amplitudePeriodicDv) * np.sin(np.pi * 2 * (self.t % 1.0))) # (nAsm,)
        
        return Dv