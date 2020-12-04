'''
Created on 2020/11/29

@author: ukai
'''
from sac.sac_batch_data_agent import SacBatchDataAgent
from sac.sac_batch_data_environment import SacBatchDataEnvironment
from sac.sac_batch_data_reward import SacBatchDataReward
from sac.sac_simulator_factory import SacSimulatorFactory


class SacEvaluator(object):
    '''
    classdocs
    '''


    def evaluate(self, simulationResultGenerator):
        
        cnt = 0
        for batchDataEnvironment, batchDataAgent, batchDataReward, batchDataEnvironmentNextStep in simulationResultGenerator:
            
            assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
            assert isinstance(batchDataAgent, SacBatchDataAgent)
            assert isinstance(batchDataReward, SacBatchDataReward)
            assert isinstance(batchDataEnvironmentNextStep, SacBatchDataEnvironment)
            
            cnt += 1
            
        return dict(count = cnt)
    
    
class SacEvaluatorDummy(object):
    '''
    classdocs
    '''

    def __init__(self, simulatorFactory):
        
        assert isinstance(simulatorFactory, SacSimulatorFactory)
        self.simulatorFactory = simulatorFactory
        

    def evaluate(self, agent, environment, evaluateMethods):
        simulator = self.simulatorFactory.create(agent, environment)
        simulator.reset()
        
        g = [*simulator.generateSeries()]
        
        for evaluateMethod in evaluateMethods:
            yield evaluateMethod, evaluateMethod.evaluate(g) 