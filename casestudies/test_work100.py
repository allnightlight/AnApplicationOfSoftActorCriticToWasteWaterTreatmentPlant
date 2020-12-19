'''
Created on 2020/12/16

@author: ukai
'''
import unittest

from casestudies.work100 import Work100
from concrete.concrete_build_parameter import ConcreteBuildParameter
import matplotlib.pylab as plt
import numpy as np
import os


class Test(unittest.TestCase):
    
    
    def setUp(self):
        unittest.TestCase.setUp(self)

        self.work = Work100.create()
        
        self.buildParameter = ConcreteBuildParameter(nIterationPerEpoch=1)
        self.nEpoch = 2**2
        self.nMesh = 2**3
        self.nInterval = 2**1
    
    def test001(self):
        
        work = self.work        
        
        agent, environment, trainer = work.createAgentEnvironmentAndTrainer(self.buildParameter)

        for _ in work.trainIterator(trainer, self.nEpoch):
            pass
        
        Pv, Mv, Adv = work.getAdvantageOnMesh(agent, nMesh = self.nMesh)
        
        for x in (Pv, Mv, Adv):
            assert x.shape == (self.nMesh, self.nMesh)
            
        fig = plt.figure()
        ax = fig.add_subplot(2,2,(1,3))
        work.showAdvantageOnMesh(Pv, Mv, Adv, ax, fig)
#         plt.show()
        plt.close(fig)
        
        Pv, Mv = work.getTrainingData(environment, nLast = None)
        
        fig = plt.figure()
        ax1 = fig.add_subplot(2,2,2)
        ax2 = fig.add_subplot(2,2,4)
        work.showTrainingData(Pv, Mv, ax1, ax2, fig)
#         plt.show()
        plt.close(fig)        
        
    
    def test002(self):
        
        for figPath in self.work.work(self.buildParameter, nEpoch = self.nEpoch, nInterval=self.nInterval, nMesh=self.nMesh, prefix="test", figSize = [20, 8]):
            #os.remove(figPath)
            pass
            
            
    def test003(self):
        
        Mv = np.random.randn(2**10, 3) * 100        
        Do = self.work.convertMv2Do(Mv)
        
        assert np.all(Do <= self.work.maxDo)
        assert np.all(Do >= self.work.minDo)
        
    def test004(self):
        
        work = self.work
        
        agent, environment, trainer = work.createAgentEnvironmentAndTrainer(self.buildParameter)

        for _ in work.trainIterator(trainer, self.nEpoch):
            pass
        
        Pv, Mv = work.getAgentResponse(agent, nMesh=2**7)
        
        fig = plt.figure()
        ax = fig.add_subplot()
        work.showResponseOnMesh(Pv, Mv, ax, fig)
#         plt.show()
        plt.close(fig)
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()