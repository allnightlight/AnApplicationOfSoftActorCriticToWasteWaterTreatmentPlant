'''
Created on 2020/12/02

@author: ukai
'''
import unittest
from concrete.concrete_evaluation_db import ConcreteEvaluationDb
from concrete.concrete_build_parameter_factory import ConcreteBuildParameterFactory
from concrete.concrete_build_parameter import ConcreteBuildParameter


class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        
        cls.db = ConcreteEvaluationDb("test.sqlite", buildParameterFactory=ConcreteBuildParameterFactory())
        
    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        
#         cls.db.removeRemainedFiles()

    def test001(self):
        
        assert isinstance(self.db, ConcreteEvaluationDb)
        
        self.db.initDb()
        
    def test002(self):
        
        assert isinstance(self.db, ConcreteEvaluationDb)
        
        self.db.initDb()
        
        agentKey = "abc"
        epoch = 123
        evaluatorClass = "evaluator001"
        
        self.db.save(agentKey=agentKey, epoch=epoch, buildParameterLabel="test", buildParameterMemnto="who are you?", stats = {"count": 123, "XXX": 456}, evaluatorClass=evaluatorClass)
        
        assert self.db.exists(agentKey, epoch, evaluatorClass)
        assert self.db.exists(agentKey, epoch + 1, evaluatorClass) == False
        assert self.db.exists(agentKey + "hoge", epoch, evaluatorClass) == False
        assert self.db.exists(agentKey, epoch) 
        
        
    def test003(self):
        
        assert isinstance(self.db, ConcreteEvaluationDb)
        
        self.db.initDb()
        
        nRow = 3
        
        stats = {"count": 123, "XXX": 456}
        
        for k1 in range(nRow):
            agentKey = "abc %d" % k1
            buildParameterLabel = "test %d" % k1
            epoch = 123
            evaluatorClass = "evaluator001"
            
            buildParameter = ConcreteBuildParameter()        
            self.db.save(agentKey=agentKey, epoch=epoch, buildParameterLabel=buildParameterLabel, buildParameterMemnto=buildParameter.createMemento(), stats = stats, evaluatorClass=evaluatorClass)

        tbl = self.db.export()
        
        assert len(tbl) == nRow * len(stats)
                
        tbl = self.db.export("test 0")
                
        assert len(tbl) == len(stats), len(tbl)

        tbl = self.db.export("test%")
                
        assert len(tbl) == len(stats) * nRow, len(tbl)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test001']
    unittest.main()