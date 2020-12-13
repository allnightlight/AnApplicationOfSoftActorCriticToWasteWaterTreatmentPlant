'''
Created on 2020/11/28

@author: ukai
'''
from framework.trainer_factory import TrainerFactory
from concrete.concrete_trainer import ConcreteTrainer
from sac.sac_replay_buffer import SacReplayBuffer
from sac.sac_simulator_factory import SacSimulatorFactory
from concrete.concrete_replay_buffer001 import ConcreteReplayBuffer001

class ConcreteTrainerFactory(TrainerFactory):
    '''
    classdocs
    '''


    def create(self, buildParameter, agent, environment):
        trainer = ConcreteTrainer(agent, environment
                        , replayBuffer = self.createReplayBuffer(buildParameter)
                        , simulatorFactory = SacSimulatorFactory(nSimulationStep=1)
                        , nStepEnvironment = buildParameter.nStepEnvironment
                        , nStepGradient = buildParameter.nStepGradient
                        , nIntervalUpdateStateValueFunction = buildParameter.nIntervalUpdateStateValueFunction
                        , nIterationPerEpoch = buildParameter.nIterationPerEpoch)
        trainer.reset()
        return trainer
    
    def createReplayBuffer(self, buildParameter):
        
        if buildParameter.replayBufferClass == "SacReplayBuffer":
            replayBuffer = SacReplayBuffer(bufferSize = buildParameter.bufferSizeReplayBuffer)
        if buildParameter.replayBufferClass == "ConcreteReplayBuffer001":
            replayBuffer = ConcreteReplayBuffer001(bufferSize = buildParameter.bufferSizeReplayBuffer, nBatch = buildParameter.nBatch)
            
        return replayBuffer