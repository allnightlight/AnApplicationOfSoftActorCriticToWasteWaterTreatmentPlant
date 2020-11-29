'''
Created on 2020/11/23

@author: ukai
'''
from concrete.concrete_agent import ConcreteAgent
from concrete.concrete_feature_extractor001 import ConcreteFeatureExtractor001
from concrete.concrete_feature_extractor002 import ConcreteFeatureExtractor002
from concrete.concrete_plant001 import ConcretePlant001
from concrete.concrete_policy import ConcretePolicy
from concrete.concrete_value_function_approximator import ConcreteValueFunctionApproximator
from sac.sac_environment import SacEnvironment
from sac.sac_replay_buffer import SacReplayBuffer
from sac.sac_trainer import SacTrainer
from sanitycheck.work001_utility import Work001Utility


class Work002Utility(object):
    '''
    classdocs
    '''
    
    @classmethod
    def create(cls, alphaTemp = 1.0, discountFactor = 0.01, nIteration = 2**3, nIntervalUpdateStateValueFunction = 1, updatePolicyByAdvantage = False, featureExtractorType = "ConcreteFeatureExtractor001"):
        
        environment = SacEnvironment(plant = ConcretePlant001()) 
        
        nHidden = 2**3
        nSampleOfActionsInValueFunctionApproximator = 2**3
        nFeature = 2**0
        
        if featureExtractorType == "ConcreteFeatureExtractor001":
            featureExtractor = ConcreteFeatureExtractor001(nFeature=nFeature)
        if featureExtractorType == "ConcreteFeatureExtractor002":
            featureExtractor = ConcreteFeatureExtractor002(nFeature=environment.getNpv())

        
        agent = ConcreteAgent(policy = ConcretePolicy(nMv = environment.getNmv())
                    , valueFunctionApproximator = ConcreteValueFunctionApproximator(nFeature, environment.getNmv(), nSampleOfActionsInValueFunctionApproximator, nHidden)
                    , featureExtractor = featureExtractor
                    , discountFactor = discountFactor
                    , alphaTemp = alphaTemp
                    , updatePolicyByAdvantage = updatePolicyByAdvantage
                    , saveFolderPath = "./checkpoint")
        
        trainer = SacTrainer(agent = agent
                            , environment = environment
                            , replayBuffer = SacReplayBuffer(bufferSize = 2**10)
                            , nStepEnvironment = 1
                            , nStepGradient = 1
                            , nIntervalUpdateStateValueFunction = nIntervalUpdateStateValueFunction
                            , nIterationPerEpoch = 1)
        
        work001Utility = Work001Utility(nMv = trainer.environment.getNmv()
                                         , nPv = trainer.environment.getNpv()
                                         , nFeature = None
                                         , agent = trainer.agent
                                         , nIter = nIteration
                                         , showLog = False)
        
        return Work002Utility(trainer, nIteration, work001Utility)
                    
    def __init__(self, trainer, nIteration, work001Utility):
        '''
        Constructor
        '''        
                
        self.nIteration = nIteration
        
        self.trainer = trainer
         
        self.work001Utility = work001Utility
        
    def runTraining(self):

        self.trainer.reset()
        
        self.trainer.train()
        
    def plotTrainedQ(self):
        
        self.work001Utility.plotTrainedQ()
        
    def plotTrainedPi(self):
        
        self.work001Utility.plotTrainedPi()
        
        
    def checkTraining(self):
        
        self.runTraining()
        
        self.plotTrainedQ()
        
        self.plotTrainedPi()