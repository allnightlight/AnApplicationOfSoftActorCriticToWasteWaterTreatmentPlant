'''
Created on 2020/11/21

@author: ukai
'''
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_batch_data_environment import ConcreteBatchDataEnvironment
from concrete.concrete_batch_data_reward import ConcreteBatchDataReward
import tensorflow
from concrete.concrete_agent import ConcreteAgent
from concrete.concrete_policy import ConcretePolicy
from concrete.concrete_value_function_approximator import ConcreteValueFunctionApproximator
from concrete.concrete_feature_extractor import ConcreteFeatureExtractor

import numpy as np
import matplotlib.pylab as plt
import sys

class Work001Utility(object):
    '''
    classdocs
    '''
    
    @classmethod
    def create(cls, nIter = 1):
        
        nMv = 1
        nPv = 1
        nFeature = 1
        nSampleOfActionsInValueFunctionApproximator = 2**3
        discountFactor = 0.5
        
        agent = ConcreteAgent(policy = ConcretePolicy(nMv)
                              , valueFunctionApproximator = ConcreteValueFunctionApproximator(nMv, nSampleOfActionsInValueFunctionApproximator)
                              , featureExtractor = ConcreteFeatureExtractor(nFeature)
                              , discountFactor = discountFactor)
        
        agent.reset()
                
        return Work001Utility(nMv, nPv, nFeature, agent, nIter)

    def __init__(self, nMv, nPv, nFeature, agent, nIter):
        
        assert isinstance(agent, ConcreteAgent)
        
        self.nMv = nMv
        self.nPv = nPv
        self.nFeature = nFeature
        self.agent = agent        
        self.nIter = nIter
        self.nBatch = 1
        self.nPlottingSamples = 2**7


    def getRandomBatchDataAgent(self):
        
        return ConcreteBatchDataAgent(_Mean = tensorflow.random.normal(shape = (self.nBatch, self.nMv))
                                        , _LogSd = tensorflow.zeros(shape = (self.nBatch, self.nMv)))

    def getRandomBatchDataEnvironment(self):

        return ConcreteBatchDataEnvironment(
                bufferPv = [tensorflow.random.normal(shape = (self.nBatch, self.nPv)),]
                , bufferMv = [])

    def getFixedBatchDataEnvironment(self):

        return ConcreteBatchDataEnvironment(
                bufferPv = [tensorflow.zeros(shape = (self.nBatch, self.nPv)),]
                , bufferMv = [])

    def generateData(self):
        
        for _ in range(self.nIter):
        
            batchDataAgent = self.getRandomBatchDataAgent()
            
            u = batchDataAgent.getSampledAction() # (1, nMv)
            reward = -tensorflow.reduce_sum(tensorflow.abs(1.-u), axis=-1, keepdims = True) # (1,1)        
            
            assert isinstance(batchDataAgent, ConcreteBatchDataAgent)
            
            batchDataEnvironment = self.getRandomBatchDataEnvironment()
            batchDataReward = ConcreteBatchDataReward(reward = reward)
            batchDataEnvironmentNextStep =ConcreteBatchDataEnvironment(bufferPv = [u,], bufferMv = []) 
            
            yield batchDataAgent, batchDataEnvironment, batchDataReward, batchDataEnvironmentNextStep
        
    def trainQ(self):
        """
        train action value function
        """
        
        print(">> Start train action value function")
        
        cnt = 0
        for batchDataAgent, batchDataEnvironment, batchDataReward, batchDataEnvironmentNextStep in self.generateData():
            
            sys.stdout.write("\r%04d/%04d" % (cnt, self.nIter))
        
            self.agent.updateActionValueFunction(batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep)
            
            cnt += 1
            
        print("\n>> Done")
        
    def trainV(self):
        
        print(">> Start train state value function")

        cnt = 0
        for _, batchDataEnvironment, _, _ in self.generateData():
            
            sys.stdout.write("\r%04d/%04d" % (cnt, self.nIter))
        
            self.agent.updateStateValueFunction(batchDataEnvironment)
            
            cnt += 1
        
        print("\n>> Done")

    def trainPi(self):
        
        print(">> Start training policy")

        cnt = 0
        for _, batchDataEnvironment, _, _ in self.generateData():
            
            sys.stdout.write("\r%04d/%04d" % (cnt, self.nIter))
        
            self.agent.updatePolicy(batchDataEnvironment)
            
            cnt += 1
        
        print("\n>> Done")
        
    def plotTrainedQ(self):
        """
        validate a trained action value function
        """
        
        values = []
        for _ in range(self.nPlottingSamples):
            value = self.agent.valueFunctionApproximator.getActionValue(
                batchDataFeature = self.agent.featureExtractor.call(self.getFixedBatchDataEnvironment())
                , batchDataAgent = self.getRandomBatchDataAgent()).getValue().numpy() # (1,1)
            assert value.shape == (1,1)
            
            values.append(value)
        values = np.concatenate(values, axis=-1).squeeze()        
        
        plt.plot(values, 'o')
        plt.show()                                    
                    
    def plotTrainedPi(self):
        """
        validate a trained action value function
        """
        
        mvs = []
        for _ in range(self.nPlottingSamples):
            
            mv = self.agent.getAction(batchDataEnvironment = self.getRandomBatchDataEnvironment())._Mean.numpy() # (1,1)
            
            mvs.append(mv)
        mvs = np.concatenate(mvs, axis=-1).squeeze()        
        
        plt.plot(mvs, 'o')
        plt.show()                                    
                    
        
    def checkUpdateQ(self):        
        """
        
        Figure of plotted value should look like convex with the peak at mv = 1
        
        """
        
        self.trainQ()
        self.plotTrainedQ()
        
    def checkUpdateV(self):
        """
        
        Figure of plotted value should look like the reward function = -|mv-1|
        
        """
        
        self.trainQ()
        self.trainV()
        self.plotTrainedQ()
        
    def checkUpdatePi(self):
        
        """
        
        Figure of plotted mv should have constant value, 1 at any pv.
        
        """

        
        self.trainQ()
        self.trainV()
        self.trainPi()
        self.plotTrainedPi()
