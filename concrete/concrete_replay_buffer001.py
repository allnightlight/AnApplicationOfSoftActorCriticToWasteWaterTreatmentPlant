'''
Created on 2020/12/13

@author: ukai
'''

from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_batch_data_environment import ConcreteBatchDataEnvironment
from concrete.concrete_batch_data_reward import ConcreteBatchDataReward
import numpy as np
from sac.sac_replay_buffer import SacReplayBuffer
from sac.sac_batch_data_environment import SacBatchDataEnvironment


class ConcreteReplayBuffer001(SacReplayBuffer):
    '''
    classdocs
    '''


    def __init__(self, bufferSize, nBatch):
        SacReplayBuffer.__init__(self, bufferSize)
        
        self.nBatch = nBatch
        self.S0 = None
        self.U0 = None
        self.R0 = None
        self.S1 = None
        
    def append(self, batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep):
        SacReplayBuffer.append(self, batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep)
        
        assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
        assert isinstance(batchDataEnvironmentNextStep, SacBatchDataEnvironment)
        assert isinstance(batchDataAgent, ConcreteBatchDataAgent)
        assert isinstance(batchDataReward, ConcreteBatchDataReward)
        
        if self.S0 is None:
            self.S0 = batchDataEnvironment.bufferPv[-1] # (..., nPv)
        else:
            self.S0 = np.concatenate((self.S0, batchDataEnvironment.bufferPv[-1]), axis=0) # (..., nPv)

        if self.U0 is None:
            self.U0 = batchDataAgent.getSampledActionOnEnvironment() # (..., nMv)
        else:
            self.U0 = np.concatenate((self.U0, batchDataAgent.getSampledActionOnEnvironment()), axis=0) # (..., nMv)

        if self.R0 is None:
            self.R0 = batchDataReward.getValue() # (..., 1)
        else:
            self.R0 = np.concatenate((self.R0, batchDataReward.getValue()), axis=0) # (..., 1)

        if self.S1 is None:
            self.S1 = batchDataEnvironmentNextStep.bufferPv[-1] # (..., nPv)
        else:
            self.S1 = np.concatenate((self.S1, batchDataEnvironmentNextStep.bufferPv[-1]), axis=0) # (..., nPv)
        
        
    def generateStateActionRewardAndNextState(self, nStepGradient):
        
        currentBufferSize = self.S0.shape[0]

        if currentBufferSize >= self.nBatch:
    
            for _ in range(nStepGradient):
                idx = np.random.permutation(currentBufferSize)[:self.nBatch]
                
                yield ConcreteBatchDataEnvironment(bufferPv = [self.S0[idx,:],], bufferMv = [])\
                    , ConcreteBatchDataAgent(None, None, self.U0[idx,:])\
                    , ConcreteBatchDataReward(reward = self.R0[idx,:])\
                    , ConcreteBatchDataEnvironment(bufferPv = [self.S1[idx,:],], bufferMv = [])                    
        
    def reset(self):
        SacReplayBuffer.reset(self)
        
        self.S0 = None
        self.U0 = None
        self.R0 = None
        self.S1 = None
        