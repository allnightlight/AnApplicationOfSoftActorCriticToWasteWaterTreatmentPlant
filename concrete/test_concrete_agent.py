'''
Created on 2020/11/17

@author: ukai
'''
import unittest
from concrete.concrete_factory_for_test import ConcreteFactoryForTest
from concrete.concrete_agent import ConcreteAgent
import tensorflow
import numpy as np 
import shutil


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = ConcreteFactoryForTest()


    def test001(self):
        
        agent = self.factory.createAgent()
        
        assert isinstance(agent, ConcreteAgent)
        
        agent.getErrForUpdateStateValueFunction(batchDataEnvironment = self.factory.createBatchDataEnvironment())
        
    def test002(self):

        agent = self.factory.createAgent()
        
        assert isinstance(agent, ConcreteAgent)
        
        dense = tensorflow.keras.layers.Dense(self.factory.nPv)
        fh = lambda : dense(tensorflow.random.normal(shape = (self.factory.nBatch, self.factory.nFeature)))
        trainableVariables = dense.trainable_variables
        optimizer = tensorflow.keras.optimizers.Adam()

        agent.applyGradientSomeoneToReduce(fh, trainableVariables, optimizer)
        
    def test003(self):
        
        agent = self.factory.createAgent()
        
        assert isinstance(agent, ConcreteAgent)

        agent.reset()
        for optimizer in [
            agent.getOptimizerForUpdateActionValueFunction()
            , agent.getOptimizerForUpdatePolicy()
            , agent.getOptimizerForUpdateStateValueFunction()
            ]:
            assert isinstance(optimizer, tensorflow.keras.optimizers.Optimizer)
            
    def test004(self):
    
        agent = self.factory.createAgent()
        
        assert isinstance(agent, ConcreteAgent)

        for trainableVariables in [
            agent.getTrainableVariablesForUpdateActionValueFunction()
            , agent.getTrainableVariablesForUpdatePolicy()
            , agent.getTrainableVariablesForUpdateStateValueFunction()]:
        
            assert trainableVariables is not None

    def test005(self):
        
        agent = self.factory.createAgent()
        
        assert isinstance(agent, ConcreteAgent)
        
        agent.reset()

        agent.updateStateValueFunction(batchDataEnvironment = self.factory.createBatchDataEnvironment())
        agent.updatePolicy(batchDataEnvironment = self.factory.createBatchDataEnvironment())
        agent.updateActionValueFunction(batchDataEnvironment = self.factory.createBatchDataEnvironment()
                                        , batchDataAgent = self.factory.createBatchDataAgent()
                                        , batchDataReward = self.factory.createBatchDataReward()
                                        , batchDataEnvironmentNextStep = self.factory.createBatchDataEnvironment())

    def test006(self):
        
        agent = self.factory.createAgent()
        
        assert isinstance(agent, ConcreteAgent)
        
        agent.reset()
        
        def isEqual(p, q):
            flag = True
            for a, b in zip(p, q):
                flag &= np.all(a == b)
            return flag

        agent.updateStateValueFunction(batchDataEnvironment = self.factory.createBatchDataEnvironment())

        p0 = [v.numpy() for v in agent.policy.trainable_variables]
        p1 = [v.numpy() for v in agent.valueFunctionApproximator.trainable_variables]
        p2 = [v.numpy() for v in agent.featureExtractor.trainable_variables]
        
        agent.updateStateValueFunction(batchDataEnvironment = self.factory.createBatchDataEnvironment())
        
        q0 = [v.numpy() for v in agent.policy.trainable_variables]
        q1 = [v.numpy() for v in agent.valueFunctionApproximator.trainable_variables]
        q2 = [v.numpy() for v in agent.featureExtractor.trainable_variables]
        
        assert len(p0) == len(q0)
        assert len(p1) == len(q1)
        assert len(p2) == len(q2)
        
        assert isEqual(p0, q0) == True        
        assert isEqual(p1, q1) == False
