'''
Created on 2020/11/14

@author: ukai
'''
import unittest
from sac.sac_plant import SacPlant
from sac.sac_environment import SacEnvironment
from sac.sac_factory_for_test import SacFactoryForTest
from sac.sac_batch_data_environment import SacBatchDataEnvironment


class Test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.factory = SacFactoryForTest()

    def test001(self):
        
        plant = self.factory.createPlant()
        
        assert isinstance(plant, SacPlant)
        
        plant.reset()
        _ = plant.update(u = None)
        _ = plant.getPv()
        
        
    def test002(self):
        
        environment = self.factory.createEnvironment()
        
        assert isinstance(environment, SacEnvironment)
        
        environment.reset()
        environment.observe()
        environment.updateWithStochasticAction(self.factory.createBatchDataAgent())
        
        
    def test003(self):
        
        environment = self.factory.createEnvironment()
        
        assert isinstance(environment, SacEnvironment)

        assert isinstance(environment.getNmv(), int)
        assert isinstance(environment.getNpv(), int)

    def test004(self):
        
        environment = self.factory.createEnvironment()
        
        assert isinstance(environment, SacEnvironment)
        
        environment.reset()
        
        for k1 in range(2**3):

            batchDataEnvironment = environment.observe()        
            assert isinstance(batchDataEnvironment, SacBatchDataEnvironment)
            
            assert len(batchDataEnvironment.bufferMv) == k1
            assert len(batchDataEnvironment.bufferPv) == (k1+1)
            
            environment.updateWithStochasticAction(self.factory.createBatchDataAgent())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()