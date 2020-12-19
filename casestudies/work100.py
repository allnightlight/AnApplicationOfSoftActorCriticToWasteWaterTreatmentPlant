'''
Created on 2020/12/16

@author: ukai
'''

import itertools
import os
import sys

from concrete.concrete_agent import ConcreteAgent
from concrete.concrete_agent_factory import ConcreteAgentFactory
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_batch_data_environment import ConcreteBatchDataEnvironment
from concrete.concrete_batch_data_value import ConcreteBatchDataValue
from concrete.concrete_environment import ConcreteEnvironment
from concrete.concrete_environment_factory import ConcreteEnvironmentFactory
from concrete.concrete_trainer import ConcreteTrainer
from concrete.concrete_trainer_factory import ConcreteTrainerFactory
from framework.util import Utils
import matplotlib.pylab as plt
import numpy as np


class Work100(object):
    '''
    classdocs
    '''

    @classmethod
    def create(cls, showLog = False):
        return Work100(agentFactory = ConcreteAgentFactory()
            , environmentFactory = ConcreteEnvironmentFactory()
            , trainerFactory = ConcreteTrainerFactory()
            , showLog = showLog)

    def __init__(self, agentFactory, environmentFactory, trainerFactory, thresholdDo = 1.5, Sv_Nh4 = 3.0, minDo = 0.0, maxDo = 3.0, figFolder = "./fig", showLog = False, limDo = [0,3], limNh4 = [0, 6]):
        '''
        Constructor
        '''
        
        assert isinstance(agentFactory, ConcreteAgentFactory)
        assert isinstance(environmentFactory, ConcreteEnvironmentFactory)
        assert isinstance(trainerFactory, ConcreteTrainerFactory)
        
        self.agentFactory = agentFactory
        self.environmentFactory = environmentFactory
        self.trainerFactory = trainerFactory        
        self.thresholdDo = thresholdDo
        self.Sv_Nh4 = Sv_Nh4
        self.minDo = minDo
        self.maxDo = maxDo
        self.figFolder = figFolder
        self.showLog = showLog
        self.limDo = limDo
        self.limNh4 = limNh4
        
    def createAgentEnvironmentAndTrainer(self, buildParameter):
        
        environment = self.environmentFactory.create(buildParameter)
        agent = self.agentFactory.create(buildParameter, environment)
        trainer = self.trainerFactory.create(buildParameter, agent, environment)

        return agent, environment, trainer
    
    def trainIterator(self, trainer, nEpoch):

        assert isinstance(trainer, ConcreteTrainer)
        
        trainer.reset()
        trainer.trainPreprocess()
        for k1 in range(nEpoch):
            trainer.train()
            yield k1

    def convertPv2Nh4(self, Pv):
        return Pv + self.Sv_Nh4
    
    def convertMv2Do(self, Mv):
        MvChopped = Mv.copy()
        MvChopped[Mv > self.thresholdDo] = self.thresholdDo
        MvChopped[Mv < -self.thresholdDo] = -self.thresholdDo
        return (MvChopped + self.thresholdDo)/(2*self.thresholdDo) * (self.maxDo-self.minDo) + self.minDo
                                                
    def getAdvantageOnMesh(self, agent, nMesh):
        '''
        Pv: Pv
        Mv: Mv
        Adv: Advantage        
        '''
        
        assert isinstance(agent, ConcreteAgent)
        
        Pv, Mv = np.meshgrid(np.linspace(self.limNh4[0]-self.Sv_Nh4, self.limNh4[1]-self.Sv_Nh4,nMesh), np.linspace(-self.thresholdDo, self.thresholdDo,nMesh))
        Pv = Pv.astype(np.float32)
        Mv = Mv.astype(np.float32)
        Adv = np.zeros((nMesh, nMesh))
        
        for k1, k2 in itertools.product(range(nMesh), range(nMesh)):
        
            e = Pv[k1,k2].reshape(1,1) # (1,1)
            u = Mv[k1,k2].reshape(1,1) # (1,1)
            batchDataEnvironment = ConcreteBatchDataEnvironment(bufferPv = [e,], bufferMv = [])        
            batchDataAgent = ConcreteBatchDataAgent(_Mean = None, _LogSd = None, sampledAction = u)
            
            batchDataValue = agent.valueFunctionApproximator.getActionValue(batchDataFeature = agent.featureExtractor.call(batchDataEnvironment)
                                                           , batchDataAgent = batchDataAgent)
            
            batchDataValue2 = agent.valueFunctionApproximator.getStateValue(batchDataFeature = agent.featureExtractor.call(batchDataEnvironment))
            
            assert isinstance(batchDataValue, ConcreteBatchDataValue)
            
            v = batchDataValue.getValue() - batchDataValue2.getValue() # (1,1)
        
            Adv[k1,k2] = v
            
        return Pv, Mv, Adv
    
    def showAdvantageOnMesh(self, Pv, Mv, Adv, ax, fig):
                
        assert isinstance(fig, plt.Figure)
        assert isinstance(ax, plt.Axes)
        
        c = ax.pcolor(self.convertPv2Nh4(Pv), self.convertMv2Do(Mv), Adv, cmap="gray")
        ax.set_xlabel("NH4")
        ax.set_ylabel("DO")    
        fig.colorbar(c, ax=ax)
                
    def getTrainingData(self, environment, nLast = None):
        
        assert isinstance(environment, ConcreteEnvironment)
        
        Pv = []
        Mv = []
        for e, u in zip(environment.bufferPv, environment.bufferMv):
            
            Pv.append(e)
            Mv.append(u)
            
        Pv = np.concatenate(Pv, axis=0) # (..., nPv)
        Mv = np.concatenate(Mv, axis=0) # (..., nMv)
        
        if nLast is not None:
            Pv = Pv[-nLast:]
            Mv = Mv[-nLast:]
                    
        return Pv, Mv
        
    def showTrainingData(self, Pv, Mv, ax1, ax2, fig):
        
        assert isinstance(fig, plt.Figure)
        assert isinstance(ax1, plt.Axes)
        assert isinstance(ax2, plt.Axes)
        
        t = np.arange(Pv.shape[0])
        
        ax1.axhline(self.Sv_Nh4, linestyle="--", color="k")
        ax1.plot(t, self.convertPv2Nh4(Pv))
        ax1.set_ylabel("NH4")
        ax1.set_xlim(t[0], t[-1])
        ax1.set_ylim(self.limNh4)
        
        
        ax2.plot(t, self.convertMv2Do(Mv))
        ax2.set_ylabel("DO")
        ax2.set_xlim(t[0], t[-1])
        ax2.set_ylim(self.limDo)
        
    def getAgentResponse(self, agent, nMesh):
        
        Pv = np.linspace(self.limNh4[0]-self.Sv_Nh4, self.limNh4[1]-self.Sv_Nh4, nMesh)
        Pv = Pv.astype(np.float32)
        Mv = np.zeros((nMesh,)).astype(np.float32)
        
        for k1 in range(nMesh):
        
            e = Pv[k1].reshape(1,1) # (1,1)
            batchDataEnvironment = ConcreteBatchDataEnvironment(bufferPv = [e,], bufferMv = [])        
            batchDataAgent = agent.getAction(batchDataEnvironment)
            
            assert isinstance(batchDataAgent, ConcreteBatchDataAgent)
            
            Mv[k1] = batchDataAgent.getDeterministicAction()[0,0]
        
        return Pv, Mv

    def showResponseOnMesh(self, Pv, Mv, ax, fig):
                
        assert isinstance(fig, plt.Figure)
        assert isinstance(ax, plt.Axes)
        
        ax.plot(self.convertPv2Nh4(Pv), self.convertMv2Do(Mv), color="red", linestyle="-", linewidth=2)
        ax.set_xlabel("NH4")
        ax.set_ylabel("DO")
        
    def watchLearningProcess(self, buildParameter, nEpoch, nInterval, fig, nMesh):
        
        assert isinstance(fig, plt.Figure)
                
        agent, environment, trainer = self.createAgentEnvironmentAndTrainer(buildParameter)
        
        for k1 in self.trainIterator(trainer, nEpoch):
            
            if self.showLog:
                sys.stdout.write("\r>> %4d/%4d" % (k1+1, nEpoch))            
            
            if (k1 + 1) % nInterval == 0:
                
                fig.clf()                
                ax0 = fig.add_subplot(2,2,(1,3))                
                self.showAdvantageOnMesh(*self.getAdvantageOnMesh(agent, nMesh), ax0, fig)
                self.showResponseOnMesh(*self.getAgentResponse(agent, nMesh), ax0, fig) 
                ax1 = fig.add_subplot(2,2,2)
                ax2 = fig.add_subplot(2,2,4)
                self.showTrainingData(*self.getTrainingData(environment, nLast = nInterval), ax1, ax2, fig) 
                fig.tight_layout()
                
                yield
                
    def work(self, buildParameter
            , nEpoch = 96 * 28
            , nInterval = 96
            , nMesh = 2**4
            , prefix = Utils.generateRandomString(16)
            , figSize = [20, 8]):
        
        if not os.path.exists(self.figFolder):
            os.mkdir(self.figFolder)
        
        fig = plt.figure(figsize=figSize)
        
        for k1, _ in enumerate(self.watchLearningProcess(buildParameter, nEpoch, nInterval, fig, nMesh)):
            day = k1 + 1
            
            fname = "%s_day=%2d.png" % (prefix, day)
            figPath = os.path.join(self.figFolder, fname)        
            fig.savefig(figPath)
            
            yield figPath