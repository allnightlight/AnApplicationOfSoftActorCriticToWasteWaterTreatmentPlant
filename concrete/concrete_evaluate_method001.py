'''
Created on 2020/12/05

@author: ukai
'''
import os
import numpy as np
import matplotlib.pylab as plt

from framework.util import Utils
from sac.sac_batch_data_agent import SacBatchDataAgent
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from sac.sac_batch_data_reward import SacBatchDataReward
from sac.sac_evaluate_method import SacEvaluateMethod


class ConcreteEvaluateMethod001(SacEvaluateMethod):
    '''
    classdocs
    '''


    def __init__(self, figSize, figFolderPath, useDeterministicAction = True):
        SacEvaluateMethod.__init__(self)
        
        self.figSize = figSize
        self.figFolderPath = figFolderPath
        self.useDeterministicAction = useDeterministicAction
        
    def evaluate(self, simulationResultGenerator):
        
        seriesPv, seriesDeterministicMv, seriesStochasticMv, _ = ConcreteEvaluateMethod001.getPVMvRewardSeries(simulationResultGenerator)
        
        if self.useDeterministicAction:
            seriesMv = seriesDeterministicMv
        else:
            seriesMv = seriesStochasticMv
        
        nSimulationStep = seriesMv.shape[0]
        
        t1 = np.linspace(0, nSimulationStep, nSimulationStep+1)
        t2 = np.linspace(0.5, nSimulationStep-0.5, nSimulationStep)
        
        figFilePath = os.path.join(self.figFolderPath, Utils.generateRandomString(16) + ".png")
        if not os.path.exists(self.figFolderPath):
            os.mkdir(self.figFolderPath)
        
        fig = plt.figure(figsize=self.figSize)
        assert isinstance(fig, plt.Figure)
        fig.clf()
        
        ax1 = fig.add_subplot(2, 1, 1)
        assert isinstance(ax1, plt.Axes)
        for k1 in range(seriesPv.shape[1]):
            ax1.plot(t1, seriesPv[:,k1], '-', label = "PV %d" % k1)
        ax1.legend()

        ax2 = fig.add_subplot(2, 1, 2)
        assert isinstance(ax2, plt.Axes)
        for k1 in range(seriesMv.shape[1]):
            ax2.plot(t2, seriesMv[:,k1], '-', label = "MV %d" % k1)
        ax2.legend()
        
        fig.tight_layout()
        fig.savefig(figFilePath)
        plt.close(fig)
        
        return dict(figFilePath = figFilePath)
    
    @classmethod
    def getPVMvRewardSeries(cls, simulationResultGenerator):
        
        seriesPv = []
        seriesDeterministicMv = []
        seriesStochasticMv = []
        seriesReward = []
        
        for batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep in simulationResultGenerator:
            
            assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
            assert isinstance(batchDataAgent, SacBatchDataAgent)
            assert isinstance(batchDataReward, SacBatchDataReward)
            assert isinstance(batchDataEnvironmentNextStep, SacBatchDataEnvironment)
            
            seriesPv.append(batchDataEnvironment.bufferPv[-1]) # (1, nPv)
            seriesDeterministicMv.append(batchDataAgent.getDeterministicAction()) # (1, nMv)
            seriesStochasticMv.append(batchDataAgent.getSampledActionOnEnvironment()) # (1, nMv)
            seriesReward.append(batchDataReward.getValue()) # (,)
        
        seriesPv.append(batchDataEnvironmentNextStep.bufferPv[-1])
        
        seriesPv = np.concatenate(seriesPv, axis=0) # (nSimulationStep+1, nPv)
        seriesDeterministicMv = np.concatenate(seriesDeterministicMv, axis=0) # (nSimulationStep, nMv)
        seriesStochasticMv = np.concatenate(seriesStochasticMv, axis=0) # (nSimulationStep, nMv)
        seriesReward = np.array(seriesReward).reshape(-1,1) # (nSimulationStep, 1)

        return seriesPv, seriesDeterministicMv, seriesStochasticMv, seriesReward        