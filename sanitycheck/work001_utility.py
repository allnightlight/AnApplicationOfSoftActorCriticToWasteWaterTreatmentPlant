'''
Created on 2020/11/21

@author: ukai
'''
import sys

import tensorflow

from concrete.concrete_agent import ConcreteAgent
from concrete.concrete_batch_data_agent import ConcreteBatchDataAgent
from concrete.concrete_batch_data_environment import ConcreteBatchDataEnvironment
from concrete.concrete_batch_data_reward import ConcreteBatchDataReward
from concrete.concrete_feature_extractor001 import ConcreteFeatureExtractor001
from concrete.concrete_feature_extractor002 import ConcreteFeatureExtractor002
from concrete.concrete_policy import ConcretePolicy
from concrete.concrete_value_function_approximator import ConcreteValueFunctionApproximator
import matplotlib.pylab as plt
import numpy as np


class Work001Utility(object):
    '''
    classdocs
    '''
    
    @classmethod
    def create(cls, nIter = 1, alphaTemp = 0.0, updatePolicyByAdvantage = False, showLog = False, featureExtractorType = "ConcreteFeatureExtractor001"):
        
        nMv = 1
        nPv = 1
        nFeature = 1
        nSampleOfActionsInValueFunctionApproximator = 2**3
        discountFactor = 0.5
        nHidden = 2**2
        
        if featureExtractorType == "ConcreteFeatureExtractor001":
            featureExtractor = ConcreteFeatureExtractor001(nFeature=nFeature)
        if featureExtractorType == "ConcreteFeatureExtractor002":
            featureExtractor = ConcreteFeatureExtractor002(nFeature=nPv)        
        
        agent = ConcreteAgent(policy = ConcretePolicy(nMv)
                              , valueFunctionApproximator = ConcreteValueFunctionApproximator(nFeature, nMv, nSampleOfActionsInValueFunctionApproximator, nHidden)
                              , featureExtractor = featureExtractor
                              , discountFactor = discountFactor
                              , alphaTemp = alphaTemp
                              , updatePolicyByAdvantage = updatePolicyByAdvantage
                              , saveFolderPath = "checkpoint")
        
        return Work001Utility(nMv, nPv, nFeature, agent, nIter, showLog)

    def __init__(self, nMv, nPv, nFeature, agent, nIter, showLog):
        
        assert isinstance(agent, ConcreteAgent)
        
        self.nMv = nMv
        self.nPv = nPv
        self.nFeature = nFeature
        self.agent = agent        
        self.nIter = nIter
        self.nBatch = 1
        self.nPlottingSamples = 2**7
        self.showLog = showLog


    def reset(self):
        
        self.agent.reset()

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
        
        self.reset()
        
        print(">> Start train action value function")
        
        cnt = 0
        for batchDataAgent, batchDataEnvironment, batchDataReward, batchDataEnvironmentNextStep in self.generateData():
            
            sys.stdout.write("\r%04d/%04d" % (cnt, self.nIter))
        
            self.agent.updateActionValueFunction(batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep)
            
            cnt += 1
            
        print("\n>> Done")
        
    def trainQandV(self):
        
        self.reset()
        
        print(">> Start train state value function")

        cnt = 0
        for batchDataAgent, batchDataEnvironment, batchDataReward, batchDataEnvironmentNextStep in self.generateData():
            
            sys.stdout.write("\r%04d/%04d" % (cnt, self.nIter))

            self.agent.updateActionValueFunction(batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep)        
            self.agent.updateStateValueFunction(batchDataEnvironment)
            
            cnt += 1
        
        print("\n>> Done")

    def trainQandVandPi(self):

        self.reset()
        
        if self.showLog:
            print(">> Start training policy")

        cnt = 0
        for batchDataAgent, batchDataEnvironment, batchDataReward, batchDataEnvironmentNextStep in self.generateData():
            
            if self.showLog:
                sys.stdout.write("\r%04d/%04d" % (cnt, self.nIter))

            self.agent.updateActionValueFunction(batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep)        
            self.agent.updateStateValueFunction(batchDataEnvironment)        
            self.agent.updatePolicy(batchDataEnvironment)
            
            cnt += 1
        
        if self.showLog:
            print("\n>> Done")

    def trainOnlyPi(self):

        self.reset()
        
        if self.showLog:
            print(">> Start training policy")

        cnt = 0
        for _ in range(self.nIter):
            
            if self.showLog:
                sys.stdout.write("\r%04d/%04d" % (cnt, self.nIter))

            self.agent.updatePolicy(batchDataEnvironment = self.getFixedBatchDataEnvironment())
            
            cnt += 1
        if self.showLog:
            print("\n>> Done")
        
    def plotTrainedQ(self):
        """
        validate a trained action value function
        """
        
        mvs = []
        values = []
        for _ in range(self.nPlottingSamples):
            batchDataAgent = self.getRandomBatchDataAgent()
            value = self.agent.valueFunctionApproximator.getActionValue(
                batchDataFeature = self.agent.featureExtractor.call(self.getFixedBatchDataEnvironment())
                , batchDataAgent = batchDataAgent).getValue().numpy() # (1,1)
            assert value.shape == (1,1)
            
            mvs.append(batchDataAgent.getSampledAction())
            values.append(value)
        mvs = np.concatenate(mvs, axis=-1).squeeze()
        values = np.concatenate(values, axis=-1).squeeze()        
        
        plt.plot(mvs, values, 'o')
        plt.grid()
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
        plt.grid()
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
        
        self.trainQandV()
        self.plotTrainedQ()
        
    def checkUpdatePi(self):
        
        """
        
        Figure of plotted mv should have constant value, 1 at any pv.
        
        """

        
        self.trainQandVandPi()
        self.plotTrainedPi()