#         assert isEqual(p2, q2) == False
        
    def test007(self):
        
        agent = self.factory.createAgent()
        
        assert isinstance(agent, ConcreteAgent)
        
        agent.reset()
        
        def isEqual(p, q):
            flag = True
            for a, b in zip(p, q):
                flag &= np.all(a == b)
            return flag

        agent.updatePolicy(batchDataEnvironment = self.factory.createBatchDataEnvironment())

        p0 = [v.numpy() for v in agent.policy.trainable_variables]
        p1 = [v.numpy() for v in agent.valueFunctionApproximator.trainable_variables]
        p2 = [v.numpy() for v in agent.featureExtractor.trainable_variables]
        
        agent.updatePolicy(batchDataEnvironment = self.factory.createBatchDataEnvironment())        
        
        q0 = [v.numpy() for v in agent.policy.trainable_variables]
        q1 = [v.numpy() for v in agent.valueFunctionApproximator.trainable_variables]
        q2 = [v.numpy() for v in agent.featureExtractor.trainable_variables]
        
        assert len(p0) == len(q0)
        assert len(p1) == len(q1)
        assert len(p2) == len(q2)
        
        assert isEqual(p0, q0) == False
        assert isEqual(p1, q1) == True
#         assert isEqual(p2, q2) == False

    def test008(self):
        
        agent = self.factory.createAgent()
        
        assert isinstance(agent, ConcreteAgent)
        
        agent.reset()
        
        def isEqual(p, q):
            flag = True
            for a, b in zip(p, q):
                flag &= np.all(a == b)
            return flag

        agent.updateActionValueFunction(batchDataEnvironment = self.factory.createBatchDataEnvironment()
                                        , batchDataAgent = self.factory.createBatchDataAgent()
                                        , batchDataReward = self.factory.createBatchDataReward()
                                        , batchDataEnvironmentNextStep = self.factory.createBatchDataEnvironment())

        p0 = [v.numpy() for v in agent.policy.trainable_variables]
        p1 = [v.numpy() for v in agent.valueFunctionApproximator.trainable_variables]
        p2 = [v.numpy() for v in agent.featureExtractor.trainable_variables]
        
        agent.updateActionValueFunction(batchDataEnvironment = self.factory.createBatchDataEnvironment()
                                        , batchDataAgent = self.factory.createBatchDataAgent()
                                        , batchDataReward = self.factory.createBatchDataReward()
                                        , batchDataEnvironmentNextStep = self.factory.createBatchDataEnvironment())
        
        q0 = [v.numpy() for v in agent.policy.trainable_variables]
        q1 = [v.numpy() for v in agent.valueFunctionApproximator.trainable_variables]
        q2 = [v.numpy() for v in agent.featureExtractor.trainable_variables]
        
        assert len(p0) == len(q0)
        assert len(p1) == len(q1)
        assert len(p2) == len(q2)
        
        assert isEqual(p0, q0) == True
        assert isEqual(p1, q1) == False
#         assert isEqual(p2, q2) == False

    def test009(self):
        agent = self.factory.createAgent()
        agent2 = self.factory.createAgent()
        
        assert isinstance(agent, ConcreteAgent)
        
        saveFilePrefix = "foo"
        
        agent.reset()
        
        agent.updateStateValueFunction(batchDataEnvironment = self.factory.createBatchDataEnvironment())
        agent.updatePolicy(batchDataEnvironment = self.factory.createBatchDataEnvironment())
        agent.updateActionValueFunction(batchDataEnvironment = self.factory.createBatchDataEnvironment()
                                        , batchDataAgent = self.factory.createBatchDataAgent()
                                        , batchDataReward = self.factory.createBatchDataReward()
                                        , batchDataEnvironmentNextStep = self.factory.createBatchDataEnvironment())
        
        agent.saveNetworks(saveFilePrefix)
        
        agent2.reset()
        agent2.loadNetworks(saveFilePrefix)
        
        batchDataEnvironment = self.factory.createBatchDataEnvironment()
        batchDataAgent1 = agent.getAction(batchDataEnvironment)
        batchDataAgent2 = agent2.getAction(batchDataEnvironment)
        
        assert np.all(batchDataAgent1._Mean.numpy() == batchDataAgent2._Mean.numpy())
        
        shutil.rmtree(agent.saveFolderPath)
        
    def test010(self):
        agent = self.factory.createAgent()
        
        assert isinstance(agent, ConcreteAgent)
        
        agent.loadMemento(agent.createMemento())
        
        shutil.rmtree(agent.saveFolderPath)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()