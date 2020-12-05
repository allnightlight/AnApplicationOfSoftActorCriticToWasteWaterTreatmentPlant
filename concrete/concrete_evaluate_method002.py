'''
Created on 2020/12/05

@author: ukai
'''
import os
import numpy as np

from concrete.concrete_evaluate_method001 import ConcreteEvaluateMethod001
from framework.util import Utils
from sac.sac_evaluate_method import SacEvaluateMethod


class ConcreteEvaluateMethod002(SacEvaluateMethod):
    '''
    classdocs
    '''


    def __init__(self, dataFolderPath):
        SacEvaluateMethod.__init__(self)
        
        self.dataFolderPath = dataFolderPath
        
    def evaluate(self, simulationResultGenerator):
        
        dataFilePath = os.path.join(self.dataFolderPath, Utils.generateRandomString(16) + ".csv")
        if not os.path.exists(self.dataFolderPath):
            os.mkdir(self.dataFolderPath)

        seriesPv, seriesDeterministicMv, seriesStochasticMv, seriesReward = ConcreteEvaluateMethod001.getPVMvRewardSeries(simulationResultGenerator)
        
        nSimulationStep = seriesDeterministicMv.shape[0]

        t1 = np.linspace(0, nSimulationStep, nSimulationStep+1)
        t2 = np.linspace(0.5, nSimulationStep-0.5, nSimulationStep)
        
        tbl = ["variable,time,value"]
        for t_arr,arr,label in [(t1, seriesPv, 'Pv'), (t2, seriesDeterministicMv, 'DtmMv'), (t2, seriesStochasticMv, 'StcMv'), (t2, seriesReward, 'Reward')]:
            for k1 in range(arr.shape[1]):
                for (t, val) in zip(t_arr, arr[:,k1]):
                    tbl.append("%s,%f,%f" % (label + str(k1), t, val))
        
        with open(dataFilePath, "w") as fp:
            fp.write("\n".join(tbl))
                
        return dict(dataFilePath = dataFilePath)
        