'''
Created on 2020/11/29

@author: ukai
'''

import numpy as np
from sac.sac_batch_data_agent import SacBatchDataAgent
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from sac.sac_batch_data_reward import SacBatchDataReward
from sac.sac_evaluate_method import SacEvaluateMethod


class MyEvaluateMethod001(SacEvaluateMethod):
    '''
    classdocs
    '''


    def evaluate(self, simulationResultGenerator):
              
        pvs = []    
        rewards = []
        mvs = []
        sds = []
        for batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep in simulationResultGenerator:
            
            assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
            assert isinstance(batchDataAgent, SacBatchDataAgent)
            assert isinstance(batchDataReward, SacBatchDataReward)
            assert isinstance(batchDataEnvironmentNextStep, SacBatchDataEnvironment)

            pvs.append(batchDataEnvironment.bufferPv[-1])
            rewards.append(batchDataReward.getValue())
            mvs.append(batchDataAgent._Mean.numpy())
            sds.append(np.exp(batchDataAgent._LogSd.numpy()))
            
        return {"mvAverage": float(np.mean(mvs))
            , "rewardAverage": float(np.mean(rewards))
            , "mvSdAverage": float(np.mean(sds))
            , "pvAverage": float(np.mean(pvs))}
        