'''
Created on 2020/11/28

@author: ukai
'''
from framework.trainer_factory import TrainerFactory
from concrete.concrete_trainer import ConcreteTrainer
from sac.sac_replay_buffer import SacReplayBuffer
from sac.sac_simulator_factory import SacSimulatorFactory

class ConcreteTrainerFactory(TrainerFactory):
    '''
    classdocs
    '''


    def create(self, buildParameter, agent, environment):
        trainer = ConcreteTrainer(agent, environment
                        , replayBuffer = SacReplayBuffer(bufferSize = buildParameter.bufferSizeReplayBuffer)
                        , simulatorFactory = SacSimulatorFactory(nSimulationStep=1)
                        , nStepEnvironment = buildParameter.nStepEnvironment
                        , nStepGradient = buildParameter.nStepGradient
                        , nIntervalUpdateStateValueFunction = buildParameter.nIntervalUpdateStateValueFunction
                        , nIterationPerEpoch = buildParameter.nIterationPerEpoch)
        trainer.reset()
        return trainer