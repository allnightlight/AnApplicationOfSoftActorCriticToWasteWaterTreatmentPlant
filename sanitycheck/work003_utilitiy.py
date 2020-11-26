'''
Created on 2020/11/26

@author: ukai
'''
import numpy as np
import matplotlib.pylab as plt
from concrete.concrete_plant003 import ConcretePlant003
from builtins import isinstance

class Work003Utility(object):
    '''
    classdocs
    '''
    
    @classmethod
    def create(cls):
        plant = ConcretePlant003()
        
        return Work003Utility(plant = plant, nIter = 2**7)


    def __init__(self, plant, nIter):
        '''
        Constructor
        '''
        
        assert isinstance(plant, ConcretePlant003)
        
        self.plant = plant
        self.nIter = nIter
        
    def runSimulationCase001(self):
        
        self.plotPv(*self.runSimulationWithConstantMv(uConst = -1.5 * np.ones((1,1))))

    def runSimulationCase002(self):
        
        self.plotPv(*self.runSimulationWithConstantMv(uConst =  1.5 * np.ones((1,1))))

    def runSimulationCase003(self):
        
        self.plotPv(*self.runSimulationWithStepChangeMv())
        
    def runSimulationWithConstantMv(self, uConst):
        
        self.plant.reset()
        
        u =  uConst # (,)
        
        Pv = [self.plant.getNH4(),]
        Mv = []
        for _ in range(self.nIter):
            self.plant.update(u)
            Mv.append(u)
            Pv.append(self.plant.getNH4())

        Pv = np.array(Pv) # (nIter,)
        Mv = np.concatenate(Mv, axis=0) # (nIter,1)
        
        return Pv, Mv

    def runSimulationWithStepChangeMv(self):
        
        self.plant.reset()
                
        Pv = [self.plant.getNH4(),]
        Mv = []
        for k1 in range(self.nIter):
            if k1 < self.nIter//2:
                u = -1.5 * np.ones((1,1))
            else:
                u = 1.5 * np.ones((1,1))
            self.plant.update(u)
            Mv.append(u)
            Pv.append(self.plant.getNH4())

        Pv = np.array(Pv) # (nIter,)
        Mv = np.concatenate(Mv, axis=0) # (nIter,1)
        
        return Pv, Mv

    
    def plotPv(self, Pv, Mv):
        
        fig = plt.figure()
        assert isinstance(fig, plt.Figure)
        
        ax = fig.add_subplot(2,1,1)
        ax.plot(Pv, '-')
        ax.set_ylabel("NH4")
        
        ax = fig.add_subplot(2,1,2)
        ax.plot(Mv, '-')
        ax.set_ylabel("DO(normalized)")
        
        fig.tight_layout()
        plt.show()