'''
Created on 2020/11/29

@author: ukai
'''

import numpy as np
from sac.sac_batch_data_agent import SacBatchDataAgent
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from sac.sac_batch_data_reward import SacBatchDataReward
from sac.sac_evaluator import SacEvaluator


class Work004Evaluator(SacEvaluator):
    '''
    classdocs
    '''


    def evaluate(self, simulationResultGenerator):
                    
        rewards = []
        mvs = []
        for batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep in simulationResultGenerator:
            
            assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
            assert isinstance(batchDataAgent, SacBatchDataAgent)
            assert isinstance(batchDataReward, SacBatchDataReward)
            assert isinstance(batchDataEnvironmentNextStep, SacBatchDataEnvironment)

            rewards.append(batchDataReward.getValue())
            mvs.append(batchDataAgent._Mean.numpy())
            
        return {"mvAverage": float(np.mean(mvs))
            , "rewardAverage": float(np.mean(rewards))}
        