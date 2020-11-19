'''
Created on 2020/11/17

@author: ukai
'''
import unittest
from concrete.factory_for_test import FactoryForTest
from concrete.concrete_agent import ConcreteAgent
import tensorflow


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = FactoryForTest()


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

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()